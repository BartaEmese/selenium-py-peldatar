age = int(input("Hány éves vagy? "))
drink = input("Mit szeretnél inni?: ")

if drink == "kóla":
    if age <= 60:
        print("Parancsolj a kólád!")
    elif age > 60:
        print("A koffein megemeli a vérnyomást!")


elif drink == "sör":
    if age >= 18:
        print("Parancsolj a söröd!")
    elif age < 18:
        print("Sajnos nem szolgálhatjuk ki!")
else:
    print("Csak sört és kólát tudunk adni")



