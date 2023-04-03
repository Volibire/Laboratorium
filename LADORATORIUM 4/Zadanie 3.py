def maximum(wektor,l,r):
    if l == r:
        return wektor[l]
    elif (l + 1) == r:
        return max(wektor[l],wektor[r])
    else:
        mid = (l + r) // 2
        max1 = maximum(wektor, l, mid)
        max2 = maximum(wektor, mid + 1, r)
        return max(max1, max2)

wektor = []
liczby = int(input("Podaj ilość liczb: "))
for i in range(liczby):
    a = int(input("Podaj liczby: "))
    wektor.append(a)
maximum(wektor, 0, liczby - 1)
print(maximum(wektor, 0, liczby - 1))