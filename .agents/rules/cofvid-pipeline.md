# CofVid Pipeline & Anti-Shortcut Rules

> **Applies to**: All agents operating inside the CofVid workspace.

1. **State Machine Execution**: Always follow `research -> proposal -> script -> scene_plan -> assets -> edit -> compose`.
2. **No Ad-Hoc Scripts**: Never write ad-hoc Python scripts (e.g. `generate_artifacts.py`) to bypass pipeline steps or mock JSON artifacts.
3. **Mandatory Research Grounding**: Use `web_data_grounder` during research to ground all metrics and facts into `grounded_facts.json`.
4. **Mandatory 7 Proposal Decisions**: Log `approval_policy`, `music_source`, `voice_selection`, `playbook_selection`, `composition_mode`, `render_runtime_selection`, and `concept_selection` into `decision_log.json`.
5. **Human Gate Discipline**: When writing `status: "awaiting_human"` for gated stages (`proposal`, `scene_plan`), present the summary and **END TURN**. Never call asset tools (`vieneu_tts`, `pixabay_image`, `coverr_video`, etc.) before `checkpoint_scene_plan.json` is approved.
6. **HyperFrames Boundary**: HyperFrames is used as a render engine during `compose`. It does not replace the CofVid stage director lifecycle.
