def dynam(a, b):
    if a == 0 and b == 0 or a < 0 and b < 0:
         return "Niepoprawne argumenty"
    elif a > 0 and b == 0:
        return 0
    elif a == 0 and b > 0:
        return 1
    else:
        return (dynam(a-1, b)+dynam(a, b-1))/2

a=int(input("Podaj a:"))

b=int(input("Podaj b:"))


print(dynam(a,b))