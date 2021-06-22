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

szokoev_kal(my_evszam)







