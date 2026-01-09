# PDF to Notebook Topic Mapping

## Overview

This document maps each topic from the PDF curriculum to corresponding notebooks, identifying coverage and gaps.

**Status:** 🔄 **IN PROGRESS**  
**Last Updated:** 2025-01-10

---

## Course 01: Introduction to AI (AIAT 111)

### Unit 1: AI Foundations | أساسيات الذكاء الاصطناعي

#### PDF Topics (8 Main Topics with Subtopics)

**Topic 1: مقدمة في الذكاء الاصطناعي (Introduction to AI)**
- Subtopic: ما هو الذكاء الاصطناعي؟ (What is AI?)
- Subtopic: الذكاء الاصطناعي الضعيف مقابل القوي (Weak vs Strong AI)
- Subtopic: الأنظمة الذكية النموذجية (Typical intelligent systems)
- Subtopic: تاريخ موجز للذكاء الاصطناعي (Brief history of AI)

**Coverage:**
- ✅ `01_ai_introduction.ipynb` - Covers: What is AI, Weak vs Strong AI, Typical systems
- ✅ `02_ai_history.ipynb` - Covers: Brief history of AI

**Status:** ✅ **COVERED**

---

**Topic 2: العوامل الذكية والعقلانية (Intelligent Agents and Rationality)**
- Subtopic: تعريف العوامل الذكية (Definition of intelligent agents)
- Subtopic: مكونات عامل الذكاء الاصطناعي (Components of AI agent)
- Subtopic: العقلانية في الذكاء الاصطناعي (Rationality in AI)

**Coverage:**
- ⚠️ `01_ai_introduction.ipynb` - May cover basics, needs verification
- ❌ **MISSING:** Dedicated notebook for agents and rationality

**Status:** ⚠️ **PARTIALLY COVERED** - Needs dedicated notebook

---

