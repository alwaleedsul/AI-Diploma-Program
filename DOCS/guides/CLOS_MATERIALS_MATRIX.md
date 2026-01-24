# CLO ↔ Materials Matrix

**Purpose:** Map each course's Course Learning Outcomes (CLOs) to units and key materials.  
**Reference:** [COMPLETE_COURSE_STRUCTURE_AND_CLOS.md](../../COMPLETE_COURSE_STRUCTURE_AND_CLOS.md), [DETAILED_UNIT_DESCRIPTIONS.md](../../DETAILED_UNIT_DESCRIPTIONS.md), [UNIT_BY_UNIT_AUDIT.md](UNIT_BY_UNIT_AUDIT.md).

---

## Course 01 — Introduction to AI (8 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Traditional vs modern AI; Turing | U1 | unit1-ai-foundations: 01_ai_introduction, 04_philosophy_turing_test |
| CLO2 | Search algorithms; PEAS | U1 | unit1-ai-foundations: 05_adversarial_search_minimax, implementing_search |
| CLO3 | Knowledge representation; ontology | U1, U2 | unit1: 06_knowledge_representation; unit2-ai-concepts: RDF/SPARQL, expert systems |
| CLO4 | Bayesian; uncertainty | U2 | unit2-ai-concepts: 05–07 Bayes, 03–04 supervised/unsupervised |
| CLO5 | ML pipelines; encoding; hypothesis; loss | U2, U3 | unit2-ai-concepts: 08 encoding, 09–10 ML; unit3-ml-basics: 04 regression/classification |
| CLO6 | Feedforward NNs; neurons; activation | U3, U4 | unit3-ml-basics: XOR, Keras; unit4-neural-networks-basics: 01 perceptron, activation |
| CLO7 | CNN, RNN, LSTM; overfitting | U4 | unit4-neural-networks-basics: 03 CNN/RNN; unit4: early stopping, regularization |
| CLO8 | Generative AI; GANs; Transformers; LLMs; ethics | U5 | unit5-generative-ai-intro: 01–04 GenAI, diabetes FFNN, EDA |

---

## Course 02 — Python for AI (5 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Implement 3+ major algorithms (k-NN, DT) | U1–U5 | NOTEBOOKS 00–05; unit* examples |
| CLO2 | Practical project; ML techniques | U5 | NOTEBOOKS 05; unit5-ai-learning-models |
| CLO3 | Metrics; accuracy, precision, recall, F1 | U3–U5 | Optimization, ML models notebooks |
| CLO4 | Case studies; algorithms; effectiveness | U4–U5 | AI learning models |
| CLO5 | Prototype: 2+ techniques (NLP, ML) | U5 | unit5-ai-learning-models |

---

## Course 03 — Mathematics & Probability (6 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Linear algebra, probability for ML | U1, U5 | modules 01, 05 |
| CLO2 | Matrix ops; eigenvalues; multivariable calculus | U1, U2 | modules 01, 02 |
| CLO3 | Statistical methods; hypothesis testing; CI | U3, U5 | modules 03, 05 |
| CLO4 | PCA, SVD, t-SNE | U4 | module 04 |
| CLO5 | Gradient descent; optimization | U3 | module 03 |
| CLO6 | Regression; dot products; projections; Python | U1–U5 | All modules |

---

## Course 04 — Machine Learning (7 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Preprocessing; missing; categorical; scaling | U1 | unit1-data-processing: 01–03 |
| CLO2 | Linear/multiple regression | U1 | unit1-data-processing: 04_linear_regression |
| CLO3 | Ridge, Lasso, SVR; model selection | U1, U2 | unit1, unit2-regression |
| CLO4 | Classification; Logistic, DT, SVM, RF | U3 | unit3-classification |
| CLO5 | Clustering; K-means; PCA, LDA | U4 | unit4-clustering |
| CLO6 | Cross-validation; grid search; XGBoost, AdaBoost | U5 | unit5-model-selection |
| CLO7 | Interpret results; recommendations | U2–U5 | All units |

---

## Course 05 — Scalable Data Science (5 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Analyze and visualize data | U1, U3 | unit1-introduction; unit3-visualization |
| CLO2 | Scale data processing | U5 | unit5-scaling: Dask, PySpark, RAPIDS |
| CLO3 | Clean and prepare datasets | U2 | unit2-cleaning |
| CLO4 | Build, evaluate, deploy ML | U4, U5 | unit4-ml-intro; unit5 scaling/deployment |
| CLO5 | End-to-end data science project | U1–U5 | PROJECTS; all units |

---

## Course 06 — AI Ethics (5 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Ethical frameworks; case studies | U1 | unit1-ethics-foundations |
| CLO2 | Bias, fairness, discrimination; metrics | U2 | unit2-bias-justice |
| CLO3 | Privacy, security; GDPR, CCPA | U3 | unit3-privacy-security |
| CLO4 | Transparency; XAI; LIME, SHAP | U4 | unit4-transparency-accountability |
| CLO5 | Governance; regulations; policies | U5 | unit5-governance-regulations |

