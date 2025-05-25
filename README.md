# 🫀 Heart Attack Prediction Project - Arief Setiawan

## 📌 Domain Proyek

Penyakit jantung merupakan penyebab utama kematian secara global. Deteksi dini sangat penting agar penanganan dapat dilakukan secara cepat dan tepat. Teknologi machine learning memberikan potensi besar untuk membantu tenaga medis dalam memprediksi risiko serangan jantung secara efisien.

**Referensi:**  
[World Health Organization - Cardiovascular Diseases (2023)](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

---

## 🎯 Business Understanding

### Problem Statements
- Bagaimana memprediksi risiko serangan jantung berdasarkan data medis pasien?
- Fitur apa yang paling berkontribusi terhadap prediksi serangan jantung?

### Goals
- Mengembangkan model klasifikasi serangan jantung.
- Mengidentifikasi fitur paling penting dalam prediksi.

### Solution Statements
- Menggunakan dua algoritma: **Random Forest Classifier** dan **Logistic Regression**.
- Mengukur performa model dengan **Accuracy**, **F1-Score**, dan **ROC AUC**.
- Memilih model terbaik berdasarkan hasil evaluasi.

---

## 📊 Data Understanding

### Jumlah dan Kondisi Data
- Jumlah entri: **1319 baris**, **9 kolom**.
- **Missing value:** Tidak ditemukan.
- **Duplikat:** Tidak ada.
- **Outlier:** Terdeteksi pada `troponin` dan `glucose`, tidak dihapus karena bisa bernilai klinis.

### Tautan Dataset
- Kaggle: [Heart Disease Classification Dataset](https://www.kaggle.com/datasets/bharath011/heart-disease-classification-dataset)

### Uraian Fitur
| Fitur           | Deskripsi                                              |
|------------------|--------------------------------------------------------|
| `age`            | Usia pasien (tahun)                                    |
| `gender`         | Jenis kelamin (0: perempuan, 1: laki-laki)             |
| `impluse`        | Detak jantung                                          |
| `pressurehight`  | Tekanan darah sistolik                                 |
| `pressurelow`    | Tekanan darah diastolik                                |
| `glucose`        | Kadar gula darah                                       |
| `kcm`            | Kadar kalium dalam darah                               |
| `troponin`       | Indikator kerusakan otot jantung                       |
| `class`          | Target (1 = serangan jantung, 0 = tidak)               |

---

## 🧹 Data Preparation

### Pemilihan Fitur dan Target
- **Target:** `class`
- **Fitur:** Semua kolom selain `class`

### Tahapan Pemrosesan Data
1. **Label Encoding**
   - `class` diubah ke numerik: `positive` → `1`, `negative` → `0`.
2. **Cek duplikat dan missing value**
   - Tidak ditemukan duplikat atau missing value.
3. **Normalisasi**
   - Semua fitur numerik dinormalisasi menggunakan `StandardScaler`.
4. **Split data**
   - Proporsi 80% training dan 20% testing menggunakan `train_test_split`.

---

## 🤖 Modeling

### Model 1: Random Forest Classifier

#### Cara Kerja
Random Forest adalah algoritma ansambel yang membentuk banyak decision tree dari subset data acak. Hasil akhir dipilih berdasarkan mayoritas voting dari semua pohon.

#### Parameter
- `n_estimators=100` (default)
- `max_depth=None` (default)
- `random_state=42`

#### (Opsional) Kelebihan/Kekurangan
- ✅ Akurat, cocok untuk data kompleks
- ❌ Waktu inferensi lebih lama

---

### Model 2: Logistic Regression

#### Cara Kerja
Logistic Regression merupakan model linier yang menggunakan fungsi sigmoid untuk memetakan nilai input ke dalam probabilitas antara 0 dan 1.

#### Parameter
- `penalty='l2'` (default)
- `solver='lbfgs'`
- `random_state=42`

#### (Opsional) Kelebihan/Kekurangan
- ✅ Cepat dan mudah diinterpretasi
- ❌ Kurang efektif untuk pola non-linier

---

## 📈 Evaluation

### Metrik Evaluasi
- **Accuracy**: proporsi prediksi yang benar.
- **F1-Score**: rata-rata harmonis dari precision dan recall, cocok untuk data tidak seimbang.
- **ROC AUC**: area di bawah kurva ROC, menunjukkan kemampuan model membedakan kelas.

### Hasil Evaluasi

| Model               | Accuracy | F1-Score (Positif) | ROC AUC |
|--------------------|----------|--------------------|---------|
| Random Forest       | 98.1%    | 0.985              | 0.991   |
| Logistic Regression | 79.9%    | 0.842              | 0.884   |

### Visualisasi
- ![Confusion Matrix RF](gambar/confusion_randomforest.png)
- ![Confusion Matrix LR](gambar/confusion_logistic.png)
- ![ROC Curve](gambar/roc.png)
- ![Feature Importance](gambar/feature_importance.png)

---

### Dampak ke Business Understanding

- **Problem terjawab:** Model dapat memprediksi risiko serangan jantung dengan akurasi tinggi.
- **Goals tercapai:** Model dan fitur penting berhasil diidentifikasi.
- **Solusi berdampak:** Random Forest terbukti menjadi solusi efektif dengan performa tinggi. Dapat diintegrasikan ke sistem klinis sebagai alat bantu diagnosis.

---

**Catatan:**  
Model ini dapat dikembangkan lebih lanjut menggunakan data klinis real dan sistem API/dasbor interaktif untuk tenaga medis.
