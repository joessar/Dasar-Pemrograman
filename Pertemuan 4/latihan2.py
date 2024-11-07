"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

students= {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Sciense",
    "Eva": "Mathematics"
}

prodi = list(students.values())    #mengubah data dictionary menjadi list dan bisa dibaca value nya


a = prodi.count("Computer Science")
b = prodi.count("Mathematics")     #menghitung banyaknya value
c = prodi.count("Physics") 

print(f"pilih\n CS\n MTK\n PHY\n selesai\n")    #menampilkan menu dan untuk menginput data


x = ""
while x != "selesai":                         #sistem akan berhenti ketika user menginput "selesai"
    x = input("> ").lower()
    if x == "CS".lower():                            #kondisi ketika user menginput "cs"
        print(f"prodi Computer Science sebanyak {a}")
    elif x == "MTK".lower():                    #kondisi ketika user menginput "mtk"
        print(f"prodi Mathematics sebanyak {b}")
    elif x == "PHY".lower():                #kondisi ketika user menginput "phy"
        print(f"prodi Physics sebanyak {c}")
    elif x == "selesai".lower():   #kondisi ketika user menginput "selesai"
        print("Udahan ya")
    else:                                #kondisi ketika user menginput selain yang muncul pada menu
        print("pilih yang bener yaa <3")