---

## Course 07 — NLP (10 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | NLP fundamentals | U1 | unit1-nlp-fundamentals |
| CLO2 | Tokenization; stemming; lemmatization; vectorization | U2 | unit2-tokenization-morphology |
| CLO3 | ML for NLP; NER; topic modeling | U3 | unit3-ml-for-nlp |
| CLO4 | RNN, LSTM, Transformers for NLP | U4 | unit4-deep-learning-nlp |
| CLO5 | NLTK, spaCy, Transformers | U2–U4 | All units |
| CLO6 | Sentiment; summarization; chatbots | U5 | unit5-applications-ethics |
| CLO7 | Ethics; bias and fairness | U5 | unit5-applications-ethics |
| CLO8 | Fine-tune pre-trained LMs | U4, U5 | unit4, unit5 |
| CLO9 | Multilingual; cross-lingual | U5 | unit5 |
| CLO10 | End-to-end NLP pipelines | U1–U5 | All units |

---

## Course 08 — Deep Learning (5 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | DL basics; backprop; gradient descent | U1 | unit1-deep-learning-basics |
| CLO2 | CNN, RNN, Transformers | U2, U3 | unit2-cnns; unit3-rnns-transformers |
| CLO3 | Deploy; image; NLP; RL | U3–U5 | unit3-rnns-transformers; unit4-advanced-dl; unit5-deployment |
| CLO4 | Hyperparameter tuning; regularization; transfer learning | U4, U5 | unit4-advanced-dl (transfer); unit5-deployment |
| CLO5 | Ethics; bias; fairness; interpretability | U4, U5 | unit4, unit5 |

---

## Course 09 — Reinforcement Learning (6 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Agents; rewards; policies; MDPs | U1 | unit1-rl-fundamentals |
| CLO2 | Q-learning; policy gradient; Actor-Critic | U2 | unit2-policy-value |
| CLO3 | Deep RL | U3 | unit3-deep-rl |
| CLO4 | Optimize; training efficiency | U3, U4 | unit3, unit4-exploration-exploitation |
| CLO5 | Applications; navigation; games | U5 | unit5-applications |
| CLO6 | Exploration vs exploitation; ethics | U4, U5 | unit4, unit5 |

---

## Course 10 — Generative AI (7 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Probabilistic modeling; latent space; sampling | U1 | unit1-generative-fundamentals |
| CLO2 | VAEs, GANs, Transformers | U1, U2, U3 | unit1-generative-fundamentals (GANs/VAEs); unit2-text-generation (Transformers/GPT); unit3-image-generation (GANs/VAEs for images) |
| CLO3 | Implement; optimize; TensorFlow, PyTorch | U1, U2, U3 | unit1, unit2-text-generation, unit3-image-generation |
| CLO4 | FID, BLEU, perplexity; mode collapse | U1, U2, U3 | unit1, unit2-text-generation, unit3-image-generation |
| CLO5 | Applications; content creation; augmentation | U5 | unit5-future-trends |
| CLO6 | Ethics; bias; misinformation; IP | U4 | unit4-ethics-regulations |
| CLO7 | Emerging trends; diffusion; multimodal | U5 | unit5-future-trends |

---

## Course 11 — Deploying AI Models (6 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Deployment concepts and process | U1 | unit1-deployment-basics |
| CLO2 | Package models | U2 | unit2-versioning-serving |
| CLO3 | APIs; serving; inference pipelines | U2 | unit2-versioning-serving |
| CLO4 | Docker; Kubernetes | U4 | unit4-containers-orchestration |
| CLO5 | CI/CD | U5 | unit5-pipelines-monitoring |
| CLO6 | Monitor; degradation; bias | U5 | unit5-pipelines-monitoring |

---

## Course 12 — Graduation Project (5 CLOs)

| CLO | Summary | Units | Key materials |
|-----|---------|-------|----------------|
| CLO1 | Design and develop AI solution | U1–U5 | All units; PROJECTS |
| CLO2 | Integrate AI subdisciplines | U1–U5 | All units |
| CLO3 | Evaluate performance; metrics | U4 | unit4-evaluation-optimization |
| CLO4 | Documentation; communication | U1, U5 | unit1-project-planning; unit5-documentation-presentation |
| CLO5 | Ethical, legal, social considerations | U1–U5 | All units |

---

## Summary

- **75 CLOs** across 12 courses mapped to units and key materials.
- **Materials:** Unit folders (examples, exercises), NOTEBOOKS (Course 02), modules (Course 03), PROJECTS (Course 05, 12).
- For full CLO text, see [COMPLETE_COURSE_STRUCTURE_AND_CLOS.md](../../COMPLETE_COURSE_STRUCTURE_AND_CLOS.md).

**Last updated:** Deep-dive execution; Phase 2 audit.
