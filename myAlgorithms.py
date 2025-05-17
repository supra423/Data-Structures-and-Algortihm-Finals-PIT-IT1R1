def quickSort(arr, key = lambda x: x):
    # this function demonstrates the quicksort algorithm
    # which has a time complexity of O(n log n)
    if len(arr) <= 1:
        return arr

    pivot = key(arr[len(arr) // 2])

    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]

    return quickSort(left, key) + middle + quickSort(right, key)
