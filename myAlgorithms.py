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

def binarySearch(arr, target, key = lambda x: x):
    low = 0 
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = key(arr[mid])

        if midVal == target:
            return arr[mid]
        elif midVal < target:
            low = mid + 1
        else: 
            high = mid - 1

    return None
