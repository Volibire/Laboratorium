def ciąg(n):
    if n == 0:
        return 1

    elif n == 1:
        return 1

    else:
        ar = [0, 1]
        i = 2

        while i <= n:
            ar.append(2 * ar[i - 1] - ar[i - 2])
            i += 1

        return ar[i - 1]


print(ciąg(3))