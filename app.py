"""
Dashboard Analisis Penjualan - Streamlit App
----------------------------------------------
Cara jalankan:
    streamlit run app.py

Lalu browser akan terbuka otomatis ke http://localhost:8501
"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ---- Konfigurasi halaman ----
st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

st.title("📊 Dashboard Analisis Penjualan")
st.caption("Contoh project data analysis sederhana menggunakan Python & Streamlit")


# ---- Load data ----
@st.cache_data
def load_data():
    df = pd.read_csv("data_penjualan.csv", parse_dates=["tanggal"])
    df["total"] = df["jumlah"] * df["harga_satuan"]
    return df


df = load_data()

# ---- Sidebar filter ----
st.sidebar.header("Filter")
produk_list = ["Semua"] + sorted(df["produk"].unique().tolist())
pilihan_produk = st.sidebar.selectbox("Pilih Produk", produk_list)

if pilihan_produk != "Semua":
    df_filtered = df[df["produk"] == pilihan_produk]
else:
    df_filtered = df

# ---- Ringkasan angka (metric cards) ----
col1, col2, col3 = st.columns(3)
col1.metric("Total Penjualan", f"Rp {df_filtered['total'].sum():,.0f}")
col2.metric("Jumlah Transaksi", f"{len(df_filtered)}")
col3.metric("Rata-rata/Transaksi", f"Rp {df_filtered['total'].mean():,.0f}")

st.divider()

# ---- Dua kolom grafik ----
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Produk Terlaris (by Omzet)")
    ranking = df.groupby("produk")["total"].sum().sort_values(ascending=False)
    st.bar_chart(ranking)

with col_b:
    st.subheader("Tren Penjualan Bulanan")
    tren = df_filtered.set_index("tanggal").resample("ME")["total"].sum()
    st.line_chart(tren)

st.divider()

# ---- Tabel data mentah ----
st.subheader("Data Transaksi")
st.dataframe(df_filtered.sort_values("tanggal", ascending=False), use_container_width=True)
