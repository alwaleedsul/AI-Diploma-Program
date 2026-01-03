# Notebook Testing Guide
## دليل اختبار الدفاتر

**Purpose**: Guide for testing notebooks after GDI dataset updates

---

## ✅ Testing Checklist

### Before Testing:
- [ ] All datasets are in `datasets/raw/` folder
- [ ] Notebook file paths are correct
- [ ] Column names match the actual dataset

### Testing Steps:

1. **Environment Setup**
   ```bash
   # Ensure required packages are installed
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

2. **Open Notebook**
   ```bash
   jupyter notebook 01_data_loading_exploration.ipynb
   # OR
   jupyter lab 01_data_loading_exploration.ipynb
   ```

3. **Run All Cells**
   - Use: Kernel → Restart & Run All
   - Check for errors in each cell

4. **Verify Outputs**
   - [ ] Data loads successfully
   - [ ] Column names match descriptions
   - [ ] Statistics make sense
   - [ ] No missing values (or expected amount)
   - [ ] Visualizations display correctly

---

## 📋 Specific Test for 01_data_loading_exploration.ipynb

### Expected Outputs:

1. **Data Loading (Cell 5)**
   - Should show: "✅ Real-world US Crime Statistics dataset loaded!"
   - Should show: 50 US states, 5 features
   - Should list: State, Murder, Assault, UrbanPop, Rape

2. **Data Overview (Cell 8)**
   - Should show: 50 rows, 5 columns
   - Should list all 5 column names

3. **Data Shape (Cell 12)**
   - Should show: Rows: 50 (number of US states)
   - Should show: Columns: 5

4. **Statistics (Cell 13)**
   - Should show statistics for: Murder, Assault, UrbanPop, Rape
   - State column should NOT appear (it's categorical)

5. **Data Types (Cell 14)**
   - Murder: float64
   - Assault: int64
   - UrbanPop: int64
   - Rape: float64
   - State: object

6. **Missing Values (Cell 15)**
   - Should show: ✅ No missing values found!

7. **Categorical Analysis (Cell 20)**
   - Should show: 50 states
   - Each state appears once

8. **Column Statistics (Cell 22)**
   - Should analyze Murder column
   - Should show top 3 and bottom 3 states

---

## ⚠️ Common Issues to Check:

1. **File Path Errors**
   - Error: `FileNotFoundError: crime_statistics.csv`
   - Fix: Verify path is `../../datasets/raw/crime_statistics.csv` from notebook location

2. **Column Name Errors**
   - Error: `KeyError: 'location'` or `KeyError: 'Year'`
   - Fix: Update code to use: State, Murder, Assault, UrbanPop, Rape

3. **Data Type Errors**
   - Error: Can't perform numeric operations on State column
   - Fix: Ensure State column is excluded from numeric operations

4. **Missing Dataset**
   - Error: File not found
   - Fix: Verify dataset is in `Course 04/datasets/raw/crime_statistics.csv`

---

## ✅ Success Criteria:

- [ ] All cells execute without errors
- [ ] All outputs match descriptions in markdown cells
- [ ] Dataset loads correctly (50 rows, 5 columns)
- [ ] Column names are correct
- [ ] Statistics are computed successfully
- [ ] No unexpected errors or warnings
- [ ] All visualizations (if any) display correctly

---

**Note**: If pandas is not installed in your environment, you'll need to install it first:
```bash
pip install pandas numpy matplotlib seaborn
```

