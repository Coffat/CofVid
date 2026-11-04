"""Test asset tool gate validation."""

from pathlib import Path
import json
import pytest
from tests.contracts.test_phase0_contracts import sample_artifact
from tools.base_tool import BaseTool, ToolResult
from lib.checkpoint import init_project, write_checkpoint, GateViolationError


class DummyTTSTool(BaseTool):
    name = "dummy_tts"
    capability = "tts"

    def execute(self, inputs):
        return ToolResult(success=True, data={"audio": "ok"})


def test_asset_tool_gate_blocks_when_scene_plan_missing(tmp_path: Path):
    project_id = "test-gate-proj"
    init_project(project_id, title="Test Gate", pipeline_type="animated-explainer", pipeline_dir=tmp_path)

    tool = DummyTTSTool()
    out_file = tmp_path / project_id / "assets" / "audio" / "scene_01.wav"

    with pytest.raises(GateViolationError, match="because stage 'scene_plan' has not been completed"):
        tool.execute({"output_path": str(out_file), "text": "Hello"})


def test_asset_tool_gate_blocks_when_scene_plan_not_approved(tmp_path: Path):
    project_id = "test-gate-proj-unapproved"
    project_dir = init_project(project_id, title="Test Gate", pipeline_type="animated-explainer", pipeline_dir=tmp_path)

    # Directly create a checkpoint_scene_plan.json with status="awaiting_human"
    cp_path = project_dir / "checkpoint_scene_plan.json"
    cp_path.write_text(
        json.dumps({
            "stage": "scene_plan",
            "status": "awaiting_human",
            "human_approval_required": True,
            "human_approved": False,
        }),
        encoding="utf-8",
    )

    tool = DummyTTSTool()
    out_file = project_dir / "assets" / "audio" / "scene_01.wav"

    with pytest.raises(GateViolationError, match="must be 'completed'"):
        tool.execute({"output_path": str(out_file), "text": "Hello"})


def test_asset_tool_gate_allows_when_scene_plan_approved(tmp_path: Path):
    project_id = "test-gate-proj-approved"
    project_dir = init_project(project_id, title="Test Gate", pipeline_type="animated-explainer", pipeline_dir=tmp_path)

    # Directly create a valid approved checkpoint_scene_plan.json
    cp_path = project_dir / "checkpoint_scene_plan.json"
    cp_path.write_text(
        json.dumps({
            "stage": "scene_plan",
            "status": "completed",
            "human_approval_required": True,
            "human_approved": True,
        }),
        encoding="utf-8",
    )

    tool = DummyTTSTool()
    out_file = project_dir / "assets" / "audio" / "scene_01.wav"

    res = tool.execute({"output_path": str(out_file), "text": "Hello"})
    assert res.success is True


def test_asset_tool_gate_allows_bypass_or_dry_run(tmp_path: Path):
    project_id = "test-gate-bypass"
    project_dir = init_project(project_id, title="Test Gate", pipeline_type="animated-explainer", pipeline_dir=tmp_path)

    tool = DummyTTSTool()
    out_file = project_dir / "assets" / "audio" / "scene_01.wav"

    # With bypass flag
    res = tool.execute({"output_path": str(out_file), "text": "Hello", "bypass_pipeline_gate": True})
    assert res.success is True

    # With dry run
    res2 = tool.execute({"output_path": str(out_file), "text": "Hello", "dry_run": True})
    assert res2.success is True
