# Real Online Datasets Mapping for GDI-Themed Notebooks
## Mapping of Publicly Available Datasets to Each Notebook

This document maps real, publicly available online datasets to each notebook, covering security/intelligence themes relevant to GDI work.

---

## Unit 1: Data Processing and Basic Regression

### `01_data_loading_exploration.ipynb`
- **Dataset**: US Crime Statistics
- **Source**: GitHub (datasciencedojo/datasets) or data.gov
- **URL**: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/crime.csv`
- **Alternative**: Any crime statistics dataset from data.gov, Kaggle
- **Theme**: Security/Crime Statistics - Intelligence Analysis
- **Features**: Year, Population, Crime counts (Total, Violent, Property)

### `02_data_cleaning.ipynb`
- **Dataset**: Titanic Dataset (has natural missing values)
- **Source**: GitHub or Kaggle
- **URL**: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`
- **Alternative**: Any dataset with missing values from Kaggle
- **Theme**: Investigation Evidence Reports (simulated through passenger data)
- **Features**: Passenger info with missing Age, Cabin, Embarked

### `03_data_preprocessing.ipynb`
- **Dataset**: Airport/Passenger Dataset or Credit Card Fraud (for categorical encoding)
- **Source**: Kaggle or UCI
- **URL Options**:
  - Credit Card Fraud: Kaggle (requires download)
  - Alternative: Use Titanic with categorical features
- **Theme**: Airport Security Screening (using passenger-like data)
- **Features**: Categorical (nationality, class) + Numerical

### `04_linear_regression.ipynb`
- **Dataset**: Financial Transaction Data or Credit Card Fraud
- **Source**: Kaggle, UCI
- **URL Options**:
  - Credit Card Fraud: `https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud` (requires Kaggle API)
  - Alternative: Use sklearn's `fetch_california_housing` but reframe as financial data
- **Theme**: Financial Investigation - Transaction Amount Prediction
- **Features**: Transaction characteristics → Amount

### `05_polynomial_regression.ipynb`
- **Dataset**: Traffic/Accident Data or Time-based data
- **Source**: Kaggle, data.gov
- **URL Options**:
  - US-Accidents: Kaggle (requires download)
  - Alternative: Use time-series data with non-linear patterns
- **Theme**: Airport Security - Wait Time Prediction
- **Features**: Time, passenger count → Wait time (non-linear)

---

## Unit 2: Advanced Regression

### `01_ridge_lasso_regression.ipynb`
- **Dataset**: Credit Card Fraud or Financial Crime Dataset
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud dataset (many features, perfect for Ridge/Lasso)
- **Theme**: Terrorism Financing Risk Assessment
- **Features**: Many financial indicators → Risk score

### `02_cross_validation.ipynb`
- **Dataset**: Crime Statistics or Intelligence Report Data
- **Source**: data.gov, GitHub
- **URL**: Crime statistics with temporal patterns
- **Theme**: Intelligence Report Volume Prediction
- **Features**: Time, threat indicators → Report volume

---

## Unit 3: Classification

### `01_logistic_regression.ipynb`
- **Dataset**: Credit Card Fraud Detection
- **Source**: Kaggle, UCI
- **URL**: `https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud`
- **Alternative**: Use sklearn's `load_breast_cancer` but reframe as threat detection
- **Theme**: Terrorist Threat Detection (Fraud = Threat, Normal = No Threat)
- **Features**: 30+ features → Binary classification (Fraud/No Fraud = Threat/No Threat)
- **Note**: Credit card fraud dataset has 30 features, perfect match!

### `02_decision_trees.ipynb`
- **Dataset**: Passenger/Travel Dataset or Credit Card Fraud
- **Source**: Titanic (for multi-class) or Fraud dataset
- **URL**: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`
- **Theme**: Airport Security - Passenger Risk Classification
- **Features**: Passenger attributes → Risk Level (multi-class)

### `03_svm.ipynb`
- **Dataset**: Credit Card Fraud or Cyber Security Dataset
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud (same as logistic regression)
- **Theme**: Counter-Espionage Threat Classification
- **Features**: Behavioral patterns → Threat/No Threat

### `04_knn.ipynb`
- **Dataset**: Credit Card Fraud or Financial Crime Dataset
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud dataset
- **Theme**: Financial Crime Classification
- **Features**: Transaction patterns → Crime Type

---

## Unit 4: Clustering and Dimensionality Reduction

### `01_kmeans_clustering.ipynb`
- **Dataset**: Crime Statistics or Cyber Security Dataset
- **Source**: data.gov, UCI
- **URL**: Crime statistics with multiple features
- **Theme**: Intelligence Pattern Clustering
- **Features**: Intelligence indicators → Pattern groups

### `02_hierarchical_clustering.ipynb`
- **Dataset**: Crime/Investigation Dataset
- **Source**: data.gov, GitHub
- **URL**: Crime statistics or investigation data
- **Theme**: Evidence Pattern Clustering
- **Features**: Evidence characteristics → Evidence groups

### `03_pca.ipynb`
- **Dataset**: Credit Card Fraud or Cyber Security Dataset (high-dimensional)
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud (30 features) or UNSW-NB15
- **Theme**: Intelligence Data Dimensionality Reduction
- **Features**: Many intelligence indicators → Reduced dimensions

---

## Unit 5: Model Selection

### `01_grid_search.ipynb`
- **Dataset**: Credit Card Fraud Detection
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud dataset
- **Theme**: Terrorist Threat Detection Model Optimization
- **Features**: Threat indicators → Threat/No Threat

### `02_boosting.ipynb`
- **Dataset**: Credit Card Fraud Detection
- **Source**: Kaggle, UCI
- **URL**: Credit Card Fraud dataset
- **Theme**: Financial Crime Risk Prediction
- **Features**: Financial features → Risk level

---

## Key Datasets to Use:

1. **Credit Card Fraud Detection** (Kaggle)
   - 30 features, binary classification
   - Perfect for: Logistic Regression, SVM, KNN, Grid Search, Boosting, PCA
   - URL: Requires Kaggle API or manual download
   - Alternative: Use sklearn datasets and reframe

2. **US Crime Statistics** (GitHub/data.gov)
   - Public government data
   - Perfect for: Data loading, exploration, clustering
   - URL: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/crime.csv`

3. **Titanic Dataset** (GitHub/Kaggle)
   - Has missing values, categorical features
   - Perfect for: Data cleaning, preprocessing, decision trees
   - URL: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`

4. **UNSW-NB15** (Cyber Security)
   - Network traffic data
   - Perfect for: Cyber threat detection, clustering
   - URL: Requires download from UNSW website

5. **CICIDS2017** (Cyber Security)
   - Intrusion detection dataset
   - Perfect for: Cyber threat classification
   - URL: Requires download from Canadian Institute for Cybersecurity

---

## Implementation Strategy:

1. **Primary**: Use datasets that can be loaded directly via URL (GitHub raw files)
2. **Secondary**: Provide instructions for downloading from Kaggle/data.gov
3. **Fallback**: Use sklearn datasets but reframe with GDI context
4. **Documentation**: Add clear instructions for students on how to obtain datasets

---

## Notes:

- All datasets should be publicly available and free
- No country-specific restrictions
- Focus on security/crime/fraud/cyber themes
- Provide multiple source options for each dataset
- Include download instructions for datasets requiring manual download


