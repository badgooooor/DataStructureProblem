def sum1ToN(n):
    if n >= 0:
        print(n)
        sum1ToN(n - 1)

sum1ToN(5)