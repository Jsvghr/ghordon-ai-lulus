import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("🎓 Prediksi Kelulusan Siswa")
st.markdown("Masukkan data siswa untuk memprediksi apakah mereka **lulus** atau **tidak**.")

jam_belajar = st.slider("Jam Belajar per Hari", 0, 10, 3)
nilai_ujian = st.slider("Nilai Ujian Sebelumnya", 0, 100, 60)
kehadiran = st.slider("Kehadiran (%)", 0, 100, 80)

if st.button("Prediksi Sekarang"):
    input_data = np.array([[jam_belajar, nilai_ujian, kehadiran]])
    hasil = model.predict(input_data)[0]
    
    if hasil == 1:
        st.success("✅ Siswa diprediksi **LULUS**!")
    else:
        st.error("❌ Siswa diprediksi **TIDAK LULUS**.")
