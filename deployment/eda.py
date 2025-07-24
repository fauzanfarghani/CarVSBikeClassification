import streamlit as st

def app():
    st.title("Exploratory Data Analysis: Car vs Bike Classification")
    # Show dataset info
    st.header("Dataset Overview")
    st.write("Dataset ini berisi gambar motor dan mobil yang digunakan untuk klasifikasi, berikut jumlah gambar per kelas: ")
    #tampilkan foto "datasetinfo.png"
    st.image("datasetinfo.png")

    # Visualize sample images per class
    st.header("1. Sample Images per Class")
    st.image("fotoeda1.png")
    st.write("\nVisualisasi contoh gambar dari masing-masing kelas (Car dan Bike) diambil dari batch data training. Tujuannya untuk memastikan data yang digunakan sudah sesuai, gambar dapat terbaca dengan baik, serta distribusi kelas sudah sesuai. hal ini juga dapat membantu model mengenali karakteristik visual dari masing-masing kategori nantinya.")

    # Show image shape and pixel range
    st.header("2. Image Shape and Pixel Range")
    st.image("fotoeda2.png")
    st.write("Pengecekan ukuran batch gambar dan range nilai pixel pada data training untuk memastikan gambar yang masuk ke model memiliki dimensi yang sesuai. Hal ini juga dapat memastikan tidak ada data error pada gambar yang bisa mengganggu proses training model.")
    st.write("Bentuk batch gambar: (32, 224, 224, 3) menunjukkan 32 gambar dengan ukuran 224x224 piksel dan 3 channel warna (RGB).")

    # Visualize validation images
    st.header("3. Sample Validation Images")
    st.image("fotoeda3.png")
    st.write("Berikut adalah sampel gambar yang digunakan untuk uji validasi dari dataset. Visualisasi sampel gambar dari data validation bertujuan untuk memastikan bahwa data validasi yang digunakan dalam proses evaluasi model sudah benar dan representatif. Dengan menampilkan beberapa gambar beserta label aslinya, kita dapat memverifikasi bahwa gambar-gambar tersebut telah terpisah dari data training dan labelnya sesuai.")

    # Distribution bar plot
    st.header("4. Data Distribution per Class")
    st.image("fotoeda4.png")
    st.write("Seperti yang sudah dijelaskan di data loading terkait proporsi train dan validation, berikut adalah visualisasi untuk menunjukkan bahwa data sudah seimbang dan terbagi berdasarkan porsi 80% Train dan 20% Validation.")