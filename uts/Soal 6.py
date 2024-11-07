#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

N = int(input("Masukkan nilai N = "))
p = int(input(f"Masukkan bilang ke-{N -N +1} = "))
x = (p**0.5+1)
while N >0:
    for i in range(2,x):
        if x%i == 0:
        return False
    return True
if N ==0:
    print(f"Jumlah bilangan prima adalah : {}")
        
