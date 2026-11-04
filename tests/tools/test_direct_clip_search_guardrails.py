"""Tests for DirectClipSearch input schema normalization and guardrails."""

from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

from tools.video.direct_clip_search import DirectClipSearch
from tools.video.stock_sources.base import Candidate


def test_direct_clip_search_handles_flat_query_and_default_output_dir(tmp_path):
    """DirectClipSearch accepts flat 'query' string without 'queries' array or output_dir."""
    tool = DirectClipSearch()
    mock_src = MagicMock()
    mock_src.name = "mock_source"
    mock_src.is_available.return_value = True

    cand = Candidate(
        source="mock_source",
        source_id="123",
        source_url="https://example.com/123",
        download_url="https://example.com/123.mp4",
        kind="video",
    )
    mock_src.search.return_value = [cand]

    def mock_download(candidate, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"DATA" * 500)
        return path

    mock_src.download.side_effect = mock_download

    with patch("tools.video.stock_sources.available_sources", return_value=[mock_src]):
        with patch("tools.video.stock_sources.all_sources", return_value=[mock_src]):
            res = tool.execute({
                "query": "quantum physics",
                "output_dir": str(tmp_path / "custom_clips"),
                "clips_per_query": 1,
                "extract_thumbnails": False,
            })

    assert res.success is True
    assert res.data["clips_downloaded"] == 1
    assert res.data["queries_run"] == 1


def test_direct_clip_search_skips_oversized_clip(tmp_path):
    """Clips exceeding max_clip_size_bytes are skipped."""
    tool = DirectClipSearch()
    mock_src = MagicMock()
    mock_src.name = "mock_source"
    mock_src.is_available.return_value = True

    # Candidate with known large size in metadata (> 50MB)
    cand_huge = Candidate(
        source="mock_source",
        source_id="huge",
        source_url="https://example.com/huge",
        download_url="https://example.com/huge.mp4",
        kind="video",
        extra={"file_size_bytes": 100 * 1024 * 1024},
    )
    # Candidate with normal size
    cand_ok = Candidate(
        source="mock_source",
        source_id="ok",
        source_url="https://example.com/ok",
        download_url="https://example.com/ok.mp4",
        kind="video",
        extra={"file_size_bytes": 5 * 1024 * 1024},
    )
    mock_src.search.return_value = [cand_huge, cand_ok]

    def mock_download(candidate, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"DATA" * 500)
        return path

    mock_src.download.side_effect = mock_download

    with patch("tools.video.stock_sources.available_sources", return_value=[mock_src]):
        with patch("tools.video.stock_sources.all_sources", return_value=[mock_src]):
            res = tool.execute({
                "query": "universe cosmos",
                "output_dir": str(tmp_path / "clips"),
                "clips_per_query": 1,
                "max_clip_size_bytes": 50 * 1024 * 1024,
                "extract_thumbnails": False,
            })

    assert res.success is True
    assert res.data["clips_downloaded"] == 1
    assert res.data["clips"][0]["clip_id"] == "mock_source_ok"
    # huge clip should have been skipped and recorded in errors
    assert any("exceeds limit" in e.get("error", "") for e in res.data["errors"])
