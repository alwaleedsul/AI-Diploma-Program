# Quiz 03: Classification Techniques - ANSWER KEY
# اختبار 03: تقنيات التصنيف - مفتاح الإجابات
# ⚠️ INSTRUCTOR ONLY - DO NOT SHARE WITH STUDENTS ⚠️

---

## Part 1: Classification Algorithms (35 points)

### Question 1 (5 points)
**Answer: A**
- Regression predicts continuous values, classification predicts categories

### Question 2 (5 points)
**Answer: B**
- Logistic Regression uses sigmoid function

### Question 3 (5 points)
**Answer: B**
- Decision Trees are easy to interpret and visualize

### Question 4 (5 points)
**Answer: A**
- SVM finds the best decision boundary that maximizes the margin

### Question 5 (5 points)
**Answer: B**
- Random Forest is an ensemble method that combines multiple decision trees

### Question 6 (5 points)
**Answer: B**
- Random Forest reduces overfitting by combining multiple trees (ensemble method)

### Question 7 (5 points)
**Answer: B**
- KNN finds the K nearest training examples and predicts the majority class

---

## Part 2: Evaluation Metrics (20 points)

### Question 5 (5 points)
**Answer: A**
- Accuracy measures the proportion of correctly classified instances

### Question 6 (5 points)
**Answer: B**
- Precision is the proportion of positive predictions that are correct

### Question 7 (5 points)
**Answer: C**
- Recall is the proportion of actual positives that are correctly identified

### Question 8 (5 points)
**Answer: D**
- F1-score is the harmonic mean of precision and recall

---

## Part 3: Confusion Matrix and ROC (20 points)

### Question 9 (5 points)
**Answer: B**
- True Positive (TP) represents correctly predicted positive cases

### Question 10 (5 points)
**Answer: A**
- False Positive (FP) is when model predicted Class 1, but actual is Class 0 (false alarm)

### Question 11 (5 points)
**Answer: B**
- False Negative (FN) is when model predicted Class 0, but actual is Class 1 (missed detection)

### Question 12 (5 points)
**Answer: B**
- AUC measures the model's ability to distinguish between classes

---

## Part 4: Advanced Topics (20 points)

### Question 13 (5 points)
**Answer: C**
- Metrics are calculated after training, on test data

### Question 14 (5 points)
**Answer: B**
- `.predict()` returns classes (0 or 1), `.predict_proba()` returns probabilities (0-1)

### Question 15 (5 points)
**Answer: B**
- Class imbalance occurs when one class has significantly more samples than another

### Question 16 (5 points)
**Answer: A**
- Use `class_weight='balanced'` parameter in logistic regression to handle class imbalance

---

## Grading Rubric | معايير التقييم

- **90-100% (68-75 points)**: Excellent understanding
- **80-89% (60-67 points)**: Good understanding
- **70-79% (53-59 points)**: Satisfactory understanding
- **60-69% (45-52 points)**: Needs improvement
- **Below 60% (<45 points)**: Requires review of concepts

---

## Common Student Mistakes | الأخطاء الشائعة للطلاب

1. **Confusing precision and recall**: Students often mix up which one measures what
2. **TP/FP/TN/FN confusion**: Students struggle with the True/False and Positive/Negative combinations
3. **When metrics are calculated**: Some students think metrics are calculated before training
4. **`.predict()` vs `.predict_proba()`**: Students confuse which returns what
5. **Random Forest vs Decision Tree**: Students may not understand that Random Forest is an ensemble of multiple trees
6. **KNN algorithm**: Students may confuse how KNN makes predictions (distance-based vs tree-based)
7. **Class imbalance**: Students may not recognize when class imbalance is a problem or how to handle it

---

**⚠️ KEEP THIS FILE SECURE - DO NOT SHARE WITH STUDENTS ⚠️**

