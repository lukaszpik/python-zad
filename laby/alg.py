# Zadanie 5 (algorytmika)

L = [5, 9, 3, 7, 2, 1]

i = 0
suma1 = L[0]
suma2 = sum(L[1:])
r = abs(suma1 - suma2)

for j in range(1,len(L)-1):
    suma1 = suma1 + L[j]
    suma2 = suma2 - L[j]
    if abs(suma1 - suma2) < r:
        r = abs(suma1 - suma2)
        i = j

print(i)