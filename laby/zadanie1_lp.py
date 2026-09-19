n = int(input("Podaj ilosc liczb w tablicy:"))
T = [int(input()) for _ in range(n)]

T.sort()

k = int(input("Podaj liczbe k: "))
l = n - 1
i = 0
while i<l:
    if T[i] + T[l] == k:
        print(T[i], "+", T[l], "=", k )
        break
    elif T[i] + T[l] < k:
        i += 1
    else:
        l -= 1
else:
    print("Nie udalo sie znalezc sumy dla liczby", k)