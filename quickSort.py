def quickSort(arr):

    if len(arr) <= 1:
        return arr
    left, middle, right = [], [], []
    for i in arr:

        pivot = arr[len(arr) // 2]

        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        else:
            right.append(i)

    return quickSort(left) + middle + quickSort(right)

def reverse_list(array):
    array = quick_sort(array)
    array.reverse()
    return array


