def sum1ToN(n):
    if n >= 0:
        sum1ToN(n - 1)
        print(n)

sum1ToN(5)