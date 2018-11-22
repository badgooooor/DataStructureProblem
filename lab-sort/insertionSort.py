l = [5,1,4,9,6,3,8,2,7]

print(l)
for i in range(1, len(l)):
    cur = l[i]

    j = i - 1
    while j >= 0 and cur < l[j]:
        l[j+1] = l[j]
        j = j - 1
        # print(cur, l)
    l[j+1] = cur
    print(l)


