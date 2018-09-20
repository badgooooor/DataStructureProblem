def multiply(m,n):
    if m == 0 or n == 0:
        return 0
    elif n < 0:
        return -m + multiply(m, n+1)
    else:
        return m + multiply(m, n-1)

print(multiply(3,-5))