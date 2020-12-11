import math


def array_shift(arr, n):
    end = len(arr)
    mid = math.ceil(end / 2)
    arr[mid + 1 : end + 1] = arr[mid:end]
    arr[mid] = n
    return arr
