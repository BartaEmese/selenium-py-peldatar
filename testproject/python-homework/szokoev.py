# Még nincs kész.

def szokoev_kal(x):
    if x % 4 == 0 and x % 400 == 0:
        return bool(x)

evszam = int(input("Írj be egy évszámot: "))
szokoev = szokoev_kal(evszam)
if szokoev == "True":
    print("Szökőév.")
else:
    print("Nem szökőév.")
