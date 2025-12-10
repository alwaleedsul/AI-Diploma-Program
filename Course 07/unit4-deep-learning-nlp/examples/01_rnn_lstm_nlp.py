"""
Unit 4 - Example 1: RNNs and LSTMs for NLP
الوحدة 4 - مثال 1: RNNs و LSTMs لمعالجة اللغة الطبيعية

This example demonstrates:
1. RNN architecture for sequences
2. LSTM for long-term dependencies
3. Text sequence modeling
"""

import numpy as np

print("=" * 60)
print("Example 1: RNNs and LSTMs for NLP")
print("مثال 1: RNNs و LSTMs لمعالجة اللغة الطبيعية")
print("=" * 60)

# 1. Understanding RNNs
# فهم RNNs
print("\n1. Recurrent Neural Networks (RNNs)")
print("الشبكات العصبية المتكررة (RNNs)")
print("-" * 60)

rnn_explanation = """
RNN Structure:
- Processes sequences one element at a time
- Maintains hidden state across time steps
- Can remember previous context
- Useful for sequential data like text

هيكل RNN:
- يعالج التسلسلات عنصراً واحداً في كل مرة
- يحافظ على الحالة المخفية عبر الخطوات الزمنية
- يمكنه تذكر السياق السابق
- مفيد للبيانات المتسلسلة مثل النص
"""

print(rnn_explanation)

# 2. LSTM for Long-term Dependencies
# LSTM للتبعيات طويلة المدى
print("\n" + "=" * 60)
print("2. Long Short-Term Memory (LSTM)")
print("الذاكرة قصيرة وطويلة المدى (LSTM)")
print("=" * 60)

lstm_explanation = """
LSTM Advantages over RNN:
- Can remember information for longer periods
- Solves vanishing gradient problem
- Better for long sequences
- Three gates: Forget, Input, Output

مزايا LSTM على RNN:
- يمكنه تذكر المعلومات لفترات أطول
- يحل مشكلة اختفاء التدرج
- أفضل للتسلسلات الطويلة
- ثلاث بوابات: النسيان، الإدخال، الإخراج
"""

print(lstm_explanation)

# 3. Simple Sequence Example
# مثال بسيط على التسلسل
print("\n" + "=" * 60)
print("3. Sequence Modeling Example")
print("مثال على نمذجة التسلسل")
print("=" * 60)

# Simple character-level sequence
# تسلسل بسيط على مستوى الأحرف
text_sequence = "hello"
char_to_int = {char: i for i, char in enumerate(set(text_sequence))}
int_to_char = {i: char for char, i in char_to_int.items()}

print(f"\nText sequence: {text_sequence}")
print(f"Character mapping: {char_to_int}")

# Convert to sequence of integers
# تحويل إلى تسلسل من الأعداد الصحيحة
sequence = [char_to_int[char] for char in text_sequence]
print(f"Integer sequence: {sequence}")

# Simulate RNN processing
# محاكاة معالجة RNN
print("\nSimulating RNN processing:")
print("محاكاة معالجة RNN:")
hidden_state = 0
for i, char_int in enumerate(sequence):
    char = int_to_char[char_int]
    # Simple update (in real RNN, this would be a neural network)
    hidden_state = hidden_state * 0.5 + char_int * 0.5
    print(f"  Step {i+1}: Input='{char}' ({char_int}), Hidden state={hidden_state:.2f}")

# 4. Applications
# التطبيقات
print("\n" + "=" * 60)
print("4. NLP Applications")
print("تطبيقات معالجة اللغة الطبيعية")
print("=" * 60)

applications = {
    "Text Generation": "Generate next word/character in sequence",
    "Sentiment Analysis": "Classify sentiment of text sequences",
    "Machine Translation": "Translate sequences from one language to another",
    "Named Entity Recognition": "Identify entities in text sequences"
}

print("\nCommon Applications:")
print("التطبيقات الشائعة:")
for app, description in applications.items():
    print(f"\n{app}:")
    print(f"  {description}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: For actual implementation, use TensorFlow/Keras or PyTorch")
print("ملاحظة: للتنفيذ الفعلي، استخدم TensorFlow/Keras أو PyTorch")

