"""
Unit 4 - Example 2: Introduction to Generative AI
الوحدة 4 - مثال 2: مقدمة في الذكاء الاصطناعي التوليدي

This example demonstrates:
1. Understanding generative vs discriminative models
2. Basic generative AI concepts
3. Simple example of data generation
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 60)
print("Example 2: Introduction to Generative AI")
print("مثال 2: مقدمة في الذكاء الاصطناعي التوليدي")
print("=" * 60)

# 1. Generative vs Discriminative Models
# النماذج التوليدية مقابل التمييزية
print("\n1. Generative vs Discriminative Models")
print("النماذج التوليدية مقابل التمييزية")
print("-" * 60)

explanation = """
Generative Models (النماذج التوليدية):
- Learn the joint probability P(X, Y)
- Can generate new data samples
- Examples: GANs, VAEs, Naive Bayes
- Answer: "What is the probability of this data?"

Discriminative Models (النماذج التمييزية):
- Learn conditional probability P(Y|X)
- Focus on classification/decision boundary
- Examples: Logistic Regression, SVM, Neural Networks
- Answer: "What class does this data belong to?"
"""

print(explanation)

# 2. Simple Generative Example: Data Generation
# مثال توليدي بسيط: توليد البيانات
print("\n" + "=" * 60)
print("2. Simple Generative Example")
print("مثال توليدي بسيط")
print("=" * 60)

def generate_data_from_distribution(mean, std, n_samples=100):
    """
    Generate data from a normal distribution.
    توليد بيانات من توزيع طبيعي.
    
    This is a simple example of generative modeling.
    هذا مثال بسيط على النمذجة التوليدية.
    """
    return np.random.normal(mean, std, n_samples)

# Generate data points
# توليد نقاط البيانات
print("\nGenerating data from learned distribution...")
print("توليد البيانات من التوزيع المتعلم...")

# Simulate: We learned that a class has mean=5, std=2
# محاكاة: تعلمنا أن فئة لها متوسط=5، انحراف معياري=2
learned_mean = 5
learned_std = 2

# Generate new samples
# توليد عينات جديدة
generated_data = generate_data_from_distribution(learned_mean, learned_std, 50)

print(f"\nGenerated {len(generated_data)} samples")
print(f"Mean: {np.mean(generated_data):.2f}")
print(f"Std: {np.std(generated_data):.2f}")

# 3. Applications of Generative AI
# تطبيقات الذكاء الاصطناعي التوليدي
print("\n" + "=" * 60)
print("3. Applications of Generative AI")
print("تطبيقات الذكاء الاصطناعي التوليدي")
print("=" * 60)

applications = {
    "Image Generation": "Creating new images (GANs, Diffusion models)",
    "Text Generation": "Writing text, stories, code (GPT, LLMs)",
    "Data Augmentation": "Creating synthetic training data",
    "Style Transfer": "Applying artistic styles to images",
    "Super Resolution": "Enhancing image quality"
}

print("\nCommon Applications:")
print("التطبيقات الشائعة:")
for app, description in applications.items():
    print(f"\n{app}:")
    print(f"  {description}")

# 4. Why Generative AI Matters
# لماذا يهم الذكاء الاصطناعي التوليدي
print("\n" + "=" * 60)
print("4. Why Generative AI Matters")
print("لماذا يهم الذكاء الاصطناعي التوليدي")
print("=" * 60)

importance_points = [
    "Creates new content, not just classifies existing data",
    "Can work with limited data (data augmentation)",
    "Enables creative applications",
    "Foundation for advanced AI systems"
]

print("\nKey Points:")
print("النقاط الرئيسية:")
for i, point in enumerate(importance_points, 1):
    print(f"  {i}. {point}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: This is an introduction. Full generative AI is covered in Course 10 (AIAT 124)")
print("ملاحظة: هذه مقدمة. الذكاء الاصطناعي التوليدي الكامل يغطى في المقرر 10 (AIAT 124)")

