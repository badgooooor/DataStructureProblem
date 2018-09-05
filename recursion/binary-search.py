def binarySearch(lo, hi, x, l):
    if hi >= 1:
        mid = int(lo + (hi - lo ) / 2)
        if l[mid] == x:
            return mid 
        
        if l[mid] > x:
            return binarySearch(lo, mid-1, x, l)
        else:
            return binarySearch(mid+1,hi, x, l)

array = [2,3,4,10,40]
size = len(array)
print(binarySearch(0,size,4,array))