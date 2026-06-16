# Security Cleanup Checklist

Use this checklist before uploading the project to GitHub, Streamlit Cloud, Hugging Face Spaces, LinkedIn, or a personal website.

## Files to check before publishing

```text
[ ] app.py
[ ] requirements.txt
[ ] README.md
[ ] README_DEPLOY.md
[ ] data/adult_dataset.csv
[ ] screenshots/
[ ] notebook files
[ ] exported HTML files
[ ] PDF files
```

## Do not upload these files

```text
[ ] .env
[ ] credentials.json
[ ] API keys
[ ] access tokens
[ ] private database files
[ ] private reports
[ ] raw confidential PDFs
[ ] local virtual environment folders
[ ] __pycache__ folders
[ ] .DS_Store
[ ] personal notes not intended for portfolio
```

## Recommended .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
.venv/
venv/
env/

# Environment variables
.env
.env.*

# Jupyter
.ipynb_checkpoints/

# OS files
.DS_Store
Thumbs.db

# Local outputs
outputs/
*.log

# Optional model artifacts
*.pkl
*.joblib
```

## Dataset safety

Before publishing `adult_dataset.csv`, confirm that:

```text
[ ] Dataset is allowed for public educational use.
[ ] No private company data is included.
[ ] No internal user/customer data is included.
[ ] No credentials or hidden columns are included.
[ ] You understand the dataset source and usage limitations.
```

## PDF safety

The original project includes a PDF report. Before uploading any PDF:

```text
[ ] Check author metadata.
[ ] Remove private links if needed.
[ ] Remove personal phone/address if present.
[ ] Remove internal/private project notes.
[ ] Export a sanitized version if you want to publish it.
```

## Notebook safety

Before publishing notebooks:

```text
[ ] Remove Google Drive personal paths.
[ ] Remove local machine paths.
[ ] Remove output cells that expose private folders.
[ ] Remove tokens or credentials.
[ ] Add markdown explanation for important steps.
[ ] Clearly mark original vs refactored notebook.
```

## Model safety

```text
[ ] Do not claim the model is production-ready.
[ ] Do not claim 100% accuracy.
[ ] Do not use target-derived features.
[ ] Do not use the old cluster feature as model input.
[ ] Add disclaimer for educational use.
[ ] Add note about sensitive attributes.
```

## Final publish checklist

```text
[ ] App runs locally.
[ ] README explains setup and limitations.
[ ] Deployment instructions are included.
[ ] Screenshots do not reveal private paths.
[ ] Sensitive files are excluded.
[ ] GitHub repo is clean.
[ ] Live demo URL works.
[ ] Portfolio page links to GitHub and demo.
```
