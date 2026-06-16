# Project Brief — Decision Tree Classification Portfolio Kit

## Project name

**Decision Tree Classification: Income Class Explainability Demo**

## One-line summary

A recruiter-facing machine learning portfolio project that demonstrates Decision Tree classification, transparent model evaluation, and simple explainability through decision rules, confusion matrix, and tree visualization.

## Background

This project started from a legacy Python/Jupyter Notebook that used the Adult Income dataset to classify income class into `<=50K` and `>50K`. The original notebook included exploratory data analysis, preprocessing, categorical encoding, Decision Tree modeling, evaluation, and tree visualization.

During portfolio preparation, the project was reframed from a simple prediction notebook into an **interpretability-focused Decision Tree case study**. The goal is to help recruiters quickly understand not only the prediction result, but also how a Decision Tree reaches a decision.

## Main focus

- Decision Tree classification
- Structured preprocessing for tabular data
- Train/test evaluation
- Confusion matrix and classification report
- Decision path explanation
- Decision tree visualization
- Responsible presentation of model limitations

## Dataset

The project uses the Adult Income dataset included in the original project files as `adult_dataset.csv`.

Target column:

```text
Unnamed: 14 → income_class
```

Target classes:

```text
<=50K
>50K
```

Main feature groups:

```text
Numeric features:
- age
- fnlwgt
- education.num
- capital.gain
- capital.loss
- hours.per.week

Categorical features:
- workclass
- education
- marital.status
- occupation
- relationship
- race
- sex
- native.country
```

## Important audit note

The original notebook produced a perfect score because it introduced a `cluster` feature derived from the target label. That made the result misleading because the model effectively learned from target-derived information.

For the recruiter demo, the model must avoid this leakage by using only legitimate input features and excluding target-derived columns from training.

## Recommended portfolio positioning

Use this framing:

> I prepared an interpretable Decision Tree classification demo from a legacy notebook, audited the workflow for leakage risk, rebuilt the model with a safer preprocessing pipeline, and presented the result with decision-path explanation and evaluation visuals.

Avoid this framing:

> I built a 100% accurate income prediction model.

## Deliverables

- Streamlit demo app
- Deployment guide
- GitHub README draft
- Local setup guide
- Recruiter-facing project summary
- Case study in Indonesian and English
- CV bullet options
- Screenshot checklist
- Security cleanup checklist

## Success criteria

The project is portfolio-ready when a recruiter can:

1. Understand the classification problem in under one minute.
2. Run or view the Streamlit demo.
3. Input a sample profile and see a predicted class.
4. See a simple explanation of the Decision Tree rule path.
5. View model evaluation using a confusion matrix and classification report.
6. See a limited-depth tree visualization.
7. Understand that the original leakage issue was identified and avoided.
