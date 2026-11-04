"""Gemini Desktop Bridge tool.

Integrates with the local Gemini Desktop helper binary (`agy`) to execute prompts
via CLI subprocess execution.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Optional

from tools.base_tool import (
    BaseTool,
    Determinism,
    ExecutionMode,
    ResourceProfile,
    RetryPolicy,
    ToolResult,
    ToolRuntime,
    ToolStability,
    ToolStatus,
    ToolTier,
)

DEFAULT_AGY_PATH = Path("/Applications/Gemini.app/Contents/Helpers/agy")


def get_agy_path() -> Path:
    """Resolve the path to the agy helper binary."""
    custom = os.getenv("GEMINI_DESKTOP_AGY_PATH") or os.getenv("AGY_PATH")
    if custom:
        return Path(custom).resolve()
    if DEFAULT_AGY_PATH.exists():
        return DEFAULT_AGY_PATH
    on_path = shutil.which("agy")
    if on_path:
        return Path(on_path).resolve()
    return DEFAULT_AGY_PATH


def query_gemini_desktop(
    prompt: str,
    timeout: int = 120,
    binary_path: Optional[str | Path] = None,
    extra_args: Optional[list[str]] = None,
) -> str:
    """Send a prompt to the Gemini Desktop agy CLI and return the response text.

    Args:
        prompt: The prompt text to evaluate.
        timeout: Subprocess execution timeout in seconds (default 120).
        binary_path: Optional path to override the agy binary.
        extra_args: Optional list of additional CLI flags.

    Returns:
        The response string from Gemini Desktop CLI.

    Raises:
        FileNotFoundError: If the agy binary does not exist.
        TimeoutError: If the command exceeds the timeout.
        RuntimeError: If the CLI process fails or exits with non-zero status.
    """
    path = Path(binary_path).resolve() if binary_path else get_agy_path()
    if not path.exists():
        raise FileNotFoundError(
            f"Gemini Desktop helper binary not found at '{path}'. "
            "Please ensure Gemini Desktop is installed or set GEMINI_DESKTOP_AGY_PATH."
        )

    cmd = [str(path), "--print", prompt]
    if extra_args:
        cmd.extend(extra_args)

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise TimeoutError(
            f"Gemini Desktop CLI timed out after {timeout} seconds."
        ) from exc
    except Exception as exc:
        raise RuntimeError(f"Failed to execute Gemini Desktop CLI: {exc}") from exc

    if proc.returncode != 0:
        error_msg = proc.stderr.strip() or proc.stdout.strip() or f"exit code {proc.returncode}"
        raise RuntimeError(f"Gemini Desktop CLI failed: {error_msg}")

    return proc.stdout.strip()


class GeminiDesktopBridge(BaseTool):
    name = "gemini_desktop_bridge"
    version = "0.1.0"
    tier = ToolTier.SOURCE
    capability = "llm_bridge"
    provider = "gemini_desktop"
    stability = ToolStability.PRODUCTION
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.STOCHASTIC
    runtime = ToolRuntime.LOCAL

    dependencies = [f"file:{DEFAULT_AGY_PATH}"]
    install_instructions = (
        "Install Gemini Desktop on macOS (/Applications/Gemini.app) "
        "or specify path via GEMINI_DESKTOP_AGY_PATH."
    )
    agent_skills = ["antigravity-guide"]

    capabilities = [
        "desktop_prompting",
        "llm_bridge",
        "local_agent_query",
    ]
    supports = {
        "offline": False,
        "streaming": False,
        "direct_print": True,
    }
    best_for = [
        "leveraging local Gemini Desktop session for prompt reasoning",
        "desktop LLM bridge without separate cloud API keys",
    ]
    not_good_for = [
        "high concurrency batch requests",
    ]

    input_schema = {
        "type": "object",
        "required": ["prompt"],
        "properties": {
            "prompt": {
                "type": "string",
                "description": "Prompt text to send to Gemini Desktop CLI.",
            },
            "timeout": {
                "type": "integer",
                "default": 120,
                "description": "Timeout in seconds for response.",
            },
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=1, ram_mb=256, vram_mb=0, disk_mb=0, network_required=True
    )
    retry_policy = RetryPolicy(max_retries=1, retryable_errors=[])
    side_effects = ["executes prompt via Gemini desktop helper"]

    def get_status(self) -> ToolStatus:
        path = get_agy_path()
        if path.exists() and os.access(path, os.X_OK):
            return ToolStatus.AVAILABLE
        return ToolStatus.UNAVAILABLE

    def estimate_cost(self, inputs: dict[str, Any]) -> float:
        return 0.0

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        if self.get_status() != ToolStatus.AVAILABLE:
            return ToolResult(
                success=False,
                error=f"Gemini Desktop bridge unavailable: {self.install_instructions}",
            )

        prompt = (inputs.get("prompt") or "").strip()
        if not prompt:
            return ToolResult(success=False, error="Prompt cannot be empty.")

        timeout = int(inputs.get("timeout") or 120)
        start_time = time.time()

        try:
            output_text = query_gemini_desktop(prompt=prompt, timeout=timeout)
            elapsed = round(time.time() - start_time, 2)
            return ToolResult(
                success=True,
                data={
                    "response": output_text,
                    "prompt_length": len(prompt),
                    "response_length": len(output_text),
                    "provider": self.provider,
                },
                duration_seconds=elapsed,
            )
        except Exception as exc:
            elapsed = round(time.time() - start_time, 2)
            return ToolResult(
                success=False,
                error=str(exc),
                duration_seconds=elapsed,
            )
