# Unit 1 Deep Dive – Introduction to Data Science

**Scope:** Examples 01–09, `exercises/exercise_01`, `solutions/solution_01`.  
**Reference:** `DETAILED_UNIT_DESCRIPTIONS.md` (Course 05, Unit 1) – **what we build the whole course from**.

---

## 1. Spec alignment (Theory + Practical)

| Spec (theory + practical) | Coverage |
|---------------------------|----------|
| 1. Data science overview, lifecycle, applications | **01** ✓ |
| 2. Python basics: control flow, loops, functions, lambda, exceptions | **04** ✓ |
| 3. Jupyter setup, structure, best practices | **05** ✓ |
| 4. Data types, lists, dicts, DataFrames, indexing | **06**, **02** ✓ |
| 5. NumPy, Pandas, cuDF, Numba, basic viz | **02**, **03**, **08**, **09** ✓ |
| Practical: Python tasks, Jupyter, structures, NumPy/Pandas/cuDF, small projects | **01–09**, **exercise_01** ✓ |

**Verdict:** Unit 1 content matches `DETAILED_UNIT_DESCRIPTIONS.md` (Unit 1).

---

## 2. Inputs & outputs audit (all notebooks)

| Notebook | Code cells | Executed | Empty outputs | Key inputs | Key outputs | Aligns with spec? |
|----------|------------|----------|---------------|------------|-------------|-------------------|
| **01** data_science_intro | 7 | 7 | 0 | Lifecycle steps, matplotlib, pandas demo, FAQ | Prints, lifecycle diagram (PNG), summary, next steps | ✓ |
| **02** pandas_numpy_basics | 10 | 10 | 0 | NumPy arrays, DataFrames, groupby, viz | Array ops, describe, plots, “dead end” → Example 3 | ✓ |
| **03** cudf_introduction | 10 | 9* | 1* | Colab vs local, cuDF vs pandas, perf comparison | Setup msg or “Libraries imported”, CPU/GPU timings | ✓ |
| **04** python_basics_loops_conditions | 2 | 2 | 0 | if/elif/else, for/while, comprehensions, lambda, try/except | Printed examples for each construct | ✓ |
| **05** jupyter_notebooks_best_practices | 6 | 6 | 0 | Structure, seeds, dependencies, clear names | Best-practice examples, next → 06 | ✓ |
| **06** data_structures_lists_dictionaries | 7 | 7 | 0 | Lists, dicts, list↔dict, nested structures | Examples, next → 02, 07 | ✓ |
| **07** data_science_applications | 19 | 19 | 6 | Lifecycle in practice, small projects | Part 1 lifecycle print; 6 comment-only cells → no output | ✓ |
| **08** numba_jit_compilation | 4 | 4 | 0 | Numba JIT, speedup vs pure Python | Timing comparisons | ✓ |
| **09** advanced_numpy_operations | 5 | 5 | 0 | Advanced array ops, building on 02 | Numerical results, viz | ✓ |

\* **03:** First cell (Colab vs local setup) may have `execution_count: null` / empty output if not run in Colab; when run locally it prints “Running on local machine.” All other cells execute and produce output.  
\* **07:** The 6 “empty” outputs are from **comment-only** code cells (e.g. `# PART 1: ...`); no print → no output. Intentional.

**Execution:** All nine notebooks run successfully via `jupyter nbconvert --execute` (tested).

---

## 3. Alignment with “what we build the whole course from”

Course 05 is built from **`DETAILED_UNIT_DESCRIPTIONS.md`**. Unit 1’s theory and practicals there are:

- **Theory:** Data science overview, Python basics, Jupyter, data types/structures, NumPy/Pandas/cuDF/Numba.  
- **Practicals:** Python (arithmetic, loops, conditions), Jupyter, data structures, NumPy/Pandas/cuDF, small applications.

| Spec element | Notebook(s) | Input → Output |
|--------------|-------------|----------------|
| Data science lifecycle, applications | 01 | Lifecycle diagram, FAQ, summary → “Next: Example 2” |
| Python: control flow, loops, lambda, exceptions | 04 | if/for/while, comprehensions, lambda, try/except → printed demos |
| Jupyter structure, best practices | 05 | Structure, seeds, deps → examples |
| Data types, lists, dicts, DataFrames | 06, 02 | Lists, dicts, NumPy, pandas → examples, “dead end” |
| NumPy, Pandas, cuDF, Numba | 02, 03, 08, 09 | Arrays, DataFrames, GPU comparison, JIT → timings, viz |
| Small real-world projects | 07 | Lifecycle in practice → lifecycle summary, next units |

**Conclusion:** Unit 1 notebooks’ **inputs** (what they teach) and **outputs** (what runs and is shown) **align with** the Unit 1 spec in `DETAILED_UNIT_DESCRIPTIONS.md`, which is what we build the whole course from.

---

## 4. Example flow and cross-references

| Example | Title | Prerequisites | Leads to / Next |
|---------|--------|---------------|------------------|
| 01 | Introduction to Data Science | — | 02, 03 |
| 02 | Pandas & NumPy Basics | 01 | 03 |
| 03 | cuDF Introduction | 02 | Unit 2, 4, 5 |
| 04 | Python Basics | 01 | 02, 05 |
| 05 | Jupyter Best Practices | 04 | 06 |
| 06 | Data Structures | 04, 05 | 02, 07 |
| 07 | Data Science Applications | 01, 04, 06 | Unit 2–5 |
| 08 | Numba JIT | 02 | — |
| 09 | Advanced NumPy | 02 | — |

“Leads to 02” from 04/06 is backward in numbering but used as “use with” / “reinforces”; next-step flow is consistent.

---

## 5. Recommended order

- **Linear:** 01 → 02 → 03 → 04 → 05 → 06 → 07; then 08, 09.  
- **Alternative:** 01 → 04 → 05 → 06 → 02 → 03 (Python & Jupyter before Pandas/NumPy).

---

## 6. Exercise & solution

- **exercise_01:** Load, explore, stats, filter, viz, aggregate.  
- **solution_01:** Full reference implementation; instructor-only.  
- Fixes applied: imports typo, placeholder solutions replaced with working code, Teaching notes filled in.

---

## 7. Fixes applied in this deep dive

1. **07_data_science_applications:** Removed markdown typos (`")` and `")` .`) in “Data Science Lifecycle in Practice” section.  
2. **03:** Noted that first cell (Colab setup) can have null/empty output when not run in Colab; no code change.

---

## 8. Summary

- Unit 1 is **aligned** with `DETAILED_UNIT_DESCRIPTIONS.md` (theory + practical).  
- All **inputs** (code, concepts) and **outputs** (prints, figures, timings) in 01–09 are **consistent** with the spec and with **what we build the whole course from**.  
- All nine example notebooks **execute** successfully.  
- **solution_01** is complete and runnable for grading.
