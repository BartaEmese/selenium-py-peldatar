# with open("adat.txt", "w") as file:
    # file.write("Egyszer\nvolt,\nhol\nnem\nvolt,\nvolt\negyszer\negy\nember.")

mese_file = open("adat.txt", "r")
for sor in mese_file:
    print(sor.strip() + " ", end=(""))
