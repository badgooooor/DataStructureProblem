# Sum from index n to 0

def sum1(n,l):
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return sum1(n - 1, l) + l[n-1]

print('Sum 1')
l = [1,2,3,4]
print(sum1(len(l) ,l))


# Sum from sublist(using start and end index)

def sum2(l,start,end):
    if start > end:
        return 0
    elif start == end:
        return l[end]
    else:
        return l[start] + sum2(l, start+1, end)

print('Sum 2')
l = [1,2,3,4,5]
print(sum2(l, 0, len(l)-1))
print(sum2(l, 0, 3))


# Sum from sublist

def sum3(l):
    n = len(l)
    if n == 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return l[0] + sum3(l[1:])

print('Sum 3')
l = [1,2,3,4,5]
print(sum3(l))
print(sum3(l[:3]))
print(sum3(l[1:]))