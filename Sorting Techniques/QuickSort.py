def partition(arr, start, end):
    pivot=arr[end]
    i=start-1
    
    for j in range(start,end):
        if arr[j]<=pivot :
            i+=1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[end] = arr[end], arr[i+1]
    return i+1

def quickSort(arr, start=0, end=None):
    if end is None:
        end = len(arr)-1
    if start < end:
        pivot_index = partition(arr, start, end)
        quickSort(arr, start, pivot_index-1)
        quickSort(arr, pivot_index+1, end)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quickSort(my_array)
print("Sorted Array :", my_array)