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
- [x] **Triage remaining failing notebooks** — [artifacts/NOTEBOOK_TRIAGE.md](../../artifacts/NOTEBOOK_TRIAGE.md): env/deps vs code bugs; optional/advanced marked; SETUP_GUIDE Troubleshooting links to it.

### 2.3 Understandability

- [x] **Start-course consistency** — Covered by “Start with Course 01” unification.
- [x] **Course 01 canonical path** — START_HERE, README, QUIZZES, STUDENT_PROGRESS_CHECKLIST point to `unit2-ai-concepts`, `unit3-ml-basics`.

### 2.4 Organization

- [x] **Move root .md clutter → DOCS/guides/** — ASSESSMENT_ORGANIZATION, BEST_PRACTICES, IMPACT_ON_LEARNING, ORGANIZATION_ASSESSMENT, PROJECT_TEMPLATES_GUIDE.
- [x] **README link to DOCS/guides** — “Documentation & guides” under Quick Links.
- [x] **Move Course 05 dev/QA artifacts** to **`Course 05/META/`** — execution_results, FINAL_*, EXECUTION_*, GPU_*; META/README.md added. ORGANIZATION_ASSESSMENT updated.
- [x] **Notebook naming** — Documented in [BEST_PRACTICES](BEST_PRACTICES.md) (§ Notebook Naming Convention); Course 05 template; extend to 01/02/04/06 as feasible.

### 2.5 Verification & Scan

- [x] **Scan notebooks for broken paths** — No critical breaks from renames/moves; Course 02 links to `unit1-data-processing`, `unit2-search-algorithms` still valid.
- [x] **Flowchart** — [OFFICIAL_PATH_FLOWCHART.md](OFFICIAL_PATH_FLOWCHART.md): official path → detailed units; LEARNING_FLOW §5 updated.

---

## 3. Phase 2 — Done

- [x] **Unit-by-unit audit** — [UNIT_BY_UNIT_AUDIT.md](UNIT_BY_UNIT_AUDIT.md): all 60 units mapped to DETAILED + repo path, examples, exercises, coverage.
- [x] **CLO ↔ materials matrix** — [CLOS_MATERIALS_MATRIX.md](CLOS_MATERIALS_MATRIX.md): all 75 CLOs → units and key materials.
- **Course 08/10 target state** — Documented in LEARNING_FLOW §5 and UNIT_BY_UNIT_AUDIT (mapping by position; no content reorganization).

---

## 4. Execution Summary

**Commits (representative):**

1. `fix(alignment): Course 06 CLOs, Course 01 unit mapping, start-course consistency`
2. `chore: un-ignore COMPLETE_COURSE_STRUCTURE and LEARNING_FLOW_ALIGNMENT`
3. `feat(align): Course 04 mapping, quick-validate, DOCS/guides, Course 08 note`
4. `docs: add AI Diploma Deep-Dive Plan, link from README`
5. *(This run)* Triage, Course 05 META, naming doc, flowchart, Phase 2 audit + CLO matrix, deep review, plan/report updates.

**Files touched:**  
[LEARNING_FLOW_ALIGNMENT_REPORT.md §6](../../LEARNING_FLOW_ALIGNMENT_REPORT.md) plus:  
`artifacts/NOTEBOOK_TRIAGE.md`, `Course 05/META/` (dev/QA moves), `SETUP_GUIDE.md` (quick-validate, NOTEBOOK_TRIAGE link), `DOCS/guides/BEST_PRACTICES.md` (notebook naming), `DOCS/guides/ORGANIZATION_ASSESSMENT.md` (Course 05 META), `DOCS/guides/OFFICIAL_PATH_FLOWCHART.md`, `DOCS/guides/UNIT_BY_UNIT_AUDIT.md`, `DOCS/guides/CLOS_MATERIALS_MATRIX.md`, `LEARNING_FLOW_ALIGNMENT_REPORT` (flowchart row).

**Latest (finish-it-all run):**  
- **Syntax fixes:** Course 03 `06_transformation_matrices_orthogonal_basis`, `05_function_approximation_ml`, `06_maximum_likelihood_estimation` (indentation, duplicate code, `intercept_print`, Hessian, `gammaln`). NOTEBOOK_TRIAGE §3 updated.  
- **Course 08/10 target state:** UNIT_BY_UNIT_AUDIT Summary.  
- **MASTER_NOTEBOOK_INDEX:** Created at root; SETUP_GUIDE, STUDENT_HANDBOOK reference it.  
- **Notebook renames:** Course 01 unit1 `implementing_search_algorithms...` → `10_implementing_search_algorithms.ipynb`, `working_with_numpy...` → `11_working_with_numpy.ipynb`. UNIT_BY_UNIT_AUDIT, MASTER_NOTEBOOK_INDEX updated.

---

## 5. References

| Doc | Purpose |
|-----|--------|
| [DETAILED_UNIT_DESCRIPTIONS.md](../../DETAILED_UNIT_DESCRIPTIONS.md) | Official curriculum; unit-level theory/practical |
| [LEARNING_FLOW_ALIGNMENT_REPORT.md](../../LEARNING_FLOW_ALIGNMENT_REPORT.md) | Alignment audit, official paths, remaining gaps |
| [COMPLETE_COURSE_STRUCTURE_AND_CLOS.md](../../COMPLETE_COURSE_STRUCTURE_AND_CLOS.md) | All 75 CLOs, unit structure |
| [ORGANIZATION_ASSESSMENT.md](ORGANIZATION_ASSESSMENT.md) | Root/course layout, clutter, Course 01, Course 05 META |
| [SETUP_GUIDE.md](../../SETUP_GUIDE.md) | Env setup, quick-validate, NOTEBOOK_TRIAGE link |
| [artifacts/NOTEBOOK_TRIAGE.md](../../artifacts/NOTEBOOK_TRIAGE.md) | Notebook failure triage; env vs code; optional/advanced |
| [OFFICIAL_PATH_FLOWCHART.md](OFFICIAL_PATH_FLOWCHART.md) | Official path → detailed units flowchart |
| [UNIT_BY_UNIT_AUDIT.md](UNIT_BY_UNIT_AUDIT.md) | 60-unit audit; unit ↔ materials |
| [CLOS_MATERIALS_MATRIX.md](CLOS_MATERIALS_MATRIX.md) | 75 CLOs ↔ units and materials |
| [MASTER_NOTEBOOK_INDEX.md](../../MASTER_NOTEBOOK_INDEX.md) | Notebook navigation by course/unit |

---

**Last updated:** After full plan execution (triage, META, naming, flowchart, Phase 2 audit, deep review).
