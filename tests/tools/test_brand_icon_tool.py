"""Unit tests for BrandIconTool (Official Brand & Tech Logo Resolver)."""

from __future__ import annotations

import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from tools.base_tool import ToolRuntime, ToolStatus, ToolTier
from tools.graphics.brand_icon_tool import (
    BUILTIN_BRANDS,
    BrandIconTool,
    _normalize_name,
)
from tools.graphics.open_design_tool import OpenDesignTool


@pytest.fixture
def brand_tool() -> BrandIconTool:
    return BrandIconTool()


def test_brand_tool_contract(brand_tool: BrandIconTool):
    """Verify tool identity and capabilities contract."""
    assert brand_tool.name == "brand_icon_tool"
    assert brand_tool.capability == "graphics"
    assert brand_tool.provider == "brand_resolver"
    assert brand_tool.runtime == ToolRuntime.LOCAL
    assert brand_tool.tier == ToolTier.CORE
    assert brand_tool.get_status() == ToolStatus.AVAILABLE
    assert "brand_icon" in brand_tool.capabilities
    assert "svg_icon" in brand_tool.capabilities
    assert "vector_logo" in brand_tool.capabilities


def test_normalize_name_and_ai_aliases():
    """Verify slug normalization and modern AI alias resolution."""
    assert _normalize_name("GitHub") == "github"
    assert _normalize_name("gh") == "github"
    assert _normalize_name("py") == "python"
    assert _normalize_name("ChatGPT") == "chatgpt"
    assert _normalize_name("gpt-4") == "chatgpt"
    assert _normalize_name("googlegemini") == "gemini"
    assert _normalize_name("google-gemini") == "gemini"
    assert _normalize_name("claude-ai") == "claude"
    assert _normalize_name("deep-seek") == "deepseek"
    assert _normalize_name("mistralai") == "mistral"
    assert _normalize_name("cursor-ai") == "cursor"
    assert _normalize_name("hf") == "huggingface"


@pytest.mark.parametrize(
    "brand",
    [
        "github",
        "docker",
        "python",
        "react",
        "apple",
        "google",
        "aws",
        "openai",
        "anthropic",
        "linux",
        "microsoft",
        "typescript",
        "javascript",
        "rust",
        "kubernetes",
    ],
)
def test_builtin_tech_brands(brand_tool: BrandIconTool, brand: str):
    """Verify standard developer tech brands resolve authentic vector SVGs."""
    result = brand_tool.execute({"brand_name": brand, "output_format": "svg_snippet"})
    assert result.success is True
    assert result.data["provenance"] == "builtin"
    svg = result.data["svg"]
    assert "<svg" in svg
    assert "</svg>" in svg
    assert "viewBox" in svg


def test_top_ai_brands(brand_tool: BrandIconTool):
    """Verify top modern AI brand marks resolve authentic full-color vector SVGs."""
    # 1. Claude: Anthropic Claude terracotta (#D97757) 14-ray flower/sunburst
    res_claude = brand_tool.execute({"brand_name": "claude", "variant": "original"})
    assert res_claude.success is True
    assert res_claude.data["provenance"] == "builtin"
    assert res_claude.data["hex_color"] == "#D97757"
    assert "#D97757" in res_claude.data["svg"]
    assert "brand-claude" in res_claude.data["svg"]

    # 2. ChatGPT: Official emerald (#10A37F) hexagonal swirl
    res_chatgpt = brand_tool.execute({"brand_name": "chatgpt", "variant": "original"})
    assert res_chatgpt.success is True
    assert res_chatgpt.data["provenance"] == "builtin"
    assert res_chatgpt.data["hex_color"] == "#10A37F"
    assert "#10A37F" in res_chatgpt.data["svg"]
    assert "brand-chatgpt" in res_chatgpt.data["svg"]

    # 3. Gemini: Google Gemini 4-pointed star with blue/purple/magenta gradient
    res_gemini = brand_tool.execute({"brand_name": "gemini", "variant": "original"})
    assert res_gemini.success is True
    assert res_gemini.data["provenance"] == "builtin"
    assert "gemini-grad" in res_gemini.data["svg"]
    assert "linearGradient" in res_gemini.data["svg"]
    assert "brand-gemini" in res_gemini.data["svg"]

    # 4. DeepSeek: Official DeepSeek blue (#4D6BFE) whale
    res_deepseek = brand_tool.execute({"brand_name": "deepseek", "variant": "original"})
    assert res_deepseek.success is True
    assert res_deepseek.data["provenance"] == "builtin"
    assert res_deepseek.data["hex_color"] == "#4D6BFE"
    assert "#4D6BFE" in res_deepseek.data["svg"]

    # 5. Ollama: Official llama mark
    res_ollama = brand_tool.execute({"brand_name": "ollama"})
    assert res_ollama.success is True
    assert res_ollama.data["provenance"] == "builtin"

    # 6. Mistral AI: Orange chevron steps
    res_mistral = brand_tool.execute({"brand_name": "mistral"})
    assert res_mistral.success is True
    assert res_mistral.data["hex_color"] == "#FF7000"


