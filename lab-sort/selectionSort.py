l = [5,1,4,9,6,3,8,2,7]

print(l)
for i in range(len(l)):
    min_idx = i
    for j in range(i+1, len(l)):
        if l[min_idx] > l[j]:
            min_idx = j
    l[i], l[min_idx] = l[min_idx], l[i]
    print(l)