# -*- coding: utf-8 -*-
"""klasifikasi_dengan_penjelasan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Cf3mQlFwbDCPYg7tFf3Ids7KwfGgQrmi

# Import Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

"""Penjelasan: Pada bagian ini, kita mengimpor berbagai library yang diperlukan untuk analisis data, visualisasi, dan pembuatan model machine learning. Library seperti pandas dan numpy digunakan untuk manipulasi data, matplotlib dan seaborn untuk visualisasi, serta scikit-learn untuk pemodelan dan evaluasi.

# Data Understanding
"""

# Load dataset
df = pd.read_csv('A:\DBS\mlTerapanAwal\HeartAttack.csv')

# Tampilkan informasi awal tentang dataset
df_info = df.info()
df_head = df.head()

df_info, df_head

"""Penjelasan: Pada bagian ini, dataset dimuat dari file CSV dan informasi dasar tentang dataset seperti tipe data dan beberapa baris awal ditampilkan untuk memahami struktur dan isi data.

# Data Preparation
"""

# Encode target class
df['class'] = df['class'].map({'negative': 0, 'positive': 1})

# Statistik ringkasan
summary_stats = df.describe()

# Visualisasi distribusi target
plt.figure(figsize=(5, 4))
sns.countplot(x='class', data=df)
plt.title('Distribusi Kelas (Target)')
plt.xlabel('Heart Attack (0 = Negative, 1 = Positive)')
plt.ylabel('Jumlah')
plt.tight_layout()
plt.show()

# Korelasi antar fitur
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Heatmap Korelasi Antar Fitur')
plt.tight_layout()
plt.show()

summary_stats

"""Penjelasan: Pada bagian ini, kita melakukan encoding pada variabel target agar menjadi numerik, melihat statistik ringkasan data, serta memvisualisasikan distribusi kelas target dan korelasi antar fitur untuk memahami hubungan antar variabel.

# Modeling
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay

# Fitur dan target
X = df.drop('class', axis=1)
y = df['class']

# Normalisasi fitur
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

"""Penjelasan: Pada bagian ini, kita memisahkan fitur dan target, melakukan normalisasi fitur menggunakan StandardScaler, dan membagi data menjadi data latih dan data uji dengan proporsi 80:20."""

# Model 1: Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)
rf_probs = rf.predict_proba(X_test)[:, 1]

# Model 2: Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)
lr_probs = lr.predict_proba(X_test)[:, 1]

"""Penjelasan: Pada bagian ini, kita melatih dua model klasifikasi, yaitu Random Forest dan Logistic Regression, kemudian melakukan prediksi kelas dan probabilitas pada data uji.

# Evaluasi
"""

# Visualisasi classification report dan confusion matrix
def plot_confusion_matrix(cm, title='Confusion Matrix'):
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title(title)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.tight_layout()
    plt.show()

# Tampilkan classification report sebagai teks
print("Random Forest Classification Report:")
print(classification_report(y_test, rf_preds))

print("Logistic Regression Classification Report:")
print(classification_report(y_test, lr_preds))

"""Penjelasan: Fungsi untuk memvisualisasikan confusion matrix dibuat, dan classification report dari kedua model ditampilkan untuk mengevaluasi performa model."""

# Evaluasi
rf_auc = roc_auc_score(y_test, rf_probs)
lr_auc = roc_auc_score(y_test, lr_probs)

# Visualisasi kurva ROC
plt.figure(figsize=(8, 6))
RocCurveDisplay.from_estimator(rf, X_test, y_test, name="Random Forest", ax=plt.gca())
RocCurveDisplay.from_estimator(lr, X_test, y_test, name="Logistic Regression", ax=plt.gca())
plt.title("ROC Curve Comparison")
plt.grid(True)
plt.tight_layout()
plt.show()

"""Penjelasan: Pada bagian ini, dilakukan evaluasi model menggunakan ROC AUC dan visualisasi kurva ROC untuk membandingkan performa kedua model."""

# Confusion matrices
rf_cm = confusion_matrix(y_test, rf_preds)
lr_cm = confusion_matrix(y_test, lr_preds)

plot_confusion_matrix(rf_cm, "Confusion Matrix - Random Forest")
plot_confusion_matrix(lr_cm, "Confusion Matrix - Logistic Regression")

"""Penjelasan: Confusion matrix dari kedua model divisualisasikan untuk melihat detail prediksi benar dan salah pada data uji."""

# Ambil feature importance dari model Random Forest
importances = rf.feature_importances_
feature_names = X.columns

# Buat DataFrame dan urutkan
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Visualisasi
plt.figure(figsize=(8, 5))
sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
plt.title('Feature Importance - Random Forest')
plt.tight_layout()
plt.show()

importance_df

"""Penjelasan: Pada bagian terakhir, kita mengambil dan memvisualisasikan pentingnya fitur dari model Random Forest untuk mengetahui fitur mana yang paling berpengaruh dalam prediksi."""