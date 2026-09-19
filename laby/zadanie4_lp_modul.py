from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obwod(self):
        pass


class Prostokat(Figura):
    def __init__(self, a, b):
        self.A = a
        self.B = b
    def pole(self):
        return self.A * self.B

    def obwod(self):
        return 2* self.A + 2 * self.B

class Kwadrat(Prostokat):
    def __init__(self, a):
       super().__init__(a,a)

class Kolo(Figura):
    def __init__(self, r):
        self.R = r
        self.pi = 3.14
    def pole(self):
        return self.pi * self.R * self.R

    def obwod(self):
        return 2 * self.pi * self.R

class Trojkat(Figura):
    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c
    def pole(self):
        p = (self.A + self.B + self.C) / 2
        return math.sqrt(p * (p - self.A) * (p - self.B) * (p - self.C))
    def obwod(self):
        return self.A + self.B + self.C

def main():
    figury = []

    n = int(input("Ile chcesz wczytać figur?:"))

    for _ in range(n):
        print("Podaj typ (P-prostokąt, K-kwadrat, O-koło, T-trójkąt): ")
        dane = input().split()
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

if __name__ == "__main__":
    main()
