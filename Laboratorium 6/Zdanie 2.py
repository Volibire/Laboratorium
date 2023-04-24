a = []
p = []
k = 0
j = 0
for i in range(10):
    a.append(int(input()))
while j <10:
    if a[j] % 2 == 0:
        p.append(a[j])
        k+=1
        j+=1
    else:
        j+=1
print(p)
print(k)