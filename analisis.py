"""
Script Analisis Data Penjualan
--------------------------------
Membaca data penjualan dari CSV, lalu menghitung beberapa statistik dasar:
- Total penjualan
- Produk terlaris
- Tren penjualan bulanan

Cara jalankan:
    python analisis.py
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(path="data_penjualan.csv"):
    """Membaca file CSV dan menambahkan kolom total penjualan per transaksi."""
    df = pd.read_csv(path, parse_dates=["tanggal"])
    df["total"] = df["jumlah"] * df["harga_satuan"]
    return df


def ringkasan_umum(df):
    """Menampilkan ringkasan angka-angka penting."""
    total_penjualan = df["total"].sum()
    total_transaksi = len(df)
    rata_rata_transaksi = df["total"].mean()

    print("=" * 40)
    print("RINGKASAN PENJUALAN")
    print("=" * 40)
    print(f"Total Penjualan     : Rp {total_penjualan:,.0f}")
    print(f"Jumlah Transaksi    : {total_transaksi}")
    print(f"Rata-rata/Transaksi : Rp {rata_rata_transaksi:,.0f}")
    print()


def produk_terlaris(df, top_n=5):
    """Menampilkan produk dengan penjualan tertinggi (berdasarkan total omzet)."""
    ranking = (
        df.groupby("produk")["total"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )
    print("=" * 40)
    print(f"TOP {top_n} PRODUK TERLARIS (by omzet)")
    print("=" * 40)
    for i, (produk, total) in enumerate(ranking.items(), start=1):
        print(f"{i}. {produk:<15} Rp {total:,.0f}")
    print()
    return ranking


def tren_bulanan(df):
    """Menghitung total penjualan per bulan."""
    df_bulanan = df.set_index("tanggal").resample("ME")["total"].sum()
    print("=" * 40)
    print("TREN PENJUALAN BULANAN")
    print("=" * 40)
    for tanggal, total in df_bulanan.items():
        print(f"{tanggal.strftime('%B %Y'):<15} Rp {total:,.0f}")
    print()
    return df_bulanan


def buat_grafik(ranking_produk, tren_bulanan_data):
    """Membuat dan menyimpan dua grafik: produk terlaris & tren bulanan."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Grafik 1: Produk terlaris
    axes[0].barh(ranking_produk.index[::-1], ranking_produk.values[::-1], color="#4C72B0")
    axes[0].set_title("Produk Terlaris (by Omzet)")
    axes[0].set_xlabel("Total Penjualan (Rp)")

    # Grafik 2: Tren bulanan
    axes[1].plot(
        tren_bulanan_data.index, tren_bulanan_data.values,
        marker="o", color="#DD8452"
    )
    axes[1].set_title("Tren Penjualan Bulanan")
    axes[1].set_xlabel("Bulan")
    axes[1].set_ylabel("Total Penjualan (Rp)")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("hasil_analisis.png", dpi=150)
    print("Grafik disimpan sebagai 'hasil_analisis.png'")


def main():
    df = load_data()
    ringkasan_umum(df)
    ranking = produk_terlaris(df)
    tren = tren_bulanan(df)
    buat_grafik(ranking, tren)


if __name__ == "__main__":
    main()
