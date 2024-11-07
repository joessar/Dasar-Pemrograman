#Nama = Moch. Yussar Rizky
#Kelas = RPL 1C
#NIM = 2403195

jumlah_bebek = int(input("Masukkan jumlah bebek:"))
print("----------------")

while jumlah_bebek > 1:
    print(f"{jumlah_bebek} bebek kecil berenang \nMenyusuri sungai yang deras \nInduknya mencari kwek kwek kwek \nHanya {jumlah_bebek -1} ekor yang pulang")
    print("----------------")
    jumlah_bebek -=1
if jumlah_bebek == 1:
    print(f"{jumlah_bebek} bebek kecil berenang \nMenyusuri sungai yang deras \nInduknya mencari kwek kwek kwek \nDan semua bebek kecil pulang, aha!")
    