"""Unit tests for UIIconTool (Official Lucide/Feather UI Icon Resolver)."""

from __future__ import annotations

from pathlib import Path
import pytest

from tools.base_tool import ToolRuntime, ToolStatus, ToolTier
from tools.graphics.ui_icon_tool import (
    BUILTIN_UI_ICONS,
    UIIconTool,
    normalize_icon_name,
)


@pytest.fixture
def ui_tool() -> UIIconTool:
    return UIIconTool()


def test_ui_tool_contract(ui_tool: UIIconTool):
    """Verify tool identity, capabilities, and runtime contract."""
    assert ui_tool.name == "ui_icon_tool"
    assert ui_tool.capability == "graphics"
    assert ui_tool.provider == "ui_icon_resolver"
    assert ui_tool.runtime == ToolRuntime.LOCAL
    assert ui_tool.tier == ToolTier.CORE
    assert ui_tool.get_status() == ToolStatus.AVAILABLE
    assert "ui_icon" in ui_tool.capabilities
    assert "svg_icon" in ui_tool.capabilities
    assert "lucide_icon" in ui_tool.capabilities


def test_normalize_icon_name():
    """Verify UI icon slug normalization and aliases."""
    assert normalize_icon_name("Star") == "star"
    assert normalize_icon_name("terminal") == "terminal"
    assert normalize_icon_name("alert") == "alert-circle"
    assert normalize_icon_name("warning") == "alert-circle"
    assert normalize_icon_name("git_branch") == "git-branch"


def test_star_outline_and_filled(ui_tool: UIIconTool):
    """Verify genuine 5-point star polygon for both outline and filled variants."""
    star_polygon = "12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"

    # 1. Outline Variant
    res_outline = ui_tool.execute({
        "icon_name": "star",
        "variant": "outline",
        "color": "#00F0FF",
        "stroke_width": 2,
    })
    assert res_outline.success is True
    svg_out = res_outline.data["svg"]
    assert '<polygon points="' in svg_out
    assert star_polygon in svg_out
    assert 'fill="none"' in svg_out
    assert 'stroke="#00F0FF"' in svg_out
    assert 'viewBox="0 0 24 24"' in svg_out
    assert 'stroke-width="2"' in svg_out

    # 2. Filled Variant
    res_filled = ui_tool.execute({
        "icon_name": "star",
        "variant": "filled",
        "color": "#FFD700",
    })
    assert res_filled.success is True
    svg_fill = res_filled.data["svg"]
    assert '<polygon points="' in svg_fill
    assert star_polygon in svg_fill
    assert 'fill="#FFD700"' in svg_fill
    assert 'stroke="#FFD700"' in svg_fill


@pytest.mark.parametrize("icon_name", ["terminal", "shield", "code", "database", "check", "cpu", "server"])
def test_standard_ui_icons(ui_tool: UIIconTool, icon_name: str):
    """Verify key developer UI icons resolve correct Lucide paths."""
    res = ui_tool.execute({
        "icon_name": icon_name,
        "width": 32,
        "height": 32,
    })
    assert res.success is True
    assert res.data["slug"] == icon_name
    svg = res.data["svg"]
    assert 'viewBox="0 0 24 24"' in svg
    assert 'width="32"' in svg
    assert 'height="32"' in svg
    assert 'stroke="currentColor"' in svg
    assert 'fill="none"' in svg


def test_ui_icon_file_output(ui_tool: UIIconTool, tmp_path: Path):
    """Verify writing UI icon SVG directly to file."""
    target_file = tmp_path / "terminal_icon.svg"
    res = ui_tool.execute({
        "icon_name": "terminal",
        "output_format": "svg_file",
        "output_path": str(target_file),
    })
    assert res.success is True
    assert target_file.is_file()
    assert str(target_file) in res.artifacts
    content = target_file.read_text(encoding="utf-8")
    assert "<polyline" in content
    assert "<line" in content


def test_unknown_icon_error(ui_tool: UIIconTool):
    """Verify graceful error reporting when an unknown icon is requested."""
    res = ui_tool.execute({"icon_name": "non_existent_symbol_xyz"})
    assert res.success is False
    assert "not found in built-in UI icon library" in res.error
