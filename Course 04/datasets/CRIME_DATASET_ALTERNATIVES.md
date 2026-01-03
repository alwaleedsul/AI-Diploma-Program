# Crime Statistics Dataset - Alternative Sources
## مصادر بديلة لمجموعة بيانات إحصائيات الجريمة

**Issue**: Original URL `https://raw.githubusercontent.com/datasciencedojo/datasets/master/crime.csv` returns 404.

---

## ✅ Verified Working Alternatives

### Option 1: USArrests Dataset (RECOMMENDED)

**URL**: `https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv`

**Status**: ✅ **VERIFIED WORKING**

**Dataset Details**:
- **Columns**: State, Murder, Assault, UrbanPop, Rape
- **Rows**: 50 (US states)
- **Source**: Classic R dataset (reliable, well-documented)
- **Use Case**: Crime statistics analysis, state-level crime data

**Pros**:
- ✅ URL is accessible and stable
- ✅ Well-known dataset in statistics/ML community
- ✅ Perfect for educational purposes
- ✅ Real data (US state crime statistics)
- ✅ Relevant to Internal Intelligence, Internal Security

**Cons**:
- ⚠️ Different structure than original (no Year, Population columns)
- ⚠️ State-level data (not time series)

**Usage**:
```python
import pandas as pd
url = 'https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv'
df = pd.read_csv(url)
```

---

### Option 2: Notebook's Built-in Fallback

**Current Implementation**: The notebook (`01_data_loading_exploration.ipynb`) already has error handling that falls back to sklearn's `fetch_california_housing` dataset if the crime URL fails.

**Status**: ✅ **ALREADY IMPLEMENTED**

**Pros**:
- ✅ No changes needed
- ✅ Notebook works even if URL fails
- ✅ Students can complete the lesson

**Cons**:
- ⚠️ Uses housing data instead of crime data (context mismatch)
- ⚠️ Not ideal for GDI alignment

---

### Option 3: data.gov Crime Statistics

**Source**: data.gov  
**URL**: Need to search data.gov for specific dataset

**Search Terms**:
- "crime statistics CSV"
- "FBI uniform crime reporting"
- "US crime data"

**Status**: ⚠️ **NEEDS RESEARCH**

**Pros**:
- ✅ Official government data
- ✅ Comprehensive crime statistics
- ✅ Better alignment with GDI responsibilities

**Cons**:
- ⚠️ May require manual download
- ⚠️ URL structure may change
- ⚠️ Need to verify specific dataset

**Action**: Research data.gov for specific CSV download URLs

---

### Option 4: Kaggle Crime Statistics

**Source**: Kaggle  
**Search**: "US crime statistics dataset" or "crime statistics CSV"

**Status**: ⚠️ **NEEDS RESEARCH**

**Pros**:
- ✅ Kaggle datasets are usually well-maintained
- ✅ Multiple options available

**Cons**:
- ⚠️ Requires Kaggle account for download
- ⚠️ Need to identify best dataset

---

### Option 5: Generate Synthetic Crime Data

**Approach**: Create realistic synthetic crime statistics data

**Structure**:
```python
# Example structure
Year, Population, Total, Violent, Property
2020, 331000000, 1000000, 200000, 800000
2021, 332000000, 980000, 195000, 785000
...
```

**Status**: ⚠️ **CAN BE IMPLEMENTED**

**Pros**:
- ✅ Full control over structure
- ✅ Aligns with notebook expectations
- ✅ No dependency on external URLs

**Cons**:
- ⚠️ Not "real" data (synthetic)
- ⚠️ Requires implementation

---

## 🎯 Recommended Solution

### **PRIMARY RECOMMENDATION**: Use USArrests Dataset

**Implementation**:
1. Update notebook to use USArrests URL as primary source
2. Update descriptions to reflect state-level crime data (instead of time series)
3. Update column references: `State, Murder, Assault, UrbanPop, Rape`
4. Keep error handling with fallback

**Code Change**:
```python
# Change from:
crime_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/crime.csv'

# To:
crime_url = 'https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv'
```

**Notebook Updates Needed**:
- Update markdown descriptions (state-level vs time series)
- Update column references in code
- Update visualizations to match new structure
- Keep GDI context (Internal Intelligence, Internal Security)

---

## 📝 Action Items

1. ✅ **Verify USArrests URL** - DONE (working)
2. ⚠️ **Update notebook** - Use USArrests as primary source
3. ⚠️ **Update download script** - Use USArrests URL
4. ⚠️ **Update documentation** - Reflect USArrests dataset
5. ⚠️ **Alternative**: Research data.gov for comprehensive crime statistics

---

## 🔗 Working URLs Summary

| Dataset | URL | Status | Verified Date |
|---------|-----|--------|---------------|
| **USArrests** | `https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv` | ✅ Working | Current Session |
| Original Crime | `https://raw.githubusercontent.com/datasciencedojo/datasets/master/crime.csv` | ❌ 404 | Current Session |

---

**Last Updated**: Current Session

