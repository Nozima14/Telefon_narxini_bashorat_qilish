import streamlit as st
import pickle
import numpy as np

# Load the model
with open("telefonmodel.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telefon Narxini Bashorat Qilish")

# Input form
st.header("Telefon parametrlarini kiriting")
sale = st.number_input("Sale (%)", min_value=0, max_value=100)
weight = st.number_input("Og'irlik (g)", min_value=50, max_value=500)
resoloution = st.selectbox("Ekran Ruxsatnomasi", options=[720, 1080, 1440, 2160])
ppi = st.number_input("PPI", min_value=100, max_value=600)
cpu_core = st.number_input("CPU Yadrolar soni", min_value=1, max_value=16)
cpu_freq = st.number_input("CPU Chastotasi (GHz)", min_value=1.0, max_value=5.0)
internal_mem = st.number_input("Ichki Xotira (GB)", min_value=8, max_value=1024)
ram = st.number_input("RAM (GB)", min_value=1, max_value=64)
rear_cam = st.number_input("Orqa Kamera (MP)", min_value=2, max_value=200)
front_cam = st.number_input("Old Kamera (MP)", min_value=2, max_value=40)
battery = st.number_input("Batareya sig'imi (mAh)", min_value=1000, max_value=8000)
thickness = st.number_input("Qalinlik (mm)", min_value=4.0, max_value=12.0)
lifespan = st.number_input("Yaroqlilik muddati (yil)", min_value=1, max_value=10)
year = st.number_input("Ishlab chiqarilgan yili", min_value=2010, max_value=2025)
condition = st.selectbox("Telefon holati", options=["yangi", "ishlatilgan", "ta'mirlangan"])

# Map categorical data
condition_map = {"yangi": 1, "ishlatilgan": 0.5, "ta'mirlangan": 0.3}
condition_value = condition_map[condition]

# Make prediction
features = np.array([[sale, weight, resoloution, ppi, cpu_core, cpu_freq, internal_mem,
                      ram, rear_cam, front_cam, battery, thickness, lifespan, year, condition_value]])
predicted_price = model.predict(features)

st.subheader(f"Telefon Narxi Bashorati: {predicted_price[0]:,.2f} dollar")



