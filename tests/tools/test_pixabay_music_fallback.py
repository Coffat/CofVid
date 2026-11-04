"""Tests for PixabayMusic zero-failure fallback and error handling."""

from pathlib import Path
from unittest.mock import patch
import pytest

from tools.audio.pixabay_music import PixabayMusic


def test_pixabay_music_synthesizes_ambient_pad_on_network_failure(tmp_path):
    """When Pixabay scraping encounters 403 / Cloudflare, fallback synth generates audio."""
    tool = PixabayMusic()
    out_file = tmp_path / "ambient_test.mp3"

    with patch.object(tool, "_search", return_value=[]):
        with patch.object(tool, "_find_local_track", return_value=None):
            with patch.object(tool, "_search_and_download_wikimedia", return_value=False):
                res = tool.execute({
                    "query": "minimalist ambient tech",
                    "duration": 10,
                    "output_path": str(out_file),
                })

    assert res.success is True
    assert out_file.exists()
    assert out_file.stat().st_size > 1024
    assert res.data["format"] == "mp3"
    assert res.data["fallback_applied"] == "ffmpeg_ambient_synth"
    assert res.data["sample_rate"] == 48000
    assert res.data["channels"] == 2


def test_pixabay_music_local_library_fallback(tmp_path):
    """When music_library has tracks, tool prefers using the local track."""
    tool = PixabayMusic()
    out_file = tmp_path / "local_out.mp3"
    local_track = tmp_path / "chill_beats.mp3"
    local_track.write_bytes(b"MOCK_MP3_DATA" * 100)

    with patch.object(tool, "_search", return_value=[]):
        with patch.object(tool, "_find_local_track", return_value=local_track):
            res = tool.execute({
                "query": "chill beats",
                "output_path": str(out_file),
            })

    assert res.success is True
    assert out_file.exists()
    assert res.data["fallback_applied"] == "music_library"
    assert res.data["track_title"] == "chill_beats"


def test_pixabay_music_handles_flexible_inputs(tmp_path):
    """Tool accepts query, prompt, or keyword flexibly."""
    tool = PixabayMusic()
    out_file = tmp_path / "prompt_test.mp3"

    with patch.object(tool, "_search", return_value=[]):
        with patch.object(tool, "_find_local_track", return_value=None):
            res = tool.execute({
                "prompt": "deep meditation",
                "duration": 5,
                "output_path": str(out_file),
            })

    assert res.success is True
    assert out_file.exists()
    assert "deep meditation" in res.data["track_title"]
