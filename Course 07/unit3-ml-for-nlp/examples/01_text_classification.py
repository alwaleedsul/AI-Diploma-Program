"""
Unit 3 - Example 1: Text Classification with ML
الوحدة 3 - مثال 1: تصنيف النص باستخدام تعلم الآلة

This example demonstrates:
1. Feature extraction (TF-IDF)
2. Text classification
3. Model evaluation
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

print("=" * 60)
print("Example 1: Text Classification with ML")
print("مثال 1: تصنيف النص باستخدام تعلم الآلة")
print("=" * 60)

# Sample data: Movie reviews
# بيانات نموذجية: مراجعات الأفلام
documents = [
    "This movie is amazing and wonderful",
    "I love this film, it's fantastic",
    "Terrible movie, very boring",
    "Worst film I've ever seen",
    "Great acting and story",
    "Poor quality, not recommended",
    "Excellent cinematography",
    "Boring and slow paced"
]

labels = [
    "positive", "positive", "negative", "negative",
    "positive", "negative", "positive", "negative"
]

print("\nSample Documents:")
print("مستندات نموذجية:")
for i, (doc, label) in enumerate(zip(documents, labels), 1):
    print(f"  {i}. [{label}] {doc}")

# 1. Feature Extraction with TF-IDF
# استخراج الميزات باستخدام TF-IDF
print("\n" + "=" * 60)
print("1. Feature Extraction (TF-IDF)")
print("استخراج الميزات (TF-IDF)")
print("=" * 60)

vectorizer = TfidfVectorizer(max_features=10, stop_words='english')
X = vectorizer.fit_transform(documents)

print(f"\nFeature matrix shape: {X.shape}")
print(f"Features (words): {vectorizer.get_feature_names_out()}")

# 2. Train-Test Split
# تقسيم التدريب والاختبار
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.25, random_state=42
)

print(f"\nTraining samples: {len(y_train)}")
print(f"Test samples: {len(y_test)}")

# 3. Train Classifier
# تدريب المصنف
print("\n" + "=" * 60)
print("2. Training Classifier")
print("تدريب المصنف")
print("=" * 60)

classifier = MultinomialNB()
classifier.fit(X_train, y_train)

print("✓ Classifier trained successfully")
print("✓ تم تدريب المصنف بنجاح")

# 4. Make Predictions
# عمل التوقعات
predictions = classifier.predict(X_test)

print("\n" + "=" * 60)
print("3. Predictions and Evaluation")
print("التوقعات والتقييم")
print("=" * 60)

print("\nPredictions:")
print("التوقعات:")
for i, (true_label, pred_label) in enumerate(zip(y_test, predictions), 1):
    status = "✓" if true_label == pred_label else "✗"
    print(f"  {i}. True: {true_label}, Predicted: {pred_label} {status}")

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy: {accuracy * 100:.1f}%")
print(f"الدقة: {accuracy * 100:.1f}%")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

