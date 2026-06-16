# Recruiter View — Decision Tree Classification Demo

## What this project shows

This project demonstrates my ability to prepare a machine learning project for portfolio presentation with a focus on interpretability, evaluation, and responsible communication.

The demo uses a Decision Tree classifier to predict an income class from tabular profile data. Instead of only showing a prediction result, the app explains the model decision using the rule path followed inside the tree.

## Why this project is relevant

Many machine learning projects stop at accuracy. This project goes further by showing:

- how the model was trained,
- how the prediction is explained,
- how the result is evaluated,
- how model limitations are communicated,
- how leakage risk was identified in the original notebook.

## What recruiters can quickly review

### 1. Input form

The demo provides a simple form with features such as age, education, occupation, working hours, capital gain, and other dataset fields.

### 2. Prediction result

The app predicts whether the input profile belongs to:

```text
<=50K
>50K
```

### 3. Prediction probability

The app displays class probabilities so the recruiter can see whether the model is confident or uncertain.

### 4. Decision path explanation

The app explains the decision using human-readable tree rules, for example:

```text
capital.gain <= threshold
education.num > threshold
hours.per.week <= threshold
```

This makes the model more understandable than a black-box prediction.

### 5. Confusion matrix

The app includes a confusion matrix to show correct and incorrect predictions across both classes.

### 6. Classification report

The app includes precision, recall, F1-score, and support for each class.

### 7. Decision tree visualization

The app shows the first levels of the tree so recruiters can see how the model splits the data.

## Key technical skills demonstrated

- Python
- pandas
- scikit-learn
- Streamlit
- DecisionTreeClassifier
- Pipeline-based preprocessing
- One-hot encoding
- Missing value imputation
- Train/test split
- Model evaluation
- Interpretable ML presentation

## Responsible ML notes

The dataset includes sensitive attributes such as race and sex. The recruiter demo should provide an option to exclude those features from model input.

The model is for educational and portfolio use only. It should not be presented as a production decision system.

## Recommended recruiter pitch

> This is an interpretability-focused Decision Tree classification demo. I cleaned up a legacy ML notebook, identified leakage risk, rebuilt the training flow using a safer scikit-learn pipeline, and created a Streamlit demo that explains predictions through decision rules, confusion matrix, and tree visualization.
