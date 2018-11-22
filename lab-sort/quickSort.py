l = [5,1,4,9,6,3,8,2,7]

# partition the array to two part
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        # find partion index
        pi = partition(arr, low, high)

        # seperately sort (before partition and after partition)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Driver code to test above 
print(l)
n = len(l) 
quickSort(l,0,n-1)
print(l)