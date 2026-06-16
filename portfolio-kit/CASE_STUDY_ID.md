# Studi Kasus — Decision Tree Classification Explainability Demo

## Ringkasan

Project ini adalah demo machine learning berbasis Decision Tree untuk klasifikasi kelas pendapatan menggunakan dataset Adult Income. Fokus utama project bukan hanya membuat prediksi, tetapi menjelaskan bagaimana model mengambil keputusan melalui rule path, confusion matrix, classification report, dan visualisasi Decision Tree.

Project ini dikembangkan dari notebook lama yang sebelumnya berisi proses eksplorasi data, preprocessing, pelatihan model Decision Tree, evaluasi, dan visualisasi. Saat proses audit portfolio, ditemukan bahwa hasil akurasi sempurna pada notebook lama tidak layak diklaim karena ada indikasi target leakage dari fitur `cluster` yang dibuat berdasarkan target.

Karena itu, project ini diposisikan ulang sebagai **Decision Tree interpretability and evaluation demo**.

## Problem statement

Bagaimana membuat demo klasifikasi yang mudah dipahami recruiter, transparan secara evaluasi, dan mampu menjelaskan alasan prediksi model secara sederhana?

## Tujuan project

- Membuat demo klasifikasi berbasis Decision Tree.
- Menampilkan prediksi class `<=50K` atau `>50K`.
- Menampilkan probabilitas prediksi.
- Menjelaskan keputusan model melalui rule path.
- Menampilkan confusion matrix dan classification report.
- Menampilkan visualisasi Decision Tree.
- Menghindari target leakage dari notebook lama.
- Menyajikan project secara lebih profesional untuk portfolio.

## Dataset

Dataset yang digunakan adalah Adult Income dataset dari project asli.

Target:

```text
income_class
```

Kelas target:

```text
<=50K
>50K
```

Fitur utama:

```text
age, workclass, fnlwgt, education, education.num,
marital.status, occupation, relationship, race, sex,
capital.gain, capital.loss, hours.per.week, native.country
```

## Pendekatan teknis

Model dibuat menggunakan pipeline scikit-learn:

```text
1. Load dataset
2. Rename target column
3. Replace missing marker ? menjadi NaN
4. Split train/test dengan stratify
5. Imputasi fitur numerik menggunakan median
6. Imputasi fitur kategorikal menggunakan most frequent
7. One-hot encoding untuk fitur kategorikal
8. Train DecisionTreeClassifier
9. Evaluasi menggunakan confusion matrix dan classification report
10. Tampilkan rule path untuk input user
```

## Explainability

Decision Tree cocok untuk demo recruiter karena hasil prediksi dapat dijelaskan melalui urutan rule. Pada demo ini, setiap input user akan ditransformasikan oleh pipeline, lalu model menampilkan jalur keputusan yang dilewati sampai mencapai leaf node.

Contoh penjelasan:

```text
capital.gain <= threshold
education.num > threshold
hours.per.week <= threshold
```

Dengan cara ini, recruiter dapat melihat bahwa model tidak hanya mengeluarkan prediksi, tetapi juga memberikan alasan sederhana di balik prediksi tersebut.

## Evaluation

Evaluasi tidak hanya menggunakan accuracy. Demo juga menampilkan:

- Confusion matrix
- Precision
- Recall
- F1-score
- Support
- Prediction probability

Pendekatan ini lebih baik daripada hanya menampilkan satu angka akurasi, karena dataset memiliki distribusi class yang tidak sepenuhnya seimbang.

## Visualization

Visualisasi yang ditampilkan:

- Confusion matrix
- Decision Tree preview dengan kedalaman terbatas
- Prediction probability table
- Decision path table

Tree preview dibatasi pada level awal agar tetap mudah dibaca.

## Responsible ML note

Dataset mengandung atribut sensitif seperti `race` dan `sex`. Untuk demo portfolio, app menyediakan opsi untuk mengecualikan atribut sensitif dari input model.

Demo ini tidak boleh diposisikan sebagai sistem produksi untuk keputusan finansial, pekerjaan, kredit, atau eligibility. Project ini adalah demo edukasi untuk menunjukkan workflow classification, interpretability, dan evaluasi model.

## Hasil akhir

Project ini menghasilkan demo yang lebih kuat untuk portfolio karena menunjukkan:

- kemampuan membaca dan mengaudit notebook lama,
- kemampuan mendeteksi potensi data leakage,
- kemampuan membangun ulang pipeline yang lebih aman,
- kemampuan menjelaskan model Decision Tree,
- kemampuan menyajikan project ML dalam format yang mudah dipahami recruiter.

## Role saya

Dalam project ini, saya berperan dalam:

- review struktur project lama,
- identifikasi dataset dan target,
- analisis preprocessing dan evaluasi,
- deteksi leakage risk,
- perancangan ulang demo portfolio,
- penyusunan dokumentasi deployment,
- penyiapan narasi portfolio bilingual.
