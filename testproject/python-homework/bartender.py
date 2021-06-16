age = int(input("Hány éves vagy? "))
drink = input("Mit szeretnél inni?: ")

if drink == "kóla":
    if age <= 60:
        print("Parancsoljon a kólája!")
    elif age > 60:
        print("A koffein megemeli a vérnyomást")


elif drink == "sör":
    if age >= 18:
        print("Parancsoljon a söre!")
    elif age < 18:
        print("Sajnos nem szolgálhatjuk ki!")
else:
    print("Csak sört és kólát tudunk adni")



