"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

nilai= [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
nilai.sort()
nilai.reverse()

nilaimax= max(nilai)
nilaimin= min(nilai)
nilaimean= sum(nilai)/len(nilai)

print(f"nilai maksimumnya adalah= {nilaimax}")
print(f"nilai minimumnya adalah= {nilaimin}")
print(f"nilai rata-ratanya adalah= {nilaimean}")
print(f"nilai terbesar kedua adalah= {nilai[1]}") 