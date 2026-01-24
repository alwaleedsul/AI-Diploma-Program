# Deep Dive: Course 05 Units 2–5

**Scope:** Unit 2 (Data Cleaning), Unit 3 (Visualization), Unit 4 (ML), Unit 5 (Scaling).  
**Reference:** `DETAILED_UNIT_DESCRIPTIONS.md` (Course 05) – **what we build the whole course from**.

**Execution:** All example notebooks in Units 2–5 were run via `jupyter nbconvert --execute`; **all run successfully**.

---

## Unit 2: Data Cleaning and Preparation

### Spec (theory + practical)

| Spec | Detail |
|------|--------|
| **Theory** | Import/export (CSV, Parquet, cuDF); cleaning (duplicates, inconsistency, normalization); missing data (identify, impute, remove); transformation & feature engineering (scaling, encoding, **unstructured** text/images); EDA (distributions, stats, outliers); GPU data processing |
| **Practical** | Import/export with cuDF; discover/fix duplication and inconsistency; handle missing values; transform (scaling, encoding); EDA (visualize, insights); cuDF optimization |

### Examples

| Example | Topic | Code cells | Executed | Empty outputs | Spec alignment |
|---------|--------|------------|----------|---------------|----------------|
| 01 | Data loading (CSV, JSON, etc.) | 8 | 8 | 0 | ✓ Import/export |
| 02 | Missing values, duplicates | 8 | 8 | 0 | ✓ Missing data, duplicates |
| 03 | Outliers, transformation | 9 | 9 | 0 | ✓ Cleaning, transformation |
| 04 | Feature transformation, scaling, encoding | 1 | 1 | 0 | ✓ Transformation |
| 05 | EDA visualizations | 1 | 1 | 0 | ✓ EDA |
| 06 | Statistical EDA | 5 | 5 | 0 | ✓ EDA, stats |
| 07 | cuDF import/export, GPU | 5 | 5 | 0 | ✓ cuDF, GPU |
| 08 | Feature extraction (text, images) | 2 | 2* | 2* | ✓ Unstructured feature extraction |

\*08: Stored notebook may show `execution_count: null` / empty outputs; **runs successfully** when executed.

### Verdict

- **Aligned** with Unit 2 spec.  
- Import/export, cleaning, missing data, transformation, EDA, cuDF, and **unstructured feature extraction** (text/images) are covered.  
- **Exercise** `exercise_01` + **solution** `solutions/solution_01.ipynb` present.

---

## Unit 3: Data Visualization

### Spec (theory + practical)

| Spec | Detail |
|------|--------|
| **Theory** | Matplotlib & Seaborn (static, statistical charts, customization); chart types (line, bar, histogram, scatter, heatmap, pair, box, violin); Plotly (interactive, dashboards); static vs interactive |
| **Practical** | Various chart types (Matplotlib, Seaborn); interactive viz and dashboards (Plotly); customization and annotations; visualization best practices |

### Examples

| Example | Topic | Code cells | Executed | Empty outputs | Spec alignment |
|---------|--------|------------|----------|---------------|----------------|
| 01 | Chart types (matplotlib, seaborn) | 7 | 6* | 1* | ✓ Chart types |
| 02 | Matplotlib basics | 8 | 8 | 0 | ✓ Matplotlib |
| 03 | Seaborn plots | 9 | 9 | 0 | ✓ Seaborn |
| 04 | Plotly interactive | 8 | 8 | 0 | ✓ Plotly |
| 05 | Interactive visualizations (Plotly) | 2 | 2 | 0 | ✓ Interactive, Plotly |
| 06 | Customizing, annotating | 8 | 7* | 1* | ✓ Customization |
| 07 | Visualization best practices | 2 | 2 | 0 | ✓ Best practices |
| 08 | Advanced visualization types | 5 | 5 | 0 | ✓ Advanced types |

\*01, 06: One cell each with unexecuted/empty in stored notebook; **notebooks run successfully** end-to-end.  
Plotly examples produce HTML (e.g. `11_interactive_scatter.html` … `15_3d_scatter.html`).

### Verdict

- **Aligned** with Unit 3 spec.  
- Matplotlib, Seaborn, Plotly, chart types, customization, best practices, and advanced viz are covered.  
- **Exercise** `exercise_01` + **solution** `solutions/solution_01.ipynb` present.

---

## Unit 4: Introduction to Machine Learning

### Spec (theory + practical)

| Spec | Detail |
|------|--------|
| **Theory** | ML concepts, workflow, applications; supervised vs unsupervised; Scikit-learn; building and evaluating models; hyperparameter optimization (Grid Search, Random Search, regularization, overfitting) |
| **Practical** | Pandas for ML; clean and prepare data (missing, encoding); implement models (Sklearn); supervised (e.g. logistic regression); unsupervised (e.g. K-means); train/test, evaluation; hyperparameter tuning (Grid Search, Random Search); real-world mix of supervised + unsupervised |

