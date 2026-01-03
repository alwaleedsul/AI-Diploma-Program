# Verified Real Datasets for Course 04 Notebooks
## Accurate Dataset Mapping - All URLs and Sources Verified

This document lists ONLY real, publicly available datasets that have been verified to work. All code outputs match the actual data structure.

---

## ✅ Verified Dataset Sources

### 1. **sklearn Built-in Datasets** (100% Reliable)
- **fetch_california_housing()**: Real California housing data from 1990 census
- **load_breast_cancer()**: Real Wisconsin breast cancer dataset
- **load_iris()**: Real iris flower dataset
- **load_diabetes()**: Real diabetes dataset
- **load_wine()**: Real wine dataset
- **Advantages**: Always available, no download needed, well-documented

### 2. **GitHub Raw URLs** (Verify Before Use)
- Must test URLs before including in notebooks
- Common sources:
  - `https://raw.githubusercontent.com/datasciencedojo/datasets/master/` (verify each file exists)
  - Individual GitHub repositories (verify URLs work)

### 3. **Kaggle Datasets** (Require Manual Download)
- Credit Card Fraud Detection: `https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud`
- Titanic: `https://www.kaggle.com/c/titanic`
- US Accidents: `https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents`
- **Note**: Require Kaggle account and API key or manual download

### 4. **UCI ML Repository** (Reliable but Require Download)
- Well-documented, academic datasets
- URLs: `https://archive.ics.uci.edu/ml/datasets.php`
- **Note**: Require manual download and verification

---

## 📋 Accurate Dataset Mapping by Notebook

### Unit 1: Data Processing

#### `01_data_loading_exploration.ipynb`
- **Dataset**: sklearn `fetch_california_housing()` OR verified GitHub crime dataset
- **Actual Columns**: 
  - California Housing: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, MedHouseVal
  - Crime Dataset: Verify actual columns from source
- **Code Output**: Must match actual columns
- **Description**: Must describe actual data structure

#### `02_data_cleaning.ipynb`
- **Dataset**: sklearn datasets with missing values OR verified Titanic dataset
- **Actual Columns**: Verify from source
- **Code Output**: Must show actual missing value patterns
- **Description**: Must match actual data quality issues

#### `03_data_preprocessing.ipynb`
- **Dataset**: sklearn `load_breast_cancer()` OR verified dataset with categorical features
- **Actual Columns**: Verify from source
- **Code Output**: Must match actual preprocessing needs
- **Description**: Must describe actual categorical/numerical mix

#### `04_linear_regression.ipynb`
- **Dataset**: sklearn `fetch_california_housing()` (use as-is, don't reframe)
- **Actual Columns**: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
- **Target**: MedHouseVal (median house value)
- **Code Output**: Must use actual column names
- **Description**: Must describe actual California housing data

#### `05_polynomial_regression.ipynb`
- **Dataset**: sklearn `fetch_california_housing()` OR time-series data
- **Actual Columns**: Verify from source
- **Code Output**: Must match actual data
- **Description**: Must describe actual non-linear patterns

---

## ⚠️ Critical Rules

1. **NEVER create synthetic data** - Use only real datasets
2. **NEVER reframe datasets without clear disclosure** - If reframing, state clearly
3. **VERIFY all URLs** - Test before including
4. **MATCH descriptions to actual data** - Code outputs must match descriptions
5. **USE sklearn datasets when possible** - Most reliable
6. **PROVIDE fallback options** - If URL fails, provide clear alternatives
7. **BE TRANSPARENT** - Clearly state what data is being used and why

---

## 🔍 Verification Checklist

Before including any dataset in a notebook:

- [ ] Dataset exists and is publicly available
- [ ] URL works (if using URL)
- [ ] Actual columns match descriptions
- [ ] Code outputs match written descriptions
- [ ] Data structure is accurately described
- [ ] Fallback options are provided
- [ ] Source is clearly cited
- [ ] Any reframing is clearly disclosed

---

## 📝 Example: Accurate Dataset Description

**GOOD (Accurate)**:
```python
# Load California Housing dataset from sklearn
# This is REAL data from 1990 California census
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['target'] = housing.target

# Actual columns: MedInc, HouseAge, AveRooms, AveBedrms, Population, 
#                 AveOccup, Latitude, Longitude
# Target: Median house value (in hundreds of thousands of dollars)
```

**BAD (Inaccurate)**:
```python
# Load financial transaction data
# (But actually using California Housing and reframing it)
# This creates confusion - students will notice the mismatch!
```

---

## 🎯 Best Practices

1. **Use sklearn datasets** - Most reliable, always available
2. **Be transparent** - If using California Housing, say it's California Housing
3. **Provide context** - Explain why this dataset is relevant to GDI work
4. **Match reality** - Code outputs must match actual data
5. **Test everything** - Verify URLs, columns, outputs before finalizing


