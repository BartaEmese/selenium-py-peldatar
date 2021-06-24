szamok = []

szam = 0

while szam < 10:
    szam = int(input("Kérek egy számot! "))
    if szam < 10:
        szamok.append(szam)

print(sum(szamok))
