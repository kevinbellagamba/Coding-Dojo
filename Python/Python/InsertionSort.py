arr = [2,54,3,76,8]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        x = i-1
        while x >=0 and key < arr[x]:
            arr[x+1] = arr[x]
            x -= 1
        arr[x+1] = key
    return arr    

 print(insertionSort(arr))