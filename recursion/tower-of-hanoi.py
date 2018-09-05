def movePeg(n, source, spare, dest):
    if n == 1:
        print(n, 'from ', source, 'to', dest)
    else:
        movePeg(n-1, source, spare, dest)
        print(n, 'from ', spare, 'to', source)
        movePeg(n-1, spare, dest, source)

movePeg(4, 'A', 'B', 'C')