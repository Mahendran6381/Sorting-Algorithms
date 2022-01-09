def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start-1
    for i in range(start, end):
        if arr[i] <= pivot:
            pIndex += 1
            arr[pIndex], arr[i] = arr[i], arr[pIndex]
    arr[pIndex+1], arr[end] = arr[end], arr[pIndex+1]
    return pIndex+1


def quickSort(arr, start, end):
    if len(arr) == 1:
        return
    if start < end:
        pindex = partition(arr, start, end)
        print(arr[pindex])
        quickSort(arr, start, pindex-1)
        quickSort(arr, pindex+1, end)


if __name__ == "__main__":
    arr = [4, 7, 3, 2, 9, 10, 21, 45, 67, 89, 23, 11, 10, -1]
    print(*arr)
    quickSort(arr, 0, len(arr)-1)
    print(*arr)
