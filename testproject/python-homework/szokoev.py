# Még nincs kész.

def szokoev_kal(evszam):
    if evszam % 400 == 0:
        print("szökőév")
    elif evszam % 100 == 0:
        print("nem szökőév")
    elif evszam % 4 == 0:
        print("szökőév")
    else:
        print("nem szökőév")

my_evszam = int(input("Írj be egy évszámot: "))
print(szokoev_kal(my_evszam))


# Ezt készítettem el először
evszam = int(input("Írj be egy évszámot: "))
if evszam % 400 == 0:
     print("Szökőév")
elif evszam % 100 == 0:
    print("Nem szökőév")
elif evszam % 4 == 0:
    print("Szökőév")
else:
    print("Nem szökőév")




