def sumEven(l, total):
    if not l:
        return 0
    else:
        if l[0] % 2 == 0:
            print(' +',l[0], end=' ')
            sumEven(l[1:], total + l[0])
        else:
            sumEven(l[1:], total)
        if len(l) == 1:
            print('Sum of even numbers:', total)
    

l = [14,556,2,4,1,3,7,3]

sumEven(l, 0)