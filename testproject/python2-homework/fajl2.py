mese_lista = []

mese_file = open("adat.txt", "r")
for sor in mese_file:
    mese_lista.append(sor.strip())
print(mese_lista)

