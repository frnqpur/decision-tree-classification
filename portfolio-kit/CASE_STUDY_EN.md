# Case Study — Decision Tree Classification Explainability Demo

## Overview

This project is a machine learning demo using a Decision Tree classifier to predict income class from tabular profile data. The main focus is not only the prediction output, but also the interpretability of the model through decision rules, evaluation metrics, and tree visualization.

The project was prepared from a legacy Jupyter Notebook that included exploratory data analysis, preprocessing, Decision Tree training, evaluation, and visualization. During the portfolio audit, the original perfect accuracy was identified as misleading because the notebook introduced a `cluster` feature derived from the target label.

For this reason, the project was reframed as a **Decision Tree interpretability and evaluation demo**.

## Problem statement

How can a tabular classification project be presented in a recruiter-friendly way while keeping the model transparent, explainable, and responsibly evaluated?

## Project goals

- Build a simple Decision Tree classification demo.
- Predict the target class `<=50K` or `>50K`.
- Display prediction probabilities.
- Explain predictions using the Decision Tree rule path.
- Show a confusion matrix and classification report.
- Show a visual preview of the Decision Tree.
- Avoid target leakage from the legacy notebook.
- Prepare the project for GitHub and portfolio presentation.

## Dataset

The project uses the Adult Income dataset included in the original project.

Target:

```text
income_class
```

Target classes:

```text
<=50K
>50K
```

Main features:

```text
age, workclass, fnlwgt, education, education.num,
marital.status, occupation, relationship, race, sex,
capital.gain, capital.loss, hours.per.week, native.country
```

## Technical approach

The model is built using a scikit-learn Pipeline:

```text
1. Load the dataset
2. Rename the target column
3. Replace ? values with NaN
4. Split the data into train and test sets using stratification
5. Impute numeric features using the median
6. Impute categorical features using the most frequent value
7. Apply one-hot encoding to categorical features
8. Train a DecisionTreeClassifier
9. Evaluate using a confusion matrix and classification report
10. Display the decision path for user input
```

## Explainability

Decision Trees are suitable for recruiter-facing demos because they can be explained through simple rules. In this demo, each user input is processed through the pipeline, and the app shows the decision path used by the model to reach a prediction.

Example explanation:

```text
capital.gain <= threshold
education.num > threshold
hours.per.week <= threshold
```

This makes the model easier to understand compared to a black-box prediction interface.

## Evaluation

The demo does not rely only on accuracy. It also displays:

- Confusion matrix
- Precision
- Recall
- F1-score
- Support
- Prediction probability

This is important because the dataset has an imbalanced target distribution, so accuracy alone may not fully describe model quality.

## Visualization

The app includes the following visual elements:

- Confusion matrix
- Limited-depth Decision Tree preview
- Prediction probability table
- Decision path table

The tree preview is intentionally limited to the first few levels so it remains readable.

## Responsible ML note

The dataset contains sensitive attributes such as `race` and `sex`. The demo includes an option to exclude those attributes from model input.

This project should be presented as an educational portfolio demo, not as a production system for financial, employment, credit, or eligibility decisions.

## Final outcome

The final project is stronger as a portfolio item because it demonstrates:

- the ability to review and audit a legacy ML notebook,
- the ability to identify target leakage risk,
- the ability to rebuild a safer ML pipeline,
- the ability to explain a Decision Tree model,
- the ability to communicate ML results clearly to recruiters.

## My role

In this project, I worked on:

- reviewing the legacy project structure,
- identifying the dataset and target column,
- analyzing preprocessing and evaluation steps,
- detecting leakage risk,
- designing a recruiter-facing demo,
- preparing deployment documentation,
- writing bilingual portfolio documentation.
