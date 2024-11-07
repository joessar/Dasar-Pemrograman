#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

username = "loginUTS"
password = "rpl2024"

kesempatan = 0
batas_kesempatan = 3

print("Silahkan login")
while kesempatan < batas_kesempatan:
    pengguna = str(input("Username:"))
    if pengguna == username:
        kata_sandi = str(input("Password:"))
        if kata_sandi == password:
            print("Selamat datang di aplikasi prodi RPL.")
            break
        else:
            kesempatan +=1
            print("Login Salah! Kesempatan Anda 2x kali lagi.")
    else:
        kesempatan +=1
        print("Login Salah! Kesempatan Anda 2x kali lagi.")
if kesempatan == batas_kesempatan:
    print("Anda tidak diperkenankan mengakses aplikasi ini.")
            
            