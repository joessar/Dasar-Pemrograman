"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

Nama = input("Masukkan nama:")

Gender= input("Pilih jenis kelamin\nX(Laki-laki)\nY(Perempuan)\n")
Umur = int(input("Masukkan umur:"))
Tinggi = int(input("Masukkan tinggi badan:"))
iq = int(input("Masukkan iq:"))

if Gender == "x" and "X":
    if Umur >=18 and Umur <=25:
        if Tinggi >=175:           
            if iq >=130:
                print("Kamu lulus sebagai model")
            else:
                print("kamu Tidak Lulus")
        else:
            print("kamu Tidak Lulus")
    else:
       print("kamu Tidak Lulus")
else:
    if Umur >=18 and Umur <=25:
        if Tinggi >=170:
            if iq >=130:
                print("Kamu lulus")
            else:
                print("kamu tidak lulus")
        else:
            print("kamu Tidak Lulus")
    else:
        print("kamu Tidak Lulus")