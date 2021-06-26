mese_file = open("adat.txt", "r")
other5_file = open("file5other.txt", "w")

for sor in mese_file:
    print(sor.strip(), file=other5_file)