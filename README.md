#  Object Detection: Car VS Bike

## Repository Outline
Berikut adalah isi dari file yang ada di repository ini:

```
  /CarVSBikeClassification
  |
  ├── MainNotebook.ipynb = Notebook utama untuk membuat model object detection menggunakan TensorFLow
  ├── inference_file.ipynb = Notebook untuk menguji model yang telah dibuat di Notebook utama.
  ├── url.txt = link website untuk dataset, model dan deployment.
  ├── README.md = Penjelasan gambaran umum proyek.
  ├── /deployment = source code yang digunakan untuk deploy model ke website streamlit
        ├── app.py
        ├── eda.py
        ├── prediction.py
        └── requirements.txt
```

## Problem Background
Teknologi computer vision telah berkembang pesat dan memiliki penerapan luas dalam kehidupan sehari-hari, salah duanya adalah otomotif dan transportasi. Salah satu penerapannya adalah dalam sistem identifikasi kendaraan untuk pengelolaan lalu lintas dan otomatisasi kendaraan. Dataset berisikan kumpulan gambar mobil dan sepeda motor yang digunakan untuk melatih model machine learning dalam membedakan kedua jenis kendaraan. Proyek ini bertujuan untuk membangun model klasifikasi berbasis computer vision yang dapat mengenali mobil dan sepeda motor.

## Project Output
Output dari hasil proyek ini adalah sebagai berikut:
- Prediksi deteksi objek kendaraan berdasarkan target label (motor atau mobil)
- Kesimpulan dari analisis yang telah dilakukan
- Model yang telah dirancang menggunakan TensorFlow.

## Data
- **Sumber data**: https://www.kaggle.com/datasets/utkarshsaxenadn/car-vs-bike-classification-dataset

## Method
Metode yang digunakan dalam proyek ini adalah sebagai berikut:

1. **Exploratory Data Analysis (EDA)**  
   - Visualisasi sampel gambar dari masing-masing kelas (Bike dan Car).
   - Pengecekan distribusi data, jumlah gambar per kelas, dan range nilai pixel.
   - Analisis keseimbangan data dan proporsi train/validation.

2. **Data Preprocessing & Augmentation**  
   - Normalisasi gambar dengan membagi nilai pixel dengan 255.
   - Augmentasi data pada training set menggunakan rotasi, pergeseran, shear, zoom, perubahan brightness, dan horizontal flip untuk meningkatkan variasi data dan mencegah overfitting.
   - Pembagian data menjadi training (80%) dan validation (20%).

3. **Model Development**  
   - Pembuatan model Artificial Neural Network (ANN) berbasis Convolutional Neural Network (CNN) menggunakan TensorFlow Keras.
   - Model pertama menggunakan beberapa layer Conv2D, MaxPooling, dan Dense.
   - Model improvement menambahkan BatchNormalization dan Dropout untuk meningkatkan generalisasi dan mengurangi overfitting.

4. **Model Training & Evaluation**  
   - Training model pada data yang telah diaugmentasi.
   - Evaluasi performa model menggunakan metrik akurasi, loss, confusion matrix, dan classification report (precision, recall, F1-score).
   - Visualisasi grafik akurasi dan loss selama training.

5. **Model Saving**  
   - Menyimpan model hasil training dalam format .h5 untuk digunakan pada proses inferensi dan deployment.

6. **Kesimpulan & Rekomendasi**  
   - Analisis hasil evaluasi model dan memberikan rekomendasi untuk peningkatan performa di masa mendatang (misal: transfer learning, tuning hyperparameter, arsitektur CNN yang lebih kompleks).

## Stacks
- **Python**: Bahasa pemrograman utama untuk seluruh proses analisis dan pengembangan model.
- **TensorFlow & Keras**: Framework deep learning untuk membangun dan melatih model Convolutional Neural Network (CNN).
- **Scikit-learn**: Untuk evaluasi model, seperti confusion matrix dan classification report.
- **Matplotlib & Seaborn**: Untuk visualisasi data, distribusi kelas, dan grafik hasil training.
- **Pandas & NumPy**: Untuk manipulasi data dan operasi numerik.
- **ImageDataGenerator (Keras)**: Untuk preprocessing dan augmentasi gambar.

## Reference
- Dataset: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset
