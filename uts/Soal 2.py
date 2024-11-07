#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

angka = []
genap = 0
ganjil = 0

while angka >=0:
    angka = int(input("Input bilangan : "))

    if angka <0:
        break

    hitung = angka %2 

    if hitung == 0:
        genap += angka
    else:
        ganjil += angka
        
print(f"Jumlah bilangan genap : {genap}")
print(f"Jumlah bilangan ganjil : {ganjil}")