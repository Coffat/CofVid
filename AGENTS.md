# CofVid - Agent Operating Rules

> **CRITICAL**: Read `AGENT_GUIDE.md` before responding to ANY user message. All production strictly follows CofVid's instruction-driven state machine.

---

## 1. Rule Zero — All Production Follows the Pipeline State Machine
Every video production request MUST go through the pipeline system:
`research -> proposal -> script -> scene_plan -> assets -> edit -> compose`

- **NO Skipping Stages**: Never jump ahead to `assets`, `vieneu_tts`, or `video_compose` before previous stages are completed and approved.
- **NO Ad-hoc Generation Scripts**: Strictly FORBIDDEN to create scripts like `generate_artifacts.py` or mock pipeline outputs. All canonical artifacts must be generated through real stage directors and registered tools.
- **Real Research Grounding**: For Mạch Số and fact-based explainers, `research` MUST execute `web_data_grounder` to record real facts into `grounded_facts.json`.

---

## 2. Checkpoint & Turn-Ending Protocol (Hard Gates)
When a stage requires human approval (`proposal`, `scene_plan`):
1. Write the checkpoint with `status: "awaiting_human"`.
2. Present the artifact summary, review findings, and cost snapshot.
3. **END YOUR TURN IMMEDIATELY**. Do NOT invoke any asset generation tools (TTS, image, video) in the same response.
4. Only advance after the user explicitly approves.

---

## 3. Proposal Gate — 7 Mandatory Decisions
At the `proposal` stage, you MUST synthesize and log ALL 7 core decisions into `decision_log.json`:
1. `approval_policy`: (e.g. stop at proposal & scene_plan gates)
2. `music_source`: (music library track or local selection)
3. `voice_selection`: (e.g. VieNeu-TTS Hải Đăng / Mai Anh)
4. `playbook_selection`: (e.g. Mạch Số Neo-Brutalist Tactile Bento)
5. `composition_mode`: (`atelier` for bespoke hand-authored or `templated`)
6. `render_runtime_selection`: (`hyperframes` primary default vs `remotion`)
7. `concept_selection`: (chosen angle from 3+ considered options)

---

## 4. HyperFrames Integration Scope
HyperFrames (`npx hyperframes`) is the **primary composition and rendering runtime** used at the `compose` stage (Atelier hand-authored or templated).
- HyperFrames domain skills (`hyperframes-animation`, `hyperframes-creative`, `hyperframes-media`) are mechanics codices for authoring scenes during `compose`.
- HyperFrames does **NOT** bypass CofVid's pipeline orchestration, research grounding, or checkpoint gates.

---

## 5. UI/UX Pro Max Mandatory Audit for Atelier Hand-Authoring
Khi sản xuất video cho các kênh của COFFAT MEDIA ở chế độ **Atelier Hand-Authoring** (Mạch Số, Vạn Vật, Dấu Mốc, Tâm Trí, Bàn Cờ):
- **Phân định quyền ưu tiên**: Brand Kit của kênh (`vertical-video-brand-kit/<channel>/design.md`) giữ quyền quyết định nhận diện cốt lõi (bảng màu canvas, viền thẻ bento, HUD phân tầng, safe area 9:16).
- **Vai trò cố vấn & kiểm định của `ui-ux-pro-max`**:
  - Tại giai đoạn `scene_plan`: Tra cứu nguyên tắc cấu trúc component, nhịp modular grid 8px, phân cấp typography.
  - Tại giai đoạn `compose`: Bắt buộc kiểm tra độ tương phản màu sắc (WCAG 4.5:1), tra cứu 17 GSAP animation presets / easing curve (`back.out`, `expo.out`, micro-interactions), và ghi nhận nhật ký kiểm định (**UI/UX Pro Max Audit**) vào `final_review.json`.

---

## 6. COFFAT MEDIA — 5 Dedicated Channel Director Skills
Khi sản xuất video cho 5 kênh của COFFAT MEDIA, Agent **BẮT BUỘC** kích hoạt đúng skill đạo diễn chuyên trách:
1. **Mạch Số** (`mach-so`): Kích hoạt `.agents/skills/mach-so-director/SKILL.md` (Neo-Brutalist Tactile Bento, 6 Developer Interaction Primitives, Cognitive Purpose Matrix, Hải Đăng 1.05x).
2. **Vạn Vật** (`van-vat`): Kích hoạt `.agents/skills/van-vat-director/SKILL.md` (National Geographic Field Journal & Minimalist Blueprint, Vernier Caliper, Mai Anh 1.0x).
3. **Dấu Mốc** (`dau-moc`): Kích hoạt `.agents/skills/dau-moc-director/SKILL.md` (Vox Paper Collage & Archival Documentary, Animated Pencil Routes, Hải Đăng 1.0x).
4. **Tâm Trí** (`tam-tri`): Kích hoạt `.agents/skills/tam-tri-director/SKILL.md` (Humanist Editorial & Kinetic Thought Typography, Candid B-roll, Mai Anh 1.0x).
5. **Bàn Cờ** (`ban-co`): Kích hoạt `.agents/skills/ban-co-director/SKILL.md` (Swiss Financial Bento Monolith, Frosted Cards blur 16px, SEC Footnotes, Hải Đăng 1.05x).

Skill `coffat-media-director` đóng vai trò là Master Router tự động phân tích prompt để điều phối sang đúng skill đạo diễn chuyên trách của kênh.