def test_star_delegation_to_ui_icon_tool(brand_tool: BrandIconTool):
    """Verify that calling 'star' in brand_icon_tool delegates to ui_icon_tool and NEVER creates an 'S' letter badge."""
    star_polygon = "12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"

    result = brand_tool.execute({"brand_name": "star"})
    assert result.success is True
    assert result.data["provenance"] == "ui_icon_delegated"
    svg = result.data["svg"]

    # Genuine 5-point star polygon MUST be present
    assert "<polygon" in svg
    assert star_polygon in svg

    # Initial badge MUST NOT be present!
    assert "brand-badge" not in svg
    assert ">S</text>" not in svg
    assert "dominant-baseline" not in svg


def test_ui_icons_delegation_variety(brand_tool: BrandIconTool):
    """Verify terminal, shield, and code also delegate automatically."""
    for icon in ["terminal", "shield", "code"]:
        result = brand_tool.execute({"brand_name": icon})
        assert result.success is True
        assert result.data["provenance"] == "ui_icon_delegated"
        assert f"icon-{icon}" in result.data["svg"]
        assert "brand-badge" not in result.data["svg"]


def test_variants_transformation(brand_tool: BrandIconTool):
    """Verify monochrome, light, and dark variant transformations."""
    # 1. Monochrome
    res_mono = brand_tool.execute({
        "brand_name": "chatgpt",
        "variant": "monochrome",
    })
    assert res_mono.success is True
    assert 'fill="currentColor"' in res_mono.data["svg"]

    # 2. Light
    res_light = brand_tool.execute({
        "brand_name": "claude",
        "variant": "light",
    })
    assert res_light.success is True
    assert 'fill="#ffffff"' in res_light.data["svg"]

    # 3. Dark
    res_dark = brand_tool.execute({
        "brand_name": "claude",
        "variant": "dark",
    })
    assert res_dark.success is True
    assert 'fill="#18181b"' in res_dark.data["svg"]


def test_svg_file_output(brand_tool: BrandIconTool, tmp_path: Path):
    """Verify saving vector SVG directly to file."""
    target_file = tmp_path / "claude_logo.svg"
    result = brand_tool.execute({
        "brand_name": "claude",
        "output_format": "svg_file",
        "output_path": str(target_file),
    })
    assert result.success is True
    assert target_file.is_file()
    assert str(target_file) in result.artifacts
    content = target_file.read_text(encoding="utf-8")
    assert "<svg" in content
    assert "viewBox" in content
    assert "#D97757" in content


def test_open_design_brand_icon_embedding():
    """Verify open_design_tool embeds brand icon into fullscreen_card, stat_callout, and lower_third."""
    od = OpenDesignTool()

    # 1. Fullscreen Card with GitHub Icon
    res_card = od.execute({
        "component_type": "fullscreen_card",
        "theme_id": "editorial",
        "props": {
            "brand_slug": "github",
            "kicker": "TECH REVOLUTION",
            "title": "Decentralized Collaboration",
            "body": "How open source transformed software development forever.",
        },
    })
    assert res_card.success is True
    dom_card = res_card.data["dom_snippet"]
    assert "od-brand-icon" in dom_card
    assert "<svg" in dom_card

    # 2. Stat Callout with Docker Icon
    res_stat = od.execute({
        "component_type": "stat_callout",
        "theme_id": "dark-data",
        "props": {
            "brand_slug": "docker",
            "stat": "100M+",
            "title": "Containers Deployed",
            "meta": "SOURCE: VERIFIED METRICS",
        },
    })
    assert res_stat.success is True
    dom_stat = res_stat.data["dom_snippet"]
    assert "od-brand-icon" in dom_stat
    assert "100M+" in dom_stat
    assert "<svg" in dom_stat
