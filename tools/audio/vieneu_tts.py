"""VieNeu-TTS local text-to-speech provider tool."""

from __future__ import annotations

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

_VIENEU_INSTANCE = None
_FALLBACK_VENV_PYTHON = Path("/Users/vuthang/Documents/VieNeu-TTS/.venv/bin/python")


def get_vieneu_instance():
    """Lazy loader and cache for Vieneu v3turbo instance."""
    global _VIENEU_INSTANCE
    if _VIENEU_INSTANCE is None:
        from vieneu import Vieneu

        _VIENEU_INSTANCE = Vieneu(mode="v3turbo")
    return _VIENEU_INSTANCE


class VieneuTTS(BaseTool):
    name = "vieneu_tts"
    version = "0.1.0"
    tier = ToolTier.SOURCE
    capability = "tts"
    provider = "vieneu"
    stability = ToolStability.PRODUCTION
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    dependencies = ["python:vieneu"]
    install_instructions = (
        "Install VieNeu-TTS:\n"
        "  pip install -e /Users/vuthang/Documents/VieNeu-TTS"
    )
    agent_skills = ["vieneu-tts", "text-to-speech"]

    capabilities = [
        "text_to_speech",
        "vietnamese_tts",
        "offline_generation",
    ]
    supports = {
        "voice_cloning": True,
        "multilingual": True,
        "offline": True,
        "native_audio": True,
    }
    best_for = [
        "natural Vietnamese speech synthesis",
        "primary Vietnamese voiceover",
        "offline neural narration",
    ]
    not_good_for = [
        "realtime low-latency streaming under 100ms on low-end CPUs",
    ]

    input_schema = {
        "type": "object",
        "required": ["text"],
        "properties": {
            "text": {
                "type": "string",
                "description": "Text to synthesize into Vietnamese speech.",
            },
            "output_path": {
                "type": "string",
                "description": "Output path where the generated audio file (.wav) will be saved.",
            },
            "voice": {
                "type": "string",
                "default": "Hải Đăng",
                "description": (
                    "Voice name to use. Default is 'Hải Đăng' (male). "
                    "Also supports 'Mai Anh' (female) and other preset voices."
                ),
            },
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=2, ram_mb=1024, vram_mb=0, disk_mb=500, network_required=False
    )
    retry_policy = RetryPolicy(max_retries=1, retryable_errors=[])
    idempotency_key_fields = ["text", "voice"]
    side_effects = ["writes audio file to output_path"]
    user_visible_verification = [
        "Listen to generated Vietnamese audio for naturalness and clarity"
    ]

    def get_status(self) -> ToolStatus:
        try:
            import vieneu  # noqa: F401

            return ToolStatus.AVAILABLE
        except Exception:
            if _FALLBACK_VENV_PYTHON.exists():
                return ToolStatus.AVAILABLE
            return ToolStatus.UNAVAILABLE

    def estimate_cost(self, inputs: dict[str, Any]) -> float:
        return 0.0

    def execute(self, params: dict[str, Any]) -> ToolResult:
        if self.get_status() != ToolStatus.AVAILABLE:
            return ToolResult(
                success=False,
                error=(
                    "VieNeu-TTS is not available. Please install it with:\n"
                    + self.install_instructions
                ),
            )

        text = (params.get("text") or "").strip()
        if not text:
            return ToolResult(success=False, error="Input text is empty.")

        output_path_str = params.get("output_path") or "output/vieneu_output.wav"
        output_path = Path(output_path_str).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)

        voice = params.get("voice") or "Hải Đăng"

        start_time = time.time()
        
        # Check if native import works
        try:
            import vieneu  # noqa: F401
            has_native = True
        except Exception:
            has_native = False

        if not has_native and _FALLBACK_VENV_PYTHON.exists():
            import subprocess
            import json
            runner_code = f"""
import sys, json, time
from pathlib import Path
from vieneu import Vieneu

tts = Vieneu(mode="v3turbo")
audio = tts.infer(text={repr(text)}, voice={repr(voice)})
tts.save(audio, {repr(str(output_path))})
sample_rate = getattr(tts, "sample_rate", 48000)
duration = round(len(audio) / sample_rate, 2) if len(audio) > 0 else 0.0
print(json.dumps({{"sample_rate": sample_rate, "duration": duration}}))
"""
            res = subprocess.run(
                [str(_FALLBACK_VENV_PYTHON), "-c", runner_code],
                capture_output=True,
                text=True,
            )
            if res.returncode != 0:
                return ToolResult(
                    success=False,
                    error=f"VieNeu-TTS fallback runner failed: {res.stderr}",
                    duration_seconds=round(time.time() - start_time, 2),
                )
            try:
                out_data = json.loads(res.stdout.strip().splitlines()[-1])
                duration = out_data.get("duration", 0.0)
                sample_rate = out_data.get("sample_rate", 48000)
            except Exception:
                duration = 0.0
                sample_rate = 48000

            elapsed = round(time.time() - start_time, 2)
            return ToolResult(
                success=True,
                data={
                    "audio_path": str(output_path),
                    "duration": duration,
                    "voice": voice,
                    "provider": self.provider,
                    "model": "v3turbo",
                    "text_length": len(text),
                    "sample_rate": sample_rate,
                },
                artifacts=[str(output_path)],
                duration_seconds=elapsed,
            )

        try:
            tts = get_vieneu_instance()
            audio = tts.infer(text=text, voice=voice)
            tts.save(audio, str(output_path))

            sample_rate = getattr(tts, "sample_rate", 48000)
            duration = round(len(audio) / sample_rate, 2) if len(audio) > 0 else 0.0
            elapsed = round(time.time() - start_time, 2)

            return ToolResult(
                success=True,
                data={
                    "audio_path": str(output_path),
                    "duration": duration,
                    "voice": voice,
                    "provider": self.provider,
                    "model": "v3turbo",
                    "text_length": len(text),
                    "sample_rate": sample_rate,
                },
                artifacts=[str(output_path)],
                duration_seconds=elapsed,
            )
        except Exception as exc:
            return ToolResult(
                success=False,
                error=f"VieNeu-TTS synthesis failed: {exc}",
                duration_seconds=round(time.time() - start_time, 2),
            )
