# Linear Search in Python
def linearSearch(array, x):

    # Going through array sequencially
    for i in range(0, len(array)):
        if (array[i] == x):
            return i
    return -1


# Binary Search in python
def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1
