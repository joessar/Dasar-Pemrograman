"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

print(f"pilih\n Alice\n Bob\n Charlie\n ") #menampilkan menu dan untuk menginput data

nama = input("inputkan nama siswa:").capitalize() #menginput data auto formal
biodata = student_info.get(nama) #variabel baru berisikan data dari "student_info"

print(f"Umur {nama} adalah {biodata["age"]} dan Prodi nya adalah {biodata["major"]}")

