"""
Nama    :Moch. Yussar Rizky
NIM     :2403195
Kelas   :RPL 1C
"""

bola= ("basket", "sepak", "voli", "badminton", "pingpong")

#metode append
bola= ("basket", "sepak", "voli", "badminton", "pingpong")
olahraga= list(bola)

olahraga.append("tenis")
bola=tuple(olahraga)

print(bola)


#metode insert
bola= ("basket", "sepak", "voli", "badminton", "pingpong")
olahraga= list(bola)

olahraga.insert(2,"kasti")
bola=tuple(olahraga)

print(bola)


#metode pop
bola= ("basket", "sepak", "voli", "badminton", "pingpong")
olahraga= list(bola)

olahraga.pop(2)
bola=tuple(olahraga)

print(bola)