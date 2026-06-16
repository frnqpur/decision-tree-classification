# Decision Tree Classification — Interpretability Demo

## Overview

This repository contains a recruiter-facing Decision Tree classification demo built with Python, scikit-learn, and Streamlit.

The project uses the Adult Income dataset to predict whether an input profile belongs to the `<=50K` or `>50K` income class. The main focus is **model interpretability**, not just prediction. The Streamlit app explains each prediction using the Decision Tree decision path and includes evaluation visuals such as a confusion matrix, classification report, and tree preview.

## Preview

!(screenshots/01-streamlit-demo-overview-1.png)

!(screenshots/01-streamlit-demo-overview-2.png)

---

## Project focus

- Decision Tree classification
- Explainable machine learning
- Prediction probability
- Rule-path explanation
- Confusion matrix
- Classification report
- Decision tree visualization
- Responsible evaluation and leakage awareness

## Important audit note

The original legacy notebook produced a perfect score because it used a `cluster` feature derived from the target label. This created target leakage and made the evaluation misleading.

This demo avoids that issue by training a clean scikit-learn Pipeline using only valid input features.

## Demo features

```text
- Streamlit input form
- Predicted class output
- Prediction probability table
- Decision path explanation
- Confusion matrix
- Classification report
- Decision Tree preview
- Toggle to exclude sensitive attributes: race and sex
```

## Live Demo

Try the Streamlit demo here:

https://decision-tree-classification-qzqfvzduowrcp5pfk5edhh.streamlit.app/

## Tech stack

```text
Python
pandas
NumPy
scikit-learn
Streamlit
matplotlib
```

## Dataset

Dataset file expected by the app:

```text
data/adult_dataset.csv
```

Target column in the original file:

```text
Unnamed: 14
```

The app renames it internally to:

```text
income_class
```

Target classes:

```text
<=50K
>50K
```

## Local setup

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

## Expected folder structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
└── data/
    └── adult_dataset.csv
```

## Model pipeline

The app trains a model using this workflow:

```text
1. Load dataset
2. Replace ? values with NaN
3. Rename target column
4. Split train/test with stratification
5. Impute numeric features with median
6. Impute categorical features with most frequent value
7. One-hot encode categorical features
8. Train DecisionTreeClassifier
9. Evaluate model
10. Explain prediction using decision path
```

## Evaluation

The app displays:

```text
- Test accuracy
- Prediction probability
- Confusion matrix
- Classification report
- Decision Tree visualization
```

## Responsible ML disclaimer

This app is an educational portfolio demo. It should not be used as a production decision system for employment, credit, financial eligibility, or other high-impact decisions.

The dataset includes sensitive attributes such as `race` and `sex`. The app provides an option to exclude those features from model input.

## Portfolio positioning

Recommended wording:

> An interpretability-focused Decision Tree classification demo that turns a legacy ML notebook into a recruiter-ready portfolio project with rule-path explanation, evaluation metrics, and visualization.
