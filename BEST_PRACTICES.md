# Best Practices Guide | دليل أفضل الممارسات
## Coding Standards, Notebook Organization, and Git Workflow

**Last Updated:** January 2025

---

## 📋 Table of Contents | جدول المحتويات

1. [Coding Standards](#coding-standards)
2. [Notebook Organization](#notebook-organization)
3. [Git Workflow](#git-workflow)
4. [Code Review Guidelines](#code-review-guidelines)
5. [Documentation Standards](#documentation-standards)

---

## 💻 Coding Standards | معايير البرمجة

### Python Style Guide

**Follow PEP 8:**
- Use 4 spaces for indentation (not tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Follow naming conventions:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants

**Example:**
```python
# ✅ Good
def calculate_accuracy(y_true, y_pred):
    """Calculate classification accuracy."""
    correct = sum(y_true == y_pred)
    total = len(y_true)
    return correct / total

# ❌ Bad
def calc(y1, y2):
    c = sum(y1 == y2)
    t = len(y1)
    return c/t
```

### Code Organization

**Structure your code:**
1. **Imports** (standard library, third-party, local)
2. **Constants**
3. **Functions/Classes**
4. **Main execution**

**Example:**
```python
# 1. Standard library imports
import os
import sys
from pathlib import Path

# 2. Third-party imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# 3. Local imports
from utils import load_data, preprocess_data

# 4. Constants
DATA_PATH = "data/sample_data.csv"
TEST_SIZE = 0.2
RANDOM_STATE = 42

# 5. Functions
def train_model(X, y):
    """Train machine learning model."""
    # Implementation
    pass

# 6. Main execution
if __name__ == "__main__":
    # Main code
    pass
```

### Comments and Documentation

**Write clear comments:**
- Explain **why**, not **what**
- Use docstrings for functions/classes
- Keep comments up-to-date

**Example:**
```python
def normalize_features(X, method='standard'):
    """
    Normalize feature matrix.
    
    Parameters:
    -----------
    X : array-like
        Feature matrix to normalize
    method : str, default='standard'
        Normalization method: 'standard' or 'minmax'
    
    Returns:
    --------
    X_normalized : array-like
        Normalized feature matrix
    """
    if method == 'standard':
        # Standardize: mean=0, std=1
        # This helps with gradient descent convergence
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        return (X - mean) / std
    elif method == 'minmax':
        # Scale to [0, 1] range
        # Useful for neural networks
        min_val = np.min(X, axis=0)
        max_val = np.max(X, axis=0)
        return (X - min_val) / (max_val - min_val)
```

---

## 📓 Notebook Organization | تنظيم الدفاتر

### Notebook Structure

**Standard notebook structure:**

1. **Header Cell** (Markdown)
   - Title
   - Learning objectives
   - Prerequisites
   - Date/Author

2. **Setup Cell** (Code)
   - Imports
   - Configuration
   - Helper functions

3. **Content Cells** (Mixed)
   - Theory (Markdown)
   - Examples (Code)
   - Visualizations (Code + Output)

4. **Summary Cell** (Markdown)
   - Key takeaways
   - Next steps

**Example structure:**
```markdown
# Title | العنوان

## Learning Objectives | أهداف التعلم
- Objective 1
- Objective 2

## Prerequisites | المتطلبات
- Prerequisite 1
- Prerequisite 2

---

## Step 1: Import Libraries
[Code cell with imports]

## Step 2: Load Data
[Code cell with data loading]

## Step 3: Analysis
[Code cells with analysis]

---

## Summary | الملخص
- Key point 1
- Key point 2
```

### Cell Best Practices

**Code Cells:**
- Keep cells focused (one concept per cell)
- Don't make cells too long (max 50-100 lines)
- Clear outputs before committing
- Use meaningful variable names

**Markdown Cells:**
- Use headers for structure
- Include explanations
- Add code examples in markdown
- Use bilingual format (English/Arabic)

**Output Cells:**
- Clear outputs before committing (optional)
- Keep important visualizations
- Remove error outputs

### Notebook Naming

**Use descriptive names:**
- ✅ `01_data_loading_exploration.ipynb`
- ✅ `02_linear_regression.ipynb`
- ✅ `03_model_evaluation.ipynb`
- ❌ `notebook1.ipynb`
- ❌ `test.ipynb`
- ❌ `final.ipynb`

---

## 🔄 Git Workflow | سير عمل Git

### Commit Messages

**Use conventional commits format:**

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Test additions/changes
- `chore`: Maintenance tasks

**Examples:**
```bash
# Good commit messages
git commit -m "feat(course05): add Numba JIT compilation notebook"
git commit -m "fix(course04): correct linear regression formula"
git commit -m "docs: update student guide with troubleshooting"
git commit -m "refactor(course08): optimize CNN training code"

# Bad commit messages
git commit -m "update"
git commit -m "fix bug"
git commit -m "changes"
```

### Branch Strategy

**For development:**
- `main`: Production-ready code
- `develop`: Development branch
- `feature/name`: Feature branches
- `fix/name`: Bug fix branches

**Example workflow:**
```bash
# Create feature branch
git checkout -b feature/add-new-notebook

# Make changes
# ... edit files ...

# Commit changes
git add .
git commit -m "feat: add new notebook for clustering"

# Push branch
git push origin feature/add-new-notebook

# Create pull request (on GitHub)
# After review, merge to develop/main
```

### File Organization

**What to commit:**
- ✅ Source code (`.py`, `.ipynb`)
- ✅ Documentation (`.md`)
- ✅ Configuration files (`.json`, `.yaml`)
- ✅ Requirements files (`requirements.txt`)

**What NOT to commit:**
- ❌ Large data files (use `.gitignore`)
- ❌ Model files (`.pkl`, `.h5`, `.pt`)
- ❌ Output files (`.png`, `.html` from notebooks)
- ❌ Environment files (`.env`, `venv/`)
- ❌ IDE files (`.vscode/`, `.idea/`)

**Example `.gitignore`:**
```
# Python
__pycache__/
*.py[cod]
*.so
*.egg
venv/
env/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Data
*.csv
*.json
*.xlsx
data/

# Models
*.pkl
*.h5
*.pt
*.pth
models/

# Outputs
*.png
*.jpg
*.html
outputs/

# IDE
.vscode/
.idea/
*.swp
```

---

## 👥 Code Review Guidelines | إرشادات مراجعة الكود

### Before Submitting

**Checklist:**
- [ ] Code follows style guide (PEP 8)
- [ ] Functions have docstrings
- [ ] Code is commented where needed
- [ ] No hardcoded values (use constants)
- [ ] Error handling is implemented
- [ ] Tests pass (if applicable)
- [ ] Documentation is updated

### Review Process

**What to review:**
1. **Functionality**: Does it work correctly?
2. **Style**: Does it follow conventions?
3. **Documentation**: Is it well-documented?
4. **Performance**: Is it efficient?
5. **Security**: Are there security issues?

**Review comments:**
- Be constructive and respectful
- Explain why changes are needed
- Suggest alternatives
- Acknowledge good practices

---

## 📚 Documentation Standards | معايير التوثيق

### README Files

**Every course should have:**
- Course overview
- Prerequisites
- Learning objectives
- Course structure
- Setup instructions
- Quick start guide

**Template:**
```markdown
# Course Name | اسم الدورة

## Course Overview | نظرة عامة على الدورة
[Description]

## Prerequisites | المتطلبات الأساسية
- Prerequisite 1
- Prerequisite 2

## Learning Objectives | أهداف التعلم
- Objective 1
- Objective 2

## Course Structure | هيكل الدورة
[Structure]

## Setup | الإعداد
[Setup instructions]

## Quick Start | البدء السريع
[Quick start guide]
```

### Code Documentation

**Functions:**
- Docstring with description
- Parameters section
- Returns section
- Examples (if helpful)

**Classes:**
- Class docstring
- Method docstrings
- Attribute descriptions

**Example:**
```python
class LinearRegression:
    """
    Simple linear regression model.
    
    Fits a linear model to minimize residual sum of squares.
    
    Attributes:
    -----------
    coef_ : array
        Model coefficients
    intercept_ : float
        Model intercept
    """
    
    def fit(self, X, y):
        """
        Fit linear regression model.
        
        Parameters:
        -----------
        X : array-like, shape (n_samples, n_features)
            Training data
        y : array-like, shape (n_samples,)
            Target values
        
        Returns:
        --------
        self : object
            Returns self
        """
        # Implementation
        return self
```

---

## ✅ Checklist | قائمة التحقق

### Before Committing Code:

- [ ] Code follows PEP 8 style guide
- [ ] Functions have docstrings
- [ ] Code is commented appropriately
- [ ] Variable names are descriptive
- [ ] No hardcoded values
- [ ] Error handling is implemented
- [ ] Tests pass (if applicable)

### Before Submitting Notebook:

- [ ] Header with title and objectives
- [ ] Clear cell structure
- [ ] Markdown explanations
- [ ] Code is well-commented
- [ ] Outputs are meaningful
- [ ] Summary section included

### Before Creating Pull Request:

- [ ] Code review checklist completed
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] Branch is up-to-date with main
- [ ] No merge conflicts
- [ ] Tests pass

---

## 🔗 Additional Resources | موارد إضافية

### Style Guides:
- **PEP 8**: https://pep8.org/
- **Google Python Style Guide**: https://google.github.io/styleguide/pyguide.html
- **NumPy Style Guide**: https://numpydoc.readthedocs.io/

### Tools:
- **Black**: Code formatter
- **Flake8**: Linter
- **Pylint**: Code analyzer
- **MyPy**: Type checker

### Git Resources:
- **Git Documentation**: https://git-scm.com/doc
- **Conventional Commits**: https://www.conventionalcommits.org/
- **GitHub Flow**: https://guides.github.com/introduction/flow/

---

**Last Updated:** January 2025  
**Status:** Complete Best Practices Guide