### Examples

| Example | Topic | Code cells | Executed | Empty outputs | Spec alignment |
|---------|--------|------------|----------|---------------|----------------|
| 01 | Pandas data manipulation | 1 | 1 | 0 | ✓ Data prep |
| 02 | Data preparation for ML | 1 | 1 | 0 | ✓ Clean, prepare |
| 03 | Implementing ML models (Sklearn) | 2 | 1* | 1* | ✓ Sklearn |
| 04 | Linear regression | 7 | 7 | 3 | ✓ Regression |
| 05 | Logistic regression | 3 | 3 | 0 | ✓ Supervised |
| 06 | Classification | 14 | 14 | 6 | ✓ Classification |
| 07 | Model evaluation | 10 | 10 | 3 | ✓ Evaluation |
| 08 | Hyperparameter tuning (Grid, Random Search) | 3 | 3 | 0 | ✓ Tuning |
| 09 | K-means | 3 | 3 | 0 | ✓ Unsupervised |
| 10 | Clustering (unsupervised) | 4 | 4 | 0 | ✓ Unsupervised |
| 11 | Real-world problem solving | 3 | 3 | 0 | ✓ Real-world mix |
| 12 | CPU vs GPU ML | 11 | 10* | 5* | ✓ Scaling (optional GPU) |

\*03, 12: Some cells unexecuted or empty in stored notebook; **notebooks run successfully**. Empty outputs often from optional GPU paths or display-only cells.

### Verdict

- **Aligned** with Unit 4 spec.  
- Data prep, Sklearn, regression, classification, evaluation, hyperparameter tuning, K-means/clustering, real-world mix, and optional CPU/GPU comparison are covered.  
- **Exercise** `exercise_01` + **solution** `solutions/solution_01.ipynb` present.

---

## Unit 5: Extending the Scope of Data Science (Scaling and Production)

### Spec (theory + practical)

| Spec | Detail |
|------|--------|
| **Theory** | Big Data (4 Vs, technologies, challenges); Dask, PySpark; distributed computing (MapReduce, fault tolerance); RAPIDS; deploying ML models (APIs); scaling and monitoring |
| **Practical** | Dask for distributed ops; PySpark for distributed processing; RAPIDS (e.g. cuDF) for GPU acceleration; deploy models via APIs (Flask/FastAPI); scaling and monitoring |

### Examples

| Example | Topic | Code cells | Executed | Empty outputs | Spec alignment |
|---------|--------|------------|----------|---------------|----------------|
| 01 | Big Data theory (4 Vs, MapReduce, fault tolerance) | 1 | 0* | 1* | ✓ Theory |
| 02 | Dask distributed | 11 | 11 | 4 | ✓ Dask |
| 03 | PySpark distributed | 9 | 9 | 0 | ✓ PySpark |
| 04 | RAPIDS workflows | 11 | 11 | 4 | ✓ RAPIDS |
| 05 | Production pipelines | 8 | 8 | 2 | ✓ Pipelines |
| 06 | Performance optimization | 10 | 10 | 4 | ✓ Optimization |
| 07 | Large datasets | 10 | 10 | 4 | ✓ Large data |
| 08 | Deployment (Flask, FastAPI) | 10 | 8* | 3* | ✓ APIs, deployment |
| 09 | Model monitoring | 4 | 4 | 0 | ✓ Monitoring |
| 10 | Data pipeline automation | 3 | 3 | 0 | ✓ Automation |

\*01: Mostly markdown + 1 MapReduce-style code cell; may show null/empty in stored notebook; **runs successfully**.  
\*08: Some cells (e.g. serve/mock API) may be unexecuted or empty; **notebook runs**.

### Verdict

- **Aligned** with Unit 5 spec.  
- Big Data theory, Dask, PySpark, RAPIDS, pipelines, optimization, large datasets, **deployment (Flask/FastAPI)**, monitoring, and automation are covered.  
- **Exercise** `exercise_01` + **solution** `solutions/solution_01.ipynb` present.

---

## Summary

| Unit | Examples | All execute? | Spec aligned? | Exercise + solution? |
|------|----------|--------------|---------------|----------------------|
| **2** Data Cleaning | 8 | ✓ | ✓ | ✓ |
| **3** Visualization | 8 | ✓ | ✓ | ✓ |
| **4** ML | 12 | ✓ | ✓ | ✓ |
| **5** Scaling | 10 | ✓ | ✓ | ✓ |

- **Inputs** (what each notebook teaches) and **outputs** (what runs) match the Unit 2–5 specs in `DETAILED_UNIT_DESCRIPTIONS.md`.  
- Some notebooks have `execution_count: null` or empty outputs **in the saved .ipynb** (optional GPU, Colab-only, or display-only cells). When run via `jupyter nbconvert --execute`, **all Unit 2–5 example notebooks run successfully**.  
- Units 2–5 are **aligned** with what we build the whole course from.
