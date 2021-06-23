szamok = []

szam = None

while szam != 0:
    szam = int(input("Írj be egy pozitív szamot! "))
    if szam:
        szamok.append(szam)
szamok.reverse()
print(szamok)