"""
Unit 5 - Example 1: Bias Detection in NLP
الوحدة 5 - مثال 1: اكتشاف التحيز في معالجة اللغة الطبيعية

This example demonstrates:
1. Detecting bias in word associations
2. Gender bias in language models
3. Mitigation strategies
"""

print("=" * 60)
print("Example 1: Bias Detection in NLP")
print("مثال 1: اكتشاف التحيز في معالجة اللغة الطبيعية")
print("=" * 60)

# 1. Understanding Bias in NLP
# فهم التحيز في معالجة اللغة الطبيعية
print("\n1. What is Bias in NLP?")
print("ما هو التحيز في معالجة اللغة الطبيعية؟")
print("-" * 60)

bias_explanation = """
Bias in NLP can manifest as:
- Gender bias (associating certain professions with genders)
- Racial bias (stereotypical associations)
- Cultural bias (favoring certain languages/cultures)
- Socioeconomic bias (class-based associations)

التحيز في معالجة اللغة الطبيعية يمكن أن يظهر كـ:
- تحيز جندري (ربط مهن معينة بالأجناس)
- تحيز عرقي (ارتباطات نمطية)
- تحيز ثقافي (تفضيل لغات/ثقافات معينة)
- تحيز اجتماعي اقتصادي (ارتباطات قائمة على الطبقة)
"""

print(bias_explanation)

# 2. Example: Gender Bias Detection
# مثال: اكتشاف التحيز الجندري
print("\n" + "=" * 60)
print("2. Gender Bias Example")
print("مثال على التحيز الجندري")
print("=" * 60)

# Simulated word associations (in real scenario, from word embeddings)
# ارتباطات كلمات محاكاة (في السيناريو الحقيقي، من تضمينات الكلمات)
professions = ["doctor", "nurse", "engineer", "teacher", "pilot"]
gender_associations = {
    "doctor": {"male": 0.7, "female": 0.3},
    "nurse": {"male": 0.2, "female": 0.8},
    "engineer": {"male": 0.8, "female": 0.2},
    "teacher": {"male": 0.4, "female": 0.6},
    "pilot": {"male": 0.9, "female": 0.1}
}

print("\nGender associations with professions:")
print("الارتباطات الجندرية مع المهن:")
print("Profession | Male | Female | Bias Level")
print("-" * 50)

for profession in professions:
    male_score = gender_associations[profession]["male"]
    female_score = gender_associations[profession]["female"]
    bias_level = abs(male_score - female_score)
    bias_status = "High" if bias_level > 0.5 else "Moderate" if bias_level > 0.3 else "Low"
    
    print(f"{profession:10} | {male_score:.2f} | {female_score:.2f} | {bias_status}")

# 3. Bias Mitigation Strategies
# استراتيجيات التخفيف من التحيز
print("\n" + "=" * 60)
print("3. Bias Mitigation Strategies")
print("استراتيجيات التخفيف من التحيز")
print("=" * 60)

mitigation_strategies = [
    "Diverse training data - Ensure balanced representation",
    "Debiasing algorithms - Remove bias from embeddings",
    "Regular auditing - Test models for bias regularly",
    "Transparent documentation - Document known biases",
    "Fair evaluation metrics - Use fairness-aware metrics"
]

print("\nStrategies:")
print("الاستراتيجيات:")
for i, strategy in enumerate(mitigation_strategies, 1):
    print(f"  {i}. {strategy}")

# 4. Responsible NLP Checklist
# قائمة التحقق من معالجة اللغة الطبيعية المسؤولة
print("\n" + "=" * 60)
print("4. Responsible NLP Checklist")
print("قائمة التحقق من معالجة اللغة الطبيعية المسؤولة")
print("=" * 60)

checklist = [
    "✓ Test for bias in training data",
    "✓ Evaluate model on diverse test sets",
    "✓ Document known limitations",
    "✓ Provide transparency in model decisions",
    "✓ Regular bias audits",
    "✓ Include diverse perspectives in development"
]

print("\nChecklist:")
print("قائمة التحقق:")
for item in checklist:
    print(f"  {item}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)

