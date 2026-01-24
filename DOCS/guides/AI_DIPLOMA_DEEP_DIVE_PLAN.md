# AI Diploma Deep-Dive Assessment Plan

**Purpose:** Master plan for aligning the AI Diploma repo with [DETAILED_UNIT_DESCRIPTIONS.md](../../DETAILED_UNIT_DESCRIPTIONS.md), improving reliability, understandability, and organization.  
**Reference:** [LEARNING_FLOW_ALIGNMENT_REPORT.md](../../LEARNING_FLOW_ALIGNMENT_REPORT.md), [COMPLETE_COURSE_STRUCTURE_AND_CLOS.md](../../COMPLETE_COURSE_STRUCTURE_AND_CLOS.md).

---

## 1. Scope

Score and improve:

| Dimension | Target | Initial score (0–10) |
|-----------|--------|----------------------|
| **Alignment** with DETAILED_UNIT_DESCRIPTIONS | 100% | ~7.5 |
| **Reliability** (“works well”) | All referenced notebooks run | ~7 |
| **Understandability** for students | Clear entry, progression, bilingual | ~7.5 |
| **Organization** | Consistent layout, minimal clutter | ~6.5 |

**Overall:** ~7/10 — good foundation; not yet 100% aligned or fully reliable/organized in every aspect.

---

## 2. Master Checklist

Use this as the **master to-do** for plan execution. Tick items as completed.

### 2.1 Alignment

- [x] **Fix Course 06 CLOs** — DETAILED + COMPLETE_COURSE_STRUCTURE: AI Ethics CLOs (not Data Science).
- [x] **Unify “Start with Course 01”** — README, STUDENT_GUIDE, etc.; optional note for Python-proficient → Course 02.
- [x] **Course 01 Unit 2/3 mapping** — Unit 2 → `unit2-ai-concepts/`, Unit 3 → `unit3-ml-basics/`; supplemental: `unit2-search-algorithms`, `unit3-knowledge-representation`.
- [x] **Course 01 duplicate-folder notices** — Canonical set only; supplemental READMEs for `unit1-introduction`, `unit4-neural-networks`, `unit5-generative-ai`, etc.
- [x] **Course 04 Unit 1 ↔ Regression Algorithms** — “Maps to” + scope note in `unit1-data-processing/README.md`.
- [x] **Un-ignore COMPLETE & LEARNING_FLOW** — `.gitignore` exceptions; both tracked and committed.
- [x] **Course 08/10 mapping docs** — LEARNING_FLOW: Course 08 unit structure row; Course 10 “mapping by position” already documented.

### 2.2 Reliability

- [x] **Quick-validate in SETUP_GUIDE** — `pip check` + `python -c "import numpy, pandas, sklearn; ..."` + optional notebook run.
- [ ] **Triage remaining failing notebooks** — Env/deps vs code bugs; fix or mark “optional/advanced.” (Deferred.)

### 2.3 Understandability

- [x] **Start-course consistency** — Covered by “Start with Course 01” unification.
- [x] **Course 01 canonical path** — START_HERE, README, QUIZZES, STUDENT_PROGRESS_CHECKLIST point to `unit2-ai-concepts`, `unit3-ml-basics`.

### 2.4 Organization

- [x] **Move root .md clutter → DOCS/guides/** — ASSESSMENT_ORGANIZATION, BEST_PRACTICES, IMPACT_ON_LEARNING, ORGANIZATION_ASSESSMENT, PROJECT_TEMPLATES_GUIDE.
- [x] **README link to DOCS/guides** — “Documentation & guides” under Quick Links.
- [ ] **Move Course 05 dev/QA artifacts** to META/ or dev/. (Deferred.)
- [ ] **Extend unique notebook naming** (e.g. Course 05–style) to 01, 02, 04, 06. (Deferred.)

### 2.5 Verification & Scan

- [x] **Scan notebooks for broken paths** — No critical breaks from renames/moves; Course 02 links to `unit1-data-processing`, `unit2-search-algorithms` still valid.
- [ ] **Optional: flowchart** of official path → detailed units. (Not created.)

---

## 3. Phase 2 (Optional / Deferred)

A **“deep deep dive”** would add:

- **Unit-by-unit audit** — All 60 units: each theory/practical bullet checked against notebooks/exercises.
- **CLO ↔ materials matrix** — Each CLO mapped to units and materials.
- **Explicit target state** for Course 08/10 — Where GANs/VAEs/RL, Text/Image/Ethics live; repo vs spec trade-offs.

These are **not required** for current alignment and learning-flow fixes. They improve guarantee of “100% aligned without changing again” if pursued later.

---

## 4. Execution Summary

**Commits (representative):**

1. `fix(alignment): Course 06 CLOs, Course 01 unit mapping, start-course consistency`
2. `chore: un-ignore COMPLETE_COURSE_STRUCTURE and LEARNING_FLOW_ALIGNMENT`
3. `feat(align): Course 04 mapping, quick-validate, DOCS/guides, Course 08 note`

**Files touched:**  
See [LEARNING_FLOW_ALIGNMENT_REPORT.md §6](../../LEARNING_FLOW_ALIGNMENT_REPORT.md) plus:  
Course 04 `unit1-data-processing/README.md`, `SETUP_GUIDE.md`, `DOCS/guides/` (moved guides), `README.md` (DOCS links), `LEARNING_FLOW_ALIGNMENT_REPORT` (Course 08 row).

---

## 5. References

| Doc | Purpose |
|-----|--------|
| [DETAILED_UNIT_DESCRIPTIONS.md](../../DETAILED_UNIT_DESCRIPTIONS.md) | Official curriculum; unit-level theory/practical |
| [LEARNING_FLOW_ALIGNMENT_REPORT.md](../../LEARNING_FLOW_ALIGNMENT_REPORT.md) | Alignment audit, official paths, remaining gaps |
| [COMPLETE_COURSE_STRUCTURE_AND_CLOS.md](../../COMPLETE_COURSE_STRUCTURE_AND_CLOS.md) | All 75 CLOs, unit structure |
| [ORGANIZATION_ASSESSMENT.md](ORGANIZATION_ASSESSMENT.md) | Root/course layout, clutter, Course 01 |
| [SETUP_GUIDE.md](../../SETUP_GUIDE.md) | Env setup, quick-validate |

---

**Last updated:** After “Continue” run (Course 04, SETUP_GUIDE, DOCS/guides, Course 08 note, commits above).
