"""Stock video acquisition from Mixkit by Envato (free, no API key required)."""

from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Any

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
from tools.video.stock_sources.base import SearchFilters
from tools.video.stock_sources.mixkit import MixkitSource


class MixkitVideo(BaseTool):
    name = "mixkit_video"
    version = "0.1.0"
    tier = ToolTier.SOURCE
    capability = "video_generation"
    provider = "mixkit"
    stability = ToolStability.BETA
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    dependencies = ["beautifulsoup4"]
    install_instructions = (
        "Mixkit works without an API key (scrapes mixkit.co curated videos).\n"
        "Requires beautifulsoup4: pip install beautifulsoup4"
    )
    agent_skills = []

    capabilities = ["search_video", "download_video", "stock_video"]
    supports = {
        "orientation_filter": False,
        "size_filter": False,
        "free_commercial_use": True,
        "no_attribution_required": True,
    }
    best_for = [
        "high-quality curated B-roll (nature, business, technology, lifestyle)",
        "clean, modern footage with consistent quality from Envato",
        "no-attribution-needed clips for quick gap-fills",
        "free stock video — no cost, no API key required",
    ]
    not_good_for = [
        "custom AI scenes",
        "animated or stylized fantasy content",
        "offline use",
    ]
    fallback_tools = ["coverr_video", "pixabay_video"]

    input_schema = {
        "type": "object",
        "required": ["query"],
        "properties": {
            "query": {"type": "string", "description": "Search term or prompt"},
            "prompt": {"type": "string", "description": "Alias for query"},
            "per_page": {"type": "integer", "default": 5, "minimum": 1, "maximum": 20},
            "page": {"type": "integer", "default": 1},
            "output_path": {"type": "string", "description": "Target file path for downloaded video"},
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=1, ram_mb=256, vram_mb=0, disk_mb=200, network_required=True
    )
    retry_policy = RetryPolicy(max_retries=2, retryable_errors=["rate_limit", "timeout"])
    idempotency_key_fields = ["query", "page"]
    side_effects = ["writes video file to output_path", "scrapes mixkit.co"]
    user_visible_verification = ["Watch downloaded clip to verify it matches the intended scene"]

    def __init__(self) -> None:
        super().__init__()
        self._source = MixkitSource()

    def get_status(self) -> ToolStatus:
        if self._source.is_available():
            return ToolStatus.AVAILABLE
        return ToolStatus.UNAVAILABLE

    def estimate_cost(self, inputs: dict[str, Any]) -> float:
        return 0.0

    def execute(self, inputs: dict[str, Any]) -> ToolResult:
        start = time.time()
        query = inputs.get("query") or inputs.get("prompt", "")
        if not query:
            return ToolResult(success=False, error="Query is required for Mixkit video search.")

        filters = SearchFilters(
            kind="video",
            per_page=inputs.get("per_page", 5),
            page=inputs.get("page", 1),
        )

        try:
            candidates = self._source.search(query=query, filters=filters)
            if not candidates:
                return ToolResult(
                    success=False,
                    error=f"No Mixkit videos found for query: {query}",
                    data={"total_results": 0},
                )

            candidate = candidates[0]
            output_str = inputs.get("output_path")
            if not output_str:
                safe_id = "".join(c for c in candidate.source_id if c.isalnum() or c in ("-", "_"))
                output_path = Path(f"mixkit_{safe_id}.mp4")
            else:
                output_path = Path(output_str)

            self._source.download(candidate, output_path)

        except Exception as e:
            return ToolResult(success=False, error=f"Mixkit video acquisition failed: {e}")

        return ToolResult(
            success=True,
            data={
                "provider": "mixkit",
                "video_id": candidate.source_id,
                "user": candidate.creator or "Mixkit",
                "tags": candidate.source_tags,
                "duration_seconds": candidate.duration,
                "width": candidate.width,
                "height": candidate.height,
                "query": query,
                "output": str(output_path),
                "total_results": len(candidates),
                "results_returned": len(candidates),
                "license": candidate.license,
                "page_url": candidate.source_url,
            },
            artifacts=[str(output_path)],
            cost_usd=0.0,
            duration_seconds=round(time.time() - start, 2),
        )
