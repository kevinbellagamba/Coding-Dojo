arr = [2,54,3,76,8]

def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for x in range(i+1, len(arr)):
            if arr[min] > arr[x]:
                min = x
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selectionSort(arr))