"""Unit tests for open_design_tool."""

from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path

import pytest

from tools.base_tool import ToolStatus, ToolTier, ToolStability
from tools.graphics.open_design_tool import OpenDesign, OpenDesignTool
from tools.tool_registry import ToolRegistry


def test_open_design_tool_registration() -> None:
    """Verify OpenDesignTool is registered in ToolRegistry."""
    registry = ToolRegistry()
    from tools.graphics import open_design_tool
    registered = registry.register_module(open_design_tool)
    assert "open_design_tool" in registered

    tool = registry.get("open_design_tool")
    assert tool is not None
    assert tool.name == "open_design_tool"
    assert tool.tier == ToolTier.CORE
    assert tool.stability == ToolStability.BETA
    assert tool.capability == "graphics"
    assert tool.provider == "open_design"
    assert tool.get_status() == ToolStatus.AVAILABLE
    assert OpenDesignTool is OpenDesign


def test_theme_token_resolution() -> None:
    """Verify theme token resolution handles standard IDs, aliases, and fallbacks."""
    tool = OpenDesign()

    # Editorial theme
    theme, tokens, css = tool._resolve_theme_tokens("editorial")
    assert theme == "editorial"
    assert "--bg" in tokens
    assert "--fg" in tokens
    assert "--accent" in tokens
    assert ":root" in css

    # Swiss editorial alias -> editorial
    theme_alias, tokens_alias, _ = tool._resolve_theme_tokens("swiss-editorial")
    assert theme_alias == "editorial"
    assert "--accent" in tokens_alias

    # Dark data
    theme_dark, tokens_dark, _ = tool._resolve_theme_tokens("dark-data")
    assert theme_dark == "dark-data"
    assert "--bg" in tokens_dark

    # Unknown theme fallback -> editorial
    theme_fallback, tokens_fallback, _ = tool._resolve_theme_tokens("completely_unknown_theme_xyz")
    assert "--bg" in tokens_fallback


@pytest.mark.parametrize(
    "component_type,props",
    [
        (
            "fullscreen_card",
            {
                "kicker": "ACT I",
                "title": "The Quantum Shift",
                "subtitle": "How microarchitectures evolved.",
                "body": "In 2026, autonomous runtimes replaced legacy clouds.",
                "meta": "ARCHIVE / OCT 2026",
            },
        ),
        (
            "lower_third",
            {
                "kicker": "DIRECTOR",
                "title": "Dr. Sarah Connor",
                "subtitle": "Cybernetics Institute",
                "meta": "LOS ANGELES, CA",
            },
        ),
        (
            "stat_callout",
            {
                "kicker": "METRIC",
                "stat": "+340%",
                "title": "Throughput Acceleration",
                "body": "Observed across 1,000 nodes under continuous stress tests.",
                "meta": "SOURCE: BENCHMARK 2026",
            },
        ),
        (
            "split_screen",
            {
                "kicker": "COMPARISON",
                "title": "Legacy vs Modern",
                "left": {"kicker": "OLD", "title": "Monolith", "stat": "120s", "body": "High latency."},
                "right": {"kicker": "NEW", "title": "Microkernel", "stat": "3ms", "body": "Zero latency."},
                "meta": "TEST SUITE v4",
            },
        ),
        (
            "timeline_step",
            {
                "step_number": "02",
                "kicker": "PHASE II",
                "title": "Silicon Integration",
                "subtitle": "Transition to single-die chips.",
                "body": "Discrete logic gave way to unified architectures.",
                "meta": "1974",
            },
        ),
        (
            "quote_card",
            {
                "kicker": "TESTIMONY",
                "quote": "Simplicity is prerequisite for reliability.",
                "author": "Edsger W. Dijkstra",
                "role": "Computer Scientist",
                "meta": "TURING LECTURE",
            },
        ),
    ],
)
def test_generate_dom_snippet_components(component_type: str, props: dict) -> None:
    """Verify generating dom_snippet for all 6 component types."""
    tool = OpenDesign()
    res = tool.execute(
        {
            "mode": "template",
            "theme_id": "editorial",
            "component_type": component_type,
            "props": props,
            "output_format": "dom_snippet",
            "width": 1920,
            "height": 1080,
        }
    )

    assert res.success is True, f"Failed for {component_type}: {res.error}"
    assert res.data["component_type"] == component_type
    assert res.data["output_format"] == "dom_snippet"
    assert "<!DOCTYPE html>" in res.data["dom_snippet"]
    assert "od-canvas" in res.data["dom_snippet"]
    assert res.data["metadata"]["generator"] == "open_design_tool"


def test_custom_mode_dom_snippet(tmp_path: Path) -> None:
    """Verify custom HTML/CSS mode and output_path file export."""
    tool = OpenDesign()
    out_html = tmp_path / "custom_output.html"
    custom_markup = "<div class='my-custom-box'><h1>Custom Title</h1></div>"

    res = tool.execute(
        {
            "mode": "custom",
            "theme_id": "dark-data",
            "custom_code": custom_markup,
            "output_format": "dom_snippet",
            "output_path": str(out_html),
        }
    )

    assert res.success is True
    assert res.data["mode"] == "custom"
    assert out_html.is_file()
    content = out_html.read_text(encoding="utf-8")
    assert custom_markup in content
    assert "--bg: #0b0f19" in content


def test_unsupported_output_format() -> None:
    """Verify proper error reporting for unsupported output formats."""
    tool = OpenDesign()
    res = tool.execute({"output_format": "mp3_audio"})
    assert res.success is False
    assert "Unsupported output_format" in (res.error or "")


def test_png_and_webm_rendering(tmp_path: Path) -> None:
    """Verify headless Chrome PNG screenshot and FFmpeg transparent WebM rendering."""
    tool = OpenDesign()

    # 1. Test PNG rendering
    png_out = tmp_path / "test_card.png"
    res_png = tool.execute(
        {
            "theme_id": "editorial",
            "component_type": "stat_callout",
            "props": {
                "kicker": "EFFICIENCY",
                "stat": "99.8%",
                "title": "System Uptime",
                "body": "Continuous operation across the telemetry lifecycle.",
            },
            "output_format": "png_still",
            "output_path": str(png_out),
            "width": 1280,
            "height": 720,
        }
    )

    # If Chrome is installed on the machine, verify success and file creation
    chrome_available = shutil.which("google-chrome") or shutil.which("chrome") or os.path.exists(
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    )
    if chrome_available:
        assert res_png.success is True, f"PNG render failed: {res_png.error}"
        assert png_out.is_file()
        assert png_out.stat().st_size > 0
        assert res_png.data["file_size_bytes"] > 0

    # 2. Test WebM alpha rendering
    webm_out = tmp_path / "test_lower_third.webm"
    res_webm = tool.execute(
        {
            "theme_id": "editorial",
            "component_type": "lower_third",
            "props": {
                "name": "Dr. Elena Rostova",
                "role": "Lead Architect",
            },
            "output_format": "webm_alpha",
            "output_path": str(webm_out),
            "width": 1280,
            "height": 720,
            "duration_seconds": 1.0,
        }
    )

    ffmpeg_available = shutil.which("ffmpeg") is not None
    if chrome_available and ffmpeg_available:
        assert res_webm.success is True, f"WebM render failed: {res_webm.error}"
        assert webm_out.is_file()
        assert webm_out.stat().st_size > 0
        assert res_webm.data["file_size_bytes"] > 0
        assert res_webm.data["metadata"]["codec"] == "vp9_yuva420p"
