l = [5,1,4,9,6,3,8,2,7]

# Simple bubble sort O(n^2)
print('Simple bubble sort')
for i in range(len(l)):
    for j in range(0, len(l) - i - 1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            print(l)

a = [5,1,4,9,6,3,8,2,7]

print('Optimised bubble sort')
for i in range(len(a)):
    swapped = False
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(a)
            swapped = True
    if swapped == False:
        break
