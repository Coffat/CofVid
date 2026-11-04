from __future__ import annotations

from unittest.mock import MagicMock, patch

from tools.base_tool import ToolStatus, ToolTier
from tools.tool_registry import registry
from tools.video.coverr_video import CoverrVideo
from tools.video.mixkit_video import MixkitVideo
from tools.video.stock_sources.base import Candidate


def test_coverr_and_mixkit_registered():
    registry.ensure_discovered()
    coverr = registry.get("coverr_video")
    mixkit = registry.get("mixkit_video")

    assert coverr is not None
    assert isinstance(coverr, CoverrVideo)
    assert coverr.capability == "video_generation"
    assert coverr.provider == "coverr"
    assert coverr.tier == ToolTier.SOURCE
    assert coverr.get_status() == ToolStatus.AVAILABLE

    assert mixkit is not None
    assert isinstance(mixkit, MixkitVideo)
    assert mixkit.capability == "video_generation"
    assert mixkit.provider == "mixkit"
    assert mixkit.tier == ToolTier.SOURCE
    assert mixkit.get_status() == ToolStatus.AVAILABLE


def test_coverr_video_execute_mock(tmp_path):
    tool = CoverrVideo()
    fake_candidate = Candidate(
        source="coverr",
        source_id="test123",
        source_url="https://coverr.co/videos/test123",
        download_url="https://cdn.coverr.co/test123.mp4",
        kind="video",
        width=1920,
        height=1080,
        duration=12.5,
        creator="Test Creator",
        license="Coverr License",
        source_tags="nature forest trees",
    )

    out_file = tmp_path / "test_out.mp4"

    with patch.object(tool._source, "search", return_value=[fake_candidate]) as mock_search, \
         patch.object(tool._source, "download", return_value=out_file) as mock_download:
        res = tool.execute({"query": "forest", "output_path": str(out_file)})
        assert res.success is True
        assert res.data["provider"] == "coverr"
        assert res.data["video_id"] == "test123"
        assert res.data["duration_seconds"] == 12.5
        mock_search.assert_called_once()
        mock_download.assert_called_once()


def test_mixkit_video_execute_mock(tmp_path):
    tool = MixkitVideo()
    fake_candidate = Candidate(
        source="mixkit",
        source_id="mixkit_456",
        source_url="https://mixkit.co/free-stock-video/tech-456/",
        download_url="https://assets.mixkit.co/videos/preview/456.mp4",
        kind="video",
        width=1920,
        height=1080,
        duration=8.0,
        creator="Mixkit",
        license="Mixkit License",
        source_tags="tech business office",
    )

    out_file = tmp_path / "test_mixkit.mp4"

    with patch.object(tool._source, "search", return_value=[fake_candidate]) as mock_search, \
         patch.object(tool._source, "download", return_value=out_file) as mock_download:
        res = tool.execute({"query": "technology", "output_path": str(out_file)})
        assert res.success is True
        assert res.data["provider"] == "mixkit"
        assert res.data["video_id"] == "mixkit_456"
        mock_search.assert_called_once()
        mock_download.assert_called_once()


def test_video_selector_includes_coverr_and_mixkit():
    registry.ensure_discovered()
    vs = registry.get("video_selector")
    assert vs is not None
    provider_names = [p.name for p in vs._providers()]
    assert "coverr_video" in provider_names
    assert "mixkit_video" in provider_names
    assert "pixabay_video" in provider_names
    assert "pexels_video" not in provider_names
