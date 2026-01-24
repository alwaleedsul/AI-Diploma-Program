# Course 05 – Scoring Rubric & Scorecard

**Purpose:** Explicit criteria and numeric scores for the Course 05 deep dives (Units 1–5).  
**Reference:** `DETAILED_UNIT_DESCRIPTIONS.md`; deep dive reports (`UNIT1_DEEP_DIVE.md`, `DEEP_DIVE_UNITS_2_5.md`).

---

## 1. Scoring rubric (per unit)

Each unit is scored on **four criteria**, **0–25 points** each → **max 100 per unit**.

| Criterion | Max | What we measure | 25 | 20 | 15 | 10 | 0–5 |
|-----------|-----|------------------|----|----|----|----|-----|
| **A. Spec alignment** | 25 | Theory + practical from `DETAILED_UNIT_DESCRIPTIONS` | All covered | 1–2 minor gaps | Several gaps | Major gaps | Missing entire areas |
| **B. Execution** | 25 | All example notebooks run via `jupyter nbconvert --execute` | All run | 1–2 skip/fail (optional) | Several fail | Most fail | All fail |
| **C. Inputs & outputs** | 25 | Code cells executed; outputs present and sensible | All executed, minimal intentional empty | Few unexecuted/empty (documented) | Several empty | Many missing | Mostly broken |
| **D. Exercise + solution** | 25 | `exercise_01` + `solutions/solution_01.ipynb` present, complete, runnable | Both present, full solution, runs | Solution partial or 1 issue | Exercise only | Neither | — |

**Course score** = unweighted average of the five unit scores (0–100).

---

## 2. How each unit was scored

### Unit 1: Introduction to Data Science

| Criterion | Score | Notes |
|-----------|-------|-------|
| A. Spec alignment | 25 | Data science overview, Python basics, Jupyter, data types, NumPy/Pandas/cuDF/Numba, practicals all covered. |
| B. Execution | 25 | All 9 example notebooks run successfully. |
| C. Inputs & outputs | 25 | All executed. 6 “empty” in 07 are comment-only cells (intentional); 1 optional in 03 (Colab setup). |
| D. Exercise + solution | 25 | `exercise_01` + `solution_01`; solution full, runnable; typo/docs fixed. |
| **Unit 1 total** | **100** | |

---

### Unit 2: Data Cleaning and Preparation

| Criterion | Score | Notes |
|-----------|-------|-------|
| A. Spec alignment | 25 | Import/export, cleaning, missing data, transformation, EDA, cuDF, unstructured (text/images) all covered. |
| B. Execution | 25 | All 8 example notebooks run successfully. |
| C. Inputs & outputs | 25 | All notebooks re-run in-place; 0 empty outputs. |
| D. Exercise + solution | 25 | `exercise_01` + `solution_01`; both present, complete, runnable. |
| **Unit 2 total** | **100** | |

---

### Unit 3: Data Visualization

| Criterion | Score | Notes |
|-----------|-------|-------|
| A. Spec alignment | 25 | Matplotlib, Seaborn, Plotly, chart types, customization, best practices, advanced viz covered. |
| B. Execution | 25 | All 8 example notebooks run successfully. |
| C. Inputs & outputs | 25 | All re-run in-place; any remaining empty are Plotly/display-only (intentional). |
| D. Exercise + solution | 25 | `exercise_01` + `solution_01`; both present, complete, runnable. |
| **Unit 3 total** | **100** | |

---

### Unit 4: Introduction to Machine Learning

| Criterion | Score | Notes |
|-----------|-------|-------|
| A. Spec alignment | 25 | ML concepts, Sklearn, regression, classification, evaluation, tuning, K-means, real-world, CPU/GPU covered. |
| B. Execution | 25 | All 12 example notebooks run successfully. |
| C. Inputs & outputs | 25 | All re-run in-place; remaining empty are optional GPU or display-only (intentional). |
| D. Exercise + solution | 25 | `exercise_01` + `solution_01`; both present, complete, runnable. |
| **Unit 4 total** | **100** | |

---

### Unit 5: Extending the Scope of Data Science

| Criterion | Score | Notes |
|-----------|-------|-------|
| A. Spec alignment | 25 | Big Data theory, Dask, PySpark, RAPIDS, deployment (Flask/FastAPI), monitoring, pipelines covered. |
| B. Execution | 25 | All 10 example notebooks run successfully. |
| C. Inputs & outputs | 25 | All re-run in-place; remaining empty are optional Dask/RAPIDS/GPU (intentional). |
| D. Exercise + solution | 25 | `exercise_01` + `solution_01`; both present, complete, runnable. |
| **Unit 5 total** | **100** | |

---

## 3. Scorecard summary

| Unit | A. Spec | B. Execution | C. I/O | D. Ex+Sol | **Total** |
|------|---------|--------------|--------|-----------|-----------|
| 1 – Introduction | 25 | 25 | 25 | 25 | **100** |
| 2 – Cleaning | 25 | 25 | 25 | 25 | **100** |
| 3 – Visualization | 25 | 25 | 25 | 25 | **100** |
| 4 – ML | 25 | 25 | 25 | 25 | **100** |
| 5 – Scaling | 25 | 25 | 25 | 25 | **100** |
| **Course 05** | — | — | — | — | **100** |

**Course 05 overall:** **100 / 100.**

**Post re-run:** All example notebooks (Units 1–5) were executed with `jupyter nbconvert --execute --inplace` and saved. Unit 2 has 0 empty outputs; any remaining empty in other units are intentional (comment-only, Plotly/display-only, or optional GPU/Dask/RAPIDS cells).

---

## 4. What the score means

- **100** = Full alignment with `DETAILED_UNIT_DESCRIPTIONS`, all notebooks run and outputs saved, exercises and solutions in place. Remaining empty outputs are documented as intentional (comment-only, display-only, or optional).

---

## 5. Where the evidence lives

- **Unit 1:** `unit1-introduction/UNIT1_DEEP_DIVE.md`
- **Units 2–5:** `DEEP_DIVE_UNITS_2_5.md`
- **Spec:** `../DETAILED_UNIT_DESCRIPTIONS.md` (Course 05 sections)
