def quickSort(arr, key = lambda x: x):
    # this function demonstrates the quicksort algorithm
    # which has a time complexity of O(n log n)

    # if you notice, this quicksort algorithm has been
    # modified so that it can sort elements based on
    # how you want it to be. In this context, I will be
    # sorting tuples fetched from the database and using
    # this algorithm, I am able to sort students according
    # to their name, student number, or grade.

    # just return the array if the length is lesser or equal
    # to one, because at that point, this array is already sorted.
    if len(arr) <= 1:
        return arr

    # a pivot is chosen each time the quickSort function
    # is called. The pivot here is determined by using the
    # floor division operator on the length of the array and then
    # the quotient will then act as the index of the "middle" array
    # this "key" is reponsible on how the list is going to be sorted.

    # to make this more easier to understand, let's say we have
    # a list that contains tuples which we want to sort. We might want
    # to sort the list according to the 2nd element of the tuples.

    # lst = [(1, a), (3, b), (2, c)], and then we want to sort this
    # lst using the 2nd element of each tuples, so let's call the
    # quickSort function like this: quickSort(lst, key = lambda x: x[1])
    # so it would look like this.
    # pivot = key(arr[len(arr) // 2]) = pivot = key(arr[1]) = key((3, b)) = b

    # so basically we first find the pivot "tuple" and then find the "x[1]"
    # of that tuple because that is how we are going to sort the list
    pivot = key(arr[len(arr) // 2])

    # this is basically list comprehension, all elements lesser than
    # the pivot is appended inside the "left" array, all elements equal
    # to the pivot is appended to the middle array, and then all elements
    # greater than the pivot is placed inside the right array.
    left = [x for x in arr if key(x) < pivot]
    middle = [x for x in arr if key(x) == pivot]
    right = [x for x in arr if key(x) > pivot]

    # based on how this was arranged, the quickSort function first arranges
    # elements to the left, then to the middle and then lastly to the right.
    # and each time the function returns, it concatenates each of those
    # subarrays. This involves recursion so the quickSort algorithm is recursively
    # being called as the original array itself is being divided into smaller
    # sub arrays.
    return quickSort(left, key) + middle + quickSort(right, key)

def binarySearch(arr, target, key = lambda x: x):
    # this function demonstrates the binarySearch algorithm
    # which has a time complexity of O(log n)

    # "low" and "high" are both pointers
    # low starts at the beginning of the list (index 0)
    # high starts at the end of the list (last index)
    # (last index is determined by subtracting one from the len of the arr)
    # these two pointers acts as some sort of like "scope" on whhich the
    # "mid" pointer will search through! In a normal binary search, say our
    # mid is less than the target: (target < mid) we then do (low = mid + 1)
    # what this does is that it increases the value of low to mid plus 1
    # which results to the low pointer moving forward because if the "mid" lesser
    # than the target, we already know that our "target" must be greater than
    # the mid. To put it into perspective, it is like removing the elements
    # that we already know won't match the target value, this is why binary search
    # is so fast when dealing with very large values.
    low = 0
    high = len(arr) - 1

    # this while loop will keep on iterating until low becomes greater
    # than high, which means that low and high already crossed with each other
    while low <= high:

        mid = (low + high) // 2
        # instead of "mid" being used to compare with "target"
        # we use the "midVal" variable, this allows the user to choose how they
        # want to search a certain type of student, either search using name or
        # search using student number, this is the same concept used in the
        # modified quicksort algorithm defined above!
        midVal = key(arr[mid])

        # if midVal is equal to the target, then this means we have found the
        # element that we are looking for! We then return that particular element
        if midVal == target:
            return arr[mid]

        # if midVal turns out to be lesser than the target, we eliminate the elements to the left
        elif midVal < target:
            low = mid + 1

        # otherwise, we eliminate the elements to the right.
        else: 
            high = mid - 1
    
    # return None if the low and high pointers have already crossed each other
    return None
