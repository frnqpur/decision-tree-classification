# Streamlit Deployment Guide

This guide explains how to deploy the Decision Tree interpretability demo to Streamlit Community Cloud or Hugging Face Spaces.

## Required files

The deployment folder should include:

```text
app.py
requirements.txt
README_DEPLOY.md
data/adult_dataset.csv
```

Optional but recommended:

```text
README.md
screenshots/
```

## Deployment option 1 — Streamlit Community Cloud

### 1. Push project to GitHub

Recommended repository structure:

```text
06_decision-tree-classification/
├── app.py
├── requirements.txt
├── README.md
├── README_DEPLOY.md
└── data/
    └── adult_dataset.csv
```

### 2. Create a new Streamlit app

Use the GitHub repository as the source.

Main file path:

```text
app.py
```

### 3. Deploy

Streamlit will install packages from:

```text
requirements.txt
```

### 4. Test the live app

After deployment, check:

```text
[ ] App loads successfully.
[ ] Dataset is available.
[ ] Input form works.
[ ] Prediction works.
[ ] Confusion matrix renders.
[ ] Decision tree preview renders.
```

## Deployment option 2 — Hugging Face Spaces

### 1. Create a new Space

Recommended SDK:

```text
Streamlit
```

### 2. Upload project files

Upload:

```text
app.py
requirements.txt
data/adult_dataset.csv
README.md
```

### 3. Confirm file paths

The app expects the dataset at:

```text
data/adult_dataset.csv
```

Do not rename the dataset unless you also update `DATA_PATH` in `app.py`.

### 4. Wait for build

Hugging Face Spaces will install dependencies from `requirements.txt` and run the Streamlit app.

## Deployment notes

### Do not deploy sensitive files

Do not upload:

```text
.env
credentials.json
API keys
tokens
private notes
raw confidential reports
```

### Dataset note

Only deploy the dataset if it is allowed for public portfolio use. If you are unsure, provide a dataset download instruction instead of uploading the CSV.

### Model note

The app trains the model at runtime from the dataset. This keeps the demo simple and avoids shipping a pickle file. For larger projects, a saved model artifact can be used, but it should be regenerated from a clean pipeline.

## Production disclaimer

This demo is for portfolio and educational purposes only. It should not be presented as a production system for financial, employment, or eligibility decisions.
