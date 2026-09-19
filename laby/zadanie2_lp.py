import string
import re

def analyze_text(text):
    alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
    analyzed_text = {'liczba_slow': 0 ,
                     'dlugosc_srednia_slowa':0,
                     'liczba_wystapien_liter': 0 ,
                     'najczestsze_slowa' : []}

    words = text.split()
    licznik_slow = len(words)
    analyzed_text['liczba_slow'] = licznik_slow

    suma_liter = sum(len(word) for word in words)
    dlugosc_srednia_slowa = suma_liter / licznik_slow
    analyzed_text['dlugosc_srednia_slowa'] = dlugosc_srednia_slowa

    lwl = {lit: 0 for lit in alfabet}
    for char in string.punctuation + " ":
        text = text.replace(char, "")

    for litera in lwl:
        lwl[litera] = lwl.get(litera, 0) + 1
    analyzed_text['liczba_wystapien_liter'] = lwl

    najczestsze = {}
    for w in words:
        najczestsze[w] = najczestsze.get(w, 0) + 1

    najczestsze_sorted = sorted(najczestsze.items(), key=lambda x: x[1], reverse=True)
    analyzed_text['najczestsze_slowa'] = [x for x, c in najczestsze_sorted[:3]]
    return analyzed_text

def main():
    text = "To jest przykładowy tekst. Zawiera kilka zdań, kilka słów, i kilka liter. Tekst ten jest do analizy."
    wynik = analyze_text(text)
    print(wynik)

if __name__ == "__main__":
   main()