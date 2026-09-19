import random
import time

def selection_sort(table, L, P):
    for i in range(L, P + 1):
        min_num = i
        for j in range(i + 1, P + 1):
            if table[j] < table[min_num]:
                min_num = j
        table[i], table[min_num] = table[min_num], table[i]

def dzielenie_tablicy(table, L, P):
    pivot = table[(L+P)//2]
    i = L
    j = P
    while True:
        while table[i] < pivot:
            i += 1
        while table[j] > pivot:
            j -= 1
        if i >= j:
            return j
        table[i], table[j] = table[j], table[i]
        i += 1
        j -= 1

def qsort_zwykly(table, L, P):
    if L >= P:
        return
    p = dzielenie_tablicy(table, L, P)
    qsort_zwykly(table, L, p)
    qsort_zwykly(table, p+1, P)

def qsort_optymised(table, L, P):
    if (P - L + 1) <= 10:
        selection_sort(table, L, P)
        return
    if L < P:
      s = dzielenie_tablicy(table, L, P)
      qsort_optymised(table, L, s)
      qsort_optymised(table, s+1, P)

def main():
    N = 100000
    table = [random.randint(0, 100000) for _ in range(N)]
    table2 = table.copy()

    t1 = time.time()
    qsort_zwykly(table, 0, len(table) - 1)
    print("Czas zwyklego qsorta:", time.time() -  t1)
    t2 = time.time()
    qsort_optymised(table2, 0, len(table2) - 1)
    print("Czas qsort z optymalizacją:", time.time() - t2)


if __name__ == "__main__":
   main()