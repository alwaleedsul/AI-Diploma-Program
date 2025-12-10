"""
Unit 2 - Example 1: Advanced Tokenization
الوحدة 2 - مثال 1: التقطيع المتقدم

This example demonstrates:
1. Word tokenization
2. Sentence tokenization
3. Subword tokenization
4. Morphological analysis
"""

import re
from collections import Counter

print("=" * 60)
print("Example 1: Advanced Tokenization")
print("مثال 1: التقطيع المتقدم")
print("=" * 60)

# Sample text
sample_text = """
Natural Language Processing is amazing! It helps computers understand human language.
We can tokenize text into words, sentences, or even subwords. This is fundamental to NLP.
"""

print("\nOriginal Text:")
print("النص الأصلي:")
print(sample_text)

# 1. Word Tokenization
# تقطيع الكلمات
print("\n" + "=" * 60)
print("1. Word Tokenization")
print("تقطيع الكلمات")
print("=" * 60)

def word_tokenize(text):
    """
    Simple word tokenization.
    تقطيع بسيط للكلمات.
    """
    # Remove punctuation and split
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    return words

words = word_tokenize(sample_text)
print(f"\nWords: {words}")
print(f"Total words: {len(words)}")

# Word frequency
word_freq = Counter(words)
print("\nMost common words:")
print("أكثر الكلمات شيوعاً:")
for word, freq in word_freq.most_common(5):
    print(f"  {word}: {freq}")

# 2. Sentence Tokenization
# تقطيع الجمل
print("\n" + "=" * 60)
print("2. Sentence Tokenization")
print("تقطيع الجمل")
print("=" * 60)

def sentence_tokenize(text):
    """
    Simple sentence tokenization.
    تقطيع بسيط للجمل.
    """
    # Split on sentence endings
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

sentences = sentence_tokenize(sample_text)
print(f"\nSentences: {len(sentences)}")
for i, sentence in enumerate(sentences, 1):
    print(f"  {i}. {sentence}")

# 3. Subword Tokenization
# تقطيع الكلمات الفرعية
print("\n" + "=" * 60)
print("3. Subword Tokenization")
print("تقطيع الكلمات الفرعية")
print("=" * 60)

def subword_tokenize(word, n=3):
    """
    Create n-gram subwords.
    إنشاء كلمات فرعية n-gram.
    """
    subwords = []
    for i in range(len(word) - n + 1):
        subwords.append(word[i:i+n])
    return subwords

example_word = "processing"
subwords = subword_tokenize(example_word, n=3)
print(f"\nWord: {example_word}")
print(f"3-gram subwords: {subwords}")

# 4. Morphological Analysis Example
# مثال على التحليل الصرفي
print("\n" + "=" * 60)
print("4. Morphological Analysis")
print("التحليل الصرفي")
print("=" * 60)

# Simple stemming example
# مثال بسيط على الاشتقاق
def simple_stem(word):
    """
    Simple stemming (remove common suffixes).
    اشتقاق بسيط (إزالة اللواحق الشائعة).
    """
    suffixes = ['ing', 'ed', 's', 'es', 'ly', 'er', 'est']
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

test_words = ['running', 'jumped', 'cats', 'quickly', 'faster']
print("\nStemming examples:")
print("أمثلة على الاشتقاق:")
for word in test_words:
    stem = simple_stem(word)
    print(f"  {word} -> {stem}")

print("\n" + "=" * 60)
print("Example completed successfully!")
print("تم إكمال المثال بنجاح!")
print("=" * 60)
print("\nNote: For production, use libraries like NLTK, spaCy, or transformers")
print("ملاحظة: للاستخدام الفعلي، استخدم مكتبات مثل NLTK أو spaCy أو transformers")

