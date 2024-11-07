"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

jumlah_barang = int(input("masukan jumlah barangnya:"))

if (jumlah_barang <100):
    print(f"total harga barangnya adalah Rp.{jumlah_barang * 5000}")
elif (jumlah_barang >= 100 and jumlah_barang < 150):
    print(f"total harga barangnya adalah Rp.{jumlah_barang * 4000}")
elif (jumlah_barang >= 150):
    print(f"total harga barangnya adalah Rp.{jumlah_barang * 2500}")

