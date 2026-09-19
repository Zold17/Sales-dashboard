# 📊 Dashboard Analisis Data Penjualan

Project analisis data penjualan sederhana menggunakan Python. Project ini dibuat sebagai portofolio pembelajaran dari nol menuju Software Engineering, dengan latar belakang sertifikasi Data Analyst.

## Fitur

- Membaca dan mengolah data penjualan dari file CSV
- Menghitung ringkasan penjualan (total, jumlah transaksi, rata-rata)
- Menentukan produk terlaris berdasarkan omzet
- Menampilkan tren penjualan bulanan
- Visualisasi data dalam bentuk grafik (bar chart & line chart)
- Dashboard interaktif berbasis web menggunakan Streamlit

## Tech Stack

- **Python 3**
- **Pandas** — pengolahan data
- **Matplotlib** — visualisasi grafik (versi script)
- **Streamlit** — dashboard web interaktif (versi app)

## Struktur Project

## Cara Menjalankan

1. Install dependencies:
2. Jalankan versi command-line (menghasilkan ringkasan di terminal + file grafik PNG):
3. Atau jalankan versi web interaktif:
      Browser akan otomatis terbuka di `http://localhost:8501`

## Data

Dataset dalam project ini adalah **data dummy** yang dibuat untuk simulasi, berisi transaksi penjualan produk berbahan kayu (meja, kursi, lemari, rak) selama 6 bulan. Untuk penggunaan nyata, tinggal ganti `data_penjualan.csv` dengan data asli — pastikan formatnya sama (kolom: `tanggal`, `produk`, `jumlah`, `harga_satuan`).

## Pengembangan Selanjutnya (Ide)

- Tambah filter berdasarkan rentang tanggal
- Tambah prediksi penjualan sederhana (forecasting)
- Deploy ke Streamlit Cloud agar bisa diakses publik lewat link
- Ganti sumber data ke database (SQL) alih-alih CSV

---

*Project ini dibuat sebagai bagian dari proses belajar Software Engineering, menggabungkan pengalaman di bidang Data Analyst dengan skill programming yang baru dipelajari.*
