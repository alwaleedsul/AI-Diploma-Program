# Course 04 Datasets
## مجموعات بيانات الدورة 04

This directory contains all datasets used in Course 04 notebooks.

---

## 📁 Directory Structure

```
datasets/
├── raw/              # Original downloaded datasets
├── processed/        # Processed/cleaned datasets (if needed)
├── download_datasets.py      # Automated download script (direct URLs)
├── download_kaggle_datasets.py  # Automated Kaggle download script
├── DOWNLOAD_INSTRUCTIONS.md  # Manual download instructions
├── KAGGLE_DOWNLOAD_GUIDE.md  # Kaggle-specific download guide
├── CRIME_DATASET_ALTERNATIVES.md  # Crime dataset alternatives
└── README.md         # This file
```

---

## ✅ Available Datasets

### Direct Download (Auto-downloaded) ✅

1. **Crime Statistics** (`raw/crime_statistics.csv`)
   - Used in: Internal Intelligence, Internal Security
   - Status: ✅ Downloaded
   - URL: `https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv`

2. **Titanic Dataset** (`raw/titanic.csv`)
   - Used in: Evidence Gathering, Airport Security
   - Status: ✅ Downloaded
   - URL: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`

---

## 📥 Kaggle Datasets (Manual/Auto Download)

### 3. Credit Card Fraud Detection (`raw/creditcard_fraud.csv`)

**Kaggle URL**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
**Dataset ID**: `mlg-ulb/creditcardfraud`  
**Size**: ~145 MB  
**Used For**: Financial Investigations, Terrorism Financing, Counter-Espionage, Admin/Tech Crimes

**Download Methods**:
- **Manual**: Visit URL → Click "Download" → Extract → Move to `raw/`
- **Automated**: `python download_kaggle_datasets.py` (requires Kaggle API setup)

**Instructions**: See `KAGGLE_DOWNLOAD_GUIDE.md`

---

### 4. US-Accidents Dataset (`raw/us_accidents.csv`)

**Kaggle URL**: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents  
**Dataset ID**: `sobhanmoosavi/us-accidents`  
**Size**: ~300+ MB  
**Used For**: Traffic Management

**Download Methods**:
- **Manual**: Visit URL → Click "Download" → Extract → Move to `raw/`
- **Automated**: `python download_kaggle_datasets.py` (requires Kaggle API setup)

**Instructions**: See `KAGGLE_DOWNLOAD_GUIDE.md`

---

## 🔗 Quick Links - All Dataset URLs

| Dataset | URL | Status |
|---------|-----|--------|
| **Crime Statistics** | Direct: `https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv` | ✅ Auto-download |
| **Titanic** | Direct: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv` | ✅ Auto-download |
| **Credit Card Fraud** | Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud | ⚠️ Manual/Auto |
| **US-Accidents** | Kaggle: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents | ⚠️ Manual/Auto |

---

## 🚀 Quick Start

### 1. Download Direct Access Datasets

```bash
cd datasets
python download_datasets.py
```

This downloads datasets with direct URLs (Crime Statistics, Titanic).

### 2. Download Kaggle Datasets

**Option A: Manual Download (Recommended for first time)**
1. Create Kaggle account: https://www.kaggle.com/account/register
2. Visit dataset URLs above
3. Click "Download" button
4. Extract and move to `datasets/raw/`

**Option B: Automated Download (Requires API setup)**
```bash
# Install Kaggle API
pip install kaggle

# Set up credentials (download kaggle.json from Kaggle settings)
# Save to ~/.kaggle/kaggle.json

# Run download script
python download_kaggle_datasets.py
```

**Detailed Instructions**: See `KAGGLE_DOWNLOAD_GUIDE.md`

### 3. Download Other Datasets

For other datasets (GTD, UNSW-NB15, CICIDS2017, 911 Calls, Border Data), see `DOWNLOAD_INSTRUCTIONS.md`

---

## 📋 Dataset Mapping to Notebooks

| Notebook | Dataset | File Location | Download Method |
|----------|---------|---------------|-----------------|
| `01_data_loading_exploration` | Crime Statistics | `raw/crime_statistics.csv` | ✅ Auto (direct URL) |
| `02_data_cleaning` | Titanic | `raw/titanic.csv` | ✅ Auto (direct URL) |
| `03_data_preprocessing` | Credit Card Fraud | `raw/creditcard_fraud.csv` | ⚠️ Kaggle (manual/auto) |
| `04_linear_regression` | Credit Card Fraud | `raw/creditcard_fraud.csv` | ⚠️ Kaggle (manual/auto) |
| `05_polynomial_regression` | US-Accidents | `raw/us_accidents.csv` | ⚠️ Kaggle (manual/auto) |
| `01_ridge_lasso_regression` | Credit Card Fraud | `raw/creditcard_fraud.csv` | ⚠️ Kaggle (manual/auto) |
| `02_cross_validation` | Crime Statistics | `raw/crime_statistics.csv` | ✅ Auto (direct URL) |
| `01_logistic_regression` | Credit Card Fraud / GTD | `raw/creditcard_fraud.csv` | ⚠️ Kaggle (manual/auto) |
| `02_decision_trees` | Titanic | `raw/titanic.csv` | ✅ Auto (direct URL) |
| `03_svm` | UNSW-NB15 / CICIDS2017 | See DOWNLOAD_INSTRUCTIONS.md | ⚠️ Manual |
| `04_knn` | Credit Card Fraud | `raw/creditcard_fraud.csv` | ⚠️ Kaggle (manual/auto) |
| `01_kmeans_clustering` | Crime Statistics | `raw/crime_statistics.csv` | ✅ Auto (direct URL) |
| `02_hierarchical_clustering` | Crime Statistics | `raw/crime_statistics.csv` | ✅ Auto (direct URL) |
| `03_pca` | UNSW-NB15 / CICIDS2017 | See DOWNLOAD_INSTRUCTIONS.md | ⚠️ Manual |
| `01_grid_search` | BTS/CBP Border Data | See DOWNLOAD_INSTRUCTIONS.md | ⚠️ Manual |
| `02_boosting` | 911 Calls | See DOWNLOAD_INSTRUCTIONS.md | ⚠️ Manual |

---

## 📝 Notes

- **License**: All datasets are publicly available for educational use
- **Size**: Some datasets are large (US-Accidents ~300MB, CICIDS2017 ~7GB)
- **Kaggle Account**: Free account required for Kaggle datasets
- **Privacy**: All datasets are anonymized/public data suitable for educational use

---

## 🔗 Documentation

- **[DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md)** - Complete download instructions for all datasets
- **[KAGGLE_DOWNLOAD_GUIDE.md](KAGGLE_DOWNLOAD_GUIDE.md)** - Detailed Kaggle download guide with URLs
- **[CRIME_DATASET_ALTERNATIVES.md](CRIME_DATASET_ALTERNATIVES.md)** - Crime dataset alternatives documentation
- **[Dataset Research](../DOCS/DEEP_DATASET_RESEARCH_INTERNATIONAL.md)** - Full research documentation

---

**Last Updated**: Current Session
