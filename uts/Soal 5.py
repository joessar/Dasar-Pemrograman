#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

angka = int(input("Input bilangan ; "))
besar = angka
x = 0
total = 0

while x < 3:
    angka = int(input("input bilangan : "))

    if angka > besar:
        total += angka
        x = 0
        besar = angka
    elif angka < besar:
        x +=1
        besar = angka
        pass
    if angka < 0:
        print(f"Hasil penjumlahan nilai yang membesar : {total}")
