"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

nilai = int(input("Masukkan nilai:"))

if 90 <= nilai <= 100:
    print("Maka nilainya A")
elif 80 <= nilai < 90:
    print("maka nilainya B") 
elif 70 <= nilai <80:
    print("Maka nilainya C")
elif 0 <= nilai <70:
    print("Maka nilainya D")
else:
    print("Tidak dapat dinilai")
