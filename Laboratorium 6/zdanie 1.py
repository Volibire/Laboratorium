a = []
n = int(input("ilość liczb = "))
for i in range(1,n+1):
    a.append(int(input()))
k = 0
for i in range(0,n):
    if a[i]<0:
        k+=1
print(k)