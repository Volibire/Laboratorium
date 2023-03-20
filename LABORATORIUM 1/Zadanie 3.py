N = int(input("Podaj liczbę N: "))
F = int(input("Podaj liczbę wyszukiwaną: "))
A = [int(input("Podaj liczbę: ")) for i in range(N)]
i = 0
while i < N:
    if A[i]==F:
        print("Liczba wyszukiwana występuje w liście")
        break
    else:
        i += 1
        continue
else:
    print("Liczba wyszukiwana nie występuje w liście")

