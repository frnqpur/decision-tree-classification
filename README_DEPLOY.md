# Decision Tree Interpretability Demo

Demo Streamlit ini dibuat untuk recruiter sebagai versi portfolio dari project **Decision Tree Classification**. Fokus utamanya bukan sekadar memprediksi income class, tetapi menunjukkan bagaimana Decision Tree mengambil keputusan melalui rule path, confusion matrix, dan visualisasi tree.

## Isi demo

- Input form sederhana untuk profil tabular.
- Prediksi income class: `<=50K` atau `>50K`.
- Prediction confidence dari `predict_proba`.
- Explanation sederhana berupa decision path/rule yang dilewati model.
- Confusion matrix dari test set.
- Classification report.
- Preview visual Decision Tree sampai 3 level pertama.
- Toggle untuk mengecualikan sensitive attributes: `race` dan `sex`.

## Catatan audit penting

Notebook lama menghasilkan akurasi 100% karena ada indikasi **target leakage**: fitur `cluster` dibuat dari target `Class`, lalu digunakan sebagai fitur model.

Demo ini tidak memakai fitur leakage tersebut. Model dilatih ulang dari dataset asli menggunakan pipeline scikit-learn:

```text
SimpleImputer -> OneHotEncoder -> DecisionTreeClassifier
```

Split data menggunakan:

```text
70% train / 30% test
stratify=y
```

Demo ini bersifat educational portfolio demo, bukan production decision system.

## Struktur file

```text
.
├── app.py
├── requirements.txt
├── README_DEPLOY.md
└── data/
    └── adult_dataset.csv
```

## Local setup

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependency:

```bash
pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
streamlit run app.py
```

Buka URL lokal yang ditampilkan Streamlit, biasanya:

```text
http://localhost:8501
```

## Deploy ke Streamlit Community Cloud

1. Buat repository GitHub, misalnya:

   ```text
   decision-tree-interpretability-demo
   ```

2. Upload file berikut ke root repository:

   ```text
   app.py
   requirements.txt
   README_DEPLOY.md
   data/adult_dataset.csv
   ```

3. Buka Streamlit Community Cloud.
4. Pilih **New app**.
5. Hubungkan ke repository GitHub.
6. Set main file path:

   ```text
   app.py
   ```

7. Deploy.

## Deploy ke Hugging Face Spaces

1. Buat Space baru.
2. Pilih SDK:

   ```text
   Streamlit
   ```

3. Upload file berikut:

   ```text
   app.py
   requirements.txt
   README_DEPLOY.md
   data/adult_dataset.csv
   ```

4. Hugging Face Spaces akan membaca `requirements.txt` dan menjalankan app Streamlit.

## Screenshot checklist untuk portfolio

Ambil screenshot berikut untuk website portfolio:

- Halaman utama demo.
- Input form di sidebar.
- Prediction result dan probability table.
- Decision path explanation.
- Confusion matrix.
- Classification report.
- Decision tree preview.
- Dataset notes/audit note.

## Recruiter positioning

Gunakan narasi berikut:

> Built an interpretable Decision Tree demo from a legacy income classification notebook, identified target leakage behind misleading perfect accuracy, and refactored the workflow into a clean scikit-learn pipeline with transparent prediction explanations.

Versi Indonesia:

> Membuat demo Decision Tree yang fokus pada interpretability, menemukan target leakage pada notebook lama, dan merapikan workflow menjadi pipeline scikit-learn yang lebih transparan untuk evaluasi dan portfolio.
