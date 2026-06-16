# Local Setup Guide

This guide explains how to run the Decision Tree Streamlit demo locally.

## 1. Recommended folder structure

```text
06_decision-tree-classification/
├── app.py
├── requirements.txt
├── README_DEPLOY.md
└── data/
    └── adult_dataset.csv
```

The dataset file must be available at:

```text
data/adult_dataset.csv
```

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit app

```bash
streamlit run app.py
```

The app should open in your browser. If it does not open automatically, copy the local URL shown in the terminal.

## 5. Expected app features

The local demo should display:

- Project title and audit note
- Toggle to exclude sensitive attributes
- Decision Tree max depth slider
- Input form in the sidebar
- Predicted class
- Prediction probability table
- Decision path explanation
- Confusion matrix
- Classification report
- Tree preview visualization
- Dataset notes

## 6. Common issues

### Dataset not found

Make sure the CSV file exists here:

```text
data/adult_dataset.csv
```

### Streamlit command not found

Activate your virtual environment and reinstall dependencies:

```bash
pip install -r requirements.txt
```

### OneHotEncoder sparse_output error

The provided `app.py` includes compatibility handling for older and newer scikit-learn versions. If you modified the app, make sure the encoder creation still supports your installed scikit-learn version.

## 7. Local acceptance checklist

```text
[ ] App starts without error.
[ ] Dataset loads from data/adult_dataset.csv.
[ ] User can submit input form.
[ ] Predicted class appears.
[ ] Prediction probability appears.
[ ] Decision path explanation appears.
[ ] Confusion matrix renders.
[ ] Classification report renders.
[ ] Tree preview renders.
[ ] No target-derived cluster feature is used.
```
