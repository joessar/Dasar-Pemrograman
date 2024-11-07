#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

NIM = int(input("Masukkan 3 digit terakhir NIM : "))

while True:
    if NIM in range(0,51):
        if NIM %2 == 0:
            print("Silahkan masuk ke kelas K2")
            break
        else:
            print("Silahkan maasuk ke kelas K1")
            break
    elif NIM in range(51,101):
        if NIM %2 == 0:
            print("Silahkan masuk ke kelas K4")
            break
        else:
            print("Silahkan maasuk ke kelas K3")
            break
    elif NIM in range(100,150):
        if NIM %2 == 0:
            print("Silahkan masuk ke kelas K6")
            break
        else:
            print("Silahkan maasuk ke kelas K5")
            break
    elif NIM >= 151:
        if NIM %2 == 0:
            print("Silahkan masuk ke kelas K8")
            break
        else:
            print("Silahkan maasuk ke kelas K7")
            break