from main import *

figury = []

n = int(input("Ile chcesz wczytać figur?:"))

for _ in range(n):
    print("Podaj typ (P-prostokąt, K-kwadrat, O-koło, T-trójkąt): ")
    dane= input().split()
    typ = dane[0].upper()

    if typ == "P":
        a = float(dane[1])
        b = float(dane[2])
        figury.append(Prostokat(a, b))

    elif typ == "K":
        a = float(dane[1])
        figury.append(Kwadrat(a))

    elif typ == "O":
        r = float(dane[1])
        figury.append(Kolo(r))

    elif typ == "T":
        a = float(dane[1])
        b = float(dane[2])
        c = float(dane[3])
        figury.append(Trojkat(a, b, c))

    else:
        print("Nieznany typ.")

for f in figury:
    print("Pole: ", f.pole(), "Obwód:", f.obwod())