**Topic 3: فلسفة الذكاء الاصطناعي (Philosophy of AI)**
- Subtopic: المساهمات الرئيسية لتورينغ (Turing's contributions)
- Subtopic: اختبار تورينغ وتداعياته (Turing test and implications)
- Subtopic: الاعتراضات على الذكاء الاصطناعي (Objections to AI)

**Coverage:**
- ❌ **MISSING:** No notebook covers philosophy of AI, Turing test, objections

**Status:** ❌ **NOT COVERED** - **NEEDS NOTEBOOK**

---

**Topic 4: خوارزميات البحث في الذكاء الاصطناعي (Search Algorithms in AI)**
- Subtopic: تقنيات البحث التقليدية (غير المستنيرة والتوجيهية) (Traditional search techniques - uninformed and informed)
- Subtopic: خوارزمية البحث الجشع وتطبيقاتها (Greedy search algorithm and applications)

**Coverage:**
- ✅ `unit2-search-algorithms/01_bfs_algorithm.ipynb` - Covers: BFS (uninformed search)
- ✅ `unit2-search-algorithms/02_dfs_algorithm.ipynb` - Covers: DFS (uninformed search)
- ✅ `unit2-search-algorithms/03_astar_algorithm.ipynb` - Covers: A* (informed search)
- ⚠️ **MISSING:** Greedy search algorithm (may be covered in Unit 2)

**Status:** ⚠️ **PARTIALLY COVERED** - Search algorithms are in Unit 2, not Unit 1

---

**Topic 5: البحث العدائي ونظرية الألعاب (Adversarial Search and Game Theory)**
- Subtopic: مقدمة في البحث العدائي (Introduction to adversarial search)
- Subtopic: خوارزمية MiniMax
- Subtopic: التقليم Alpha-Beta

**Coverage:**
- ❌ **MISSING:** No notebook covers adversarial search, MiniMax, Alpha-Beta pruning

**Status:** ❌ **NOT COVERED** - **NEEDS NOTEBOOK**

---

**Topic 6: تمثيل المعرفة والاستدلال (Knowledge Representation and Inference)**
- Subtopic: نظرية المعرفة في الذكاء الاصطناعي (Knowledge theory in AI)
- Subtopic: نماذج المعرفة وتمثيلها (Knowledge models and representation)
- Subtopic: بنية الوكالات المعتمدين على المعرفة (Knowledge-based agent structure)

**Coverage:**
- ✅ `unit3-knowledge-representation/01_knowledge_graph.ipynb` - Covers: Knowledge graphs
- ⚠️ **MISSING:** Knowledge theory basics, Knowledge models, Knowledge-based agents

**Status:** ⚠️ **PARTIALLY COVERED** - Some coverage in Unit 3, but Unit 1 basics missing

---

**Topic 7: بايثون لتطوير الذكاء الاصطناعي (Python for AI Development)**
- Subtopic: أساسيات بايثون (القوائم، القواميس، الحلقات، جمل if) (Python basics: lists, dicts, loops, if statements)
- Subtopic: مصفوفات NumPy
- Subtopic: قراءة وكتابة الملفات في بايثون (File I/O in Python)

**Coverage:**
- ✅ `Course 02/` - Course 02 covers Python basics extensively
- ⚠️ **MISSING:** Unit 1 should have basic Python introduction for AI context

**Status:** ⚠️ **COVERED IN COURSE 02** - But Unit 1 may need brief introduction

---

**Topic 8: مقدمة في الذكاء الاصطناعي التوليدي (Introduction to Generative AI)**
- Subtopic: نظرة عامة على أطر العمل للذكاء الاصطناعي التوليدي (Overview of Generative AI frameworks)
- Subtopic: التطبيقات والاعتبارات الأخلاقية (Applications and ethical considerations)

**Coverage:**
- ✅ `unit5-generative-ai-intro/01_generative_ai_introduction.ipynb` - Covers: Generative AI introduction
- ✅ `unit5-generative-ai-intro/02_generative_vs_discriminative.ipynb` - Covers: Generative vs discriminative
- ⚠️ **NOTE:** This topic is covered in Unit 5, not Unit 1

**Status:** ✅ **COVERED IN UNIT 5** - Correct placement

---

### Unit 1 Summary

| Topic | PDF Topic | Notebook Coverage | Status |
|-------|-----------|-------------------|--------|
| 1 | Introduction to AI | ✅ 2 notebooks | ✅ Covered |
| 2 | Intelligent Agents | ⚠️ Partial | ⚠️ Needs notebook |
| 3 | Philosophy of AI | ❌ Missing | ❌ **CRITICAL GAP** |
| 4 | Search Algorithms | ✅ Unit 2 | ⚠️ Wrong unit |
| 5 | Adversarial Search | ❌ Missing | ❌ **CRITICAL GAP** |
| 6 | Knowledge Representation | ⚠️ Partial | ⚠️ Needs expansion |
| 7 | Python Basics | ✅ Course 02 | ⚠️ May need intro |
| 8 | Generative AI Intro | ✅ Unit 5 | ✅ Correct |

**Critical Gaps:**
1. ❌ Philosophy of AI (Turing test, objections) - **NEEDS NOTEBOOK**
2. ❌ Adversarial Search (MiniMax, Alpha-Beta) - **NEEDS NOTEBOOK**
3. ⚠️ Intelligent Agents and Rationality - **NEEDS DEDICATED NOTEBOOK**

---

### Unit 2: Search Algorithms | خوارزميات البحث

#### PDF Topics

**Coverage:**
- ✅ `01_bfs_algorithm.ipynb` - Breadth-First Search
- ✅ `02_dfs_algorithm.ipynb` - Depth-First Search
- ✅ `03_astar_algorithm.ipynb` - A* Algorithm

**Status:** ✅ **GOOD COVERAGE** - 3 notebooks cover main search algorithms

**Note:** Greedy search may need to be added if not covered

---

### Unit 3: Knowledge Representation | تمثيل المعرفة

#### PDF Topics

**Coverage:**
- ✅ `01_knowledge_graph.ipynb` - Knowledge graphs

**Missing Topics:**
- ❌ Rule-based systems
- ❌ Expert systems
- ❌ Knowledge bases structure

**Status:** ⚠️ **NEEDS EXPANSION** - Only 1 notebook, missing rule-based and expert systems

**Recommendations:**
- ✅ Add: `02_rule_based_systems.ipynb`
- ✅ Add: `03_expert_systems.ipynb`

---

### Unit 4: Neural Networks Basics | أساسيات الشبكات العصبية

#### PDF Topics

**Coverage:**
- ✅ `01_simple_perceptron.ipynb` - Perceptrons
- ✅ `02_generative_ai_intro.ipynb` - Generative AI intro (may be misplaced)

**Status:** ✅ **COVERED** - Basic neural networks covered

---

### Unit 5: Introduction to Generative AI | مقدمة في الذكاء الاصطناعي التوليدي

#### PDF Topics

**Coverage:**
- ✅ `01_generative_ai_introduction.ipynb`
- ✅ `02_generative_vs_discriminative.ipynb`
- ✅ `03_course_summary.ipynb`

**Status:** ✅ **GOOD COVERAGE** - 3 notebooks cover generative AI introduction

---

## Course 07: Natural Language Processing (AIAT 121)

### Unit 1: NLP Fundamentals

#### PDF Topics
- Introduction to NLP
- Text preprocessing
- Tokenization
- Normalization
- Stop word removal
- Stemming and lemmatization
- Text representation (BoW, TF-IDF)
- Basic NLP tasks

**Coverage:**
- ✅ `01_text_preprocessing.ipynb` - Covers preprocessing, tokenization, normalization
- ✅ `02_nltk_spacy_introduction.ipynb` - Covers NLP frameworks
- ✅ `03_real_world_nlp_applications.ipynb` - Covers applications

**Status:** ✅ **GOOD COVERAGE** - 3 notebooks cover main topics

---

## Course 08: Deep Learning (AIAT 122)

### Unit 1: Deep Learning Basics

#### PDF Topics
- Deep learning introduction
- Neural network architecture
- Layers and neurons
- Activation functions
- Building neural networks
- Training neural networks
- Model evaluation
- Backpropagation
- Optimization techniques

**Coverage:**
- ✅ `01_simple_neural_network.ipynb` - Covers basic NN, architecture, training
- ✅ `02_backpropagation_detailed.ipynb` - Covers backpropagation
- ✅ `03_optimization_techniques.ipynb` - Covers optimization

**Status:** ✅ **GOOD COVERAGE** - 3 notebooks cover main topics

---

## Summary of Gaps

### Critical Gaps (Need Immediate Attention)

1. **Course 01 Unit 1:**
   - ❌ Philosophy of AI (Turing test, objections) - **NEEDS NOTEBOOK**
   - ❌ Adversarial Search (MiniMax, Alpha-Beta) - **NEEDS NOTEBOOK**
   - ⚠️ Intelligent Agents and Rationality - **NEEDS DEDICATED NOTEBOOK**

2. **Course 01 Unit 3:**
   - ❌ Rule-based systems - **NEEDS NOTEBOOK**
   - ❌ Expert systems - **NEEDS NOTEBOOK**

### Missing Exercises

- Course 07 Unit 5: 0 exercises
- Course 08 Unit 5: 0 exercises
- Course 09 Units 1, 3: 0 exercises
- Course 10 Units 1, 5: 0 exercises
- Course 11 Units 3, 4: 0 exercises

### Low Example Counts

- Course 01 Units 1, 3, 4: Need more examples
- Course 09 Unit 4: Only 2 examples
- Course 10 Unit 3: Only 2 examples
- Course 11 Units 1, 5: Only 2 examples

---

## Next Steps

1. ✅ **Complete:** Topic-by-topic mapping created
2. ⏳ **Next:** Add missing notebooks for critical gaps
3. ⏳ **Next:** Add missing exercises
4. ⏳ **Next:** Expand notebooks with low example counts

---

**Date:** 2025-01-10  
**Status:** 🔄 **MAPPING COMPLETE - GAPS IDENTIFIED**

