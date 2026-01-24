# Notebook Execution Triage

**Source:** [failure_analysis.json](failure_analysis.json), execution reports.  
**Purpose:** Categorize failures (env/deps vs code bugs), mark optional/advanced, guide fixes.

---

## 1. Summary

| Category | Count | Verdict | Action |
|----------|-------|---------|--------|
| **missing_packages** | 36 | Env/deps | Install `requirements.txt`; use correct venv. Run `pip check` + quick-validate (SETUP_GUIDE). |
| **missing_imports** | 36 | Mixed | Many are TODO cells or docstring-only; some need `sklearn`/`torch`/`tensorflow`. Treat as env first. |
| **syntax_errors** | 15 | Code bugs | Fix notebooks (see §3). |
| **api_errors** | 3 | Env / edge | TensorFlow Serving, SOLUTIONS_ALL metadata; mark optional or fix invalid notebooks. |
| **timeout** | 1 | Env | MLflow localhost; optional. |
| **other** | 2 | Optional | RDF serialize, RNN TODO; advanced use. |

**Overall:** Majority of failures are **env/deps**. Ensure `pip install -r requirements.txt`, `pip check`, and core-libs check before running notebooks. Remaining **syntax** and **optional** items are triaged below.

---

## 2. Env/Dependencies (no code change)

- **Missing packages:** `sklearn`, `scikit-learn`, `tensorflow`, `torch`, `transformers`, `gym`. All in `requirements.txt`. Use project venv and `pip install -r requirements.txt`.
- **Timeout (MLflow):** `Course 11/unit2-versioning-serving/examples/03_model_versioning.ipynb` — expects MLflow server. **Optional/advanced.**
- **API (TensorFlow Serving):** `Course 08/unit5-deployment/examples/02_tensorflow_serving.ipynb` — expects TF Serving. **Optional/advanced.**

---

## 3. Syntax / Code Bugs (fix or mark optional)

| Notebook | Issue | Action |
|----------|-------|--------|
| Course 03 `unit1-linear-algebra` 06_transformation_matrices_orthogonal_basis | Syntax | Fix or mark optional |
| Course 03 `unit2-calculus` 05_function_approximation_ml | Syntax | Fix or mark optional |
| Course 03 `unit5-probability` 06_maximum_likelihood_estimation | Syntax | Fix or mark optional |
| Course 04 `unit1-data-processing` 01_data_loading_exploration | Syntax | Fix or mark optional |
| Course 04 `unit1-data-processing` 04_linear_regression | Syntax | Fix or mark optional |

*Full list in `failure_analysis.json` → `sample_failures.syntax_errors`.*

---

## 4. Optional / Advanced

- **TODO exercises:** Course 03 `modules` exercises (exercise_01, exercise_02, utils.ipynb), Course 08 RNN exercise — incomplete by design; **optional**.
- **RDF/SPARQL:** `Course 01/unit2-search-algorithms` 07_rdf_sparql — may need `rdflib`; **advanced**.
- **SOLUTIONS_ALL** invalid metadata: Exclude from student path or fix notebook structure.

---

## 5. Quick Validate

Before running notebooks:

```bash
pip install -r requirements.txt
pip check
python -c "import numpy, pandas, sklearn; print('✅ Core libs OK')"
```

See [SETUP_GUIDE.md](../SETUP_GUIDE.md) for full setup and optional notebook check.

---

**Last updated:** With deep-dive execution.
