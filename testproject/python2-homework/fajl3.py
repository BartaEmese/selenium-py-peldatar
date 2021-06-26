mese_lista = []

mese_file = open("adat.txt", "r")
for sor in mese_file:
    mese_lista.append(sor.strip())
print(mese_lista)

other_file = open("fajl3other.txt", "w")
for sor in mese_lista:
    print(sor, end=" ", file=other_file)
