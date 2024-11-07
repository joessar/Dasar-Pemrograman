

angka = 0
hitung = 0
list=[]
while True:
    hitung += angka
    angka = int(input("Masukkan angka:"))
    if angka <=0:
        break
    list.append(angka)

print(*list, sep="+")
print(f"= {hitung}")

