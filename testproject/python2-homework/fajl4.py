mese_lista = []

mese_file = open("adat.txt")
for sor in mese_file:
    mese_lista.append(sor)
print(mese_lista)

other2_file = open("fajl4other.txt", "w")
for s in mese_lista:
    print(s.strip(), file=other2_file)

