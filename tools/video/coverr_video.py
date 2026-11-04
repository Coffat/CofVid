"""Stock video acquisition from Coverr (free, no API key required)."""

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
from tools.video.stock_sources.coverr import CoverrSource


class CoverrVideo(BaseTool):
    name = "coverr_video"
    version = "0.1.0"
    tier = ToolTier.SOURCE
    capability = "video_generation"
    provider = "coverr"
    stability = ToolStability.BETA
    execution_mode = ExecutionMode.SYNC
    determinism = Determinism.DETERMINISTIC
    runtime = ToolRuntime.LOCAL

    dependencies = []
    install_instructions = (
        "Coverr works without an API key (free tier, 50 req/hr).\n"
        "Optional: Set COVERR_API_KEY in .env for higher rate limits."
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
        "modern lifestyle and cinematic B-roll",
        "nature, urban, technology, abstract backgrounds",
        "high production quality curated footage (HD and 4K)",
        "free stock video — no cost, no API key required",
    ]
    not_good_for = [
        "custom AI scenes",
        "animated or stylized fantasy content",
        "offline use",
    ]
    fallback_tools = ["mixkit_video", "pixabay_video"]

    input_schema = {
        "type": "object",
        "required": ["query"],
        "properties": {
            "query": {"type": "string", "description": "Search term or prompt (max 100 chars)"},
            "prompt": {"type": "string", "description": "Alias for query"},
            "min_duration": {
                "type": "integer",
                "description": "Minimum duration in seconds",
            },
            "max_duration": {
                "type": "integer",
                "description": "Maximum duration in seconds",
            },
            "per_page": {"type": "integer", "default": 5, "minimum": 1, "maximum": 25},
            "page": {"type": "integer", "default": 1},
            "output_path": {"type": "string", "description": "Target file path for downloaded video"},
        },
    }

    resource_profile = ResourceProfile(
        cpu_cores=1, ram_mb=256, vram_mb=0, disk_mb=200, network_required=True
    )
    retry_policy = RetryPolicy(max_retries=2, retryable_errors=["rate_limit", "timeout"])
    idempotency_key_fields = ["query", "page"]
    side_effects = ["writes video file to output_path", "calls Coverr API"]
    user_visible_verification = ["Watch downloaded clip to verify it matches the intended scene"]

    def __init__(self) -> None:
        super().__init__()
        self._source = CoverrSource()

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
            return ToolResult(success=False, error="Query is required for Coverr video search.")

        filters = SearchFilters(
            kind="video",
            min_duration=inputs.get("min_duration"),
            max_duration=inputs.get("max_duration"),
            per_page=inputs.get("per_page", 5),
            page=inputs.get("page", 1),
        )

        try:
            candidates = self._source.search(query=query, filters=filters)
            if not candidates:
                return ToolResult(
                    success=False,
                    error=f"No Coverr videos found for query: {query}",
                    data={"total_results": 0},
                )

            candidate = candidates[0]
            output_str = inputs.get("output_path")
            if not output_str:
                safe_id = "".join(c for c in candidate.source_id if c.isalnum() or c in ("-", "_"))
                output_path = Path(f"coverr_{safe_id}.mp4")
            else:
                output_path = Path(output_str)

            self._source.download(candidate, output_path)

        except Exception as e:
            return ToolResult(success=False, error=f"Coverr video acquisition failed: {e}")

        return ToolResult(
            success=True,
            data={
                "provider": "coverr",
                "video_id": candidate.source_id,
                "user": candidate.creator or "Coverr Creator",
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
