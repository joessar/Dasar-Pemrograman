"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

#Ganti item dengan nama "ceri" menjadi "cherry"
buah[2] = "cherry"
print(buah)

#Tambahkan item dengan nama dan indeks sesuai user
inputbuah= input("masukan nama buah yang ingin dimasukan=")
inputindeks= int(input("masukan indeks yang ingin ditambahkan="))
buah.insert(inputindeks,inputbuah)
print(buah)

#Urutkan item pada list sesuai dengan abdjadnya
buah.sort()
print(buah)