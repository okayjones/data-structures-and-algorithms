import math


def array_shift(arr, n):
    """Inserts a value at the midpoint of an array. If the array has an odd number of item, the midpoint is considered the index to the right.

    Args:
        arr (array): An array
        n (any): Any value to insert

    Returns:
        array: array with shifted value
    """
    end = len(arr)
    mid = math.ceil(end / 2)
    try:
        arr[mid + 1 : end + 1] = arr[mid:end]
        arr[mid] = n
        return arr
    except:
        return "Invalid Input"
