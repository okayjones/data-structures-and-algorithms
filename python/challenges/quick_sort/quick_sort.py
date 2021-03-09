def quick_sort(arr, left, right):
    # can we add defaults?
    if left < right:
        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1

    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            arr[low], arr[i] = arr[i], arr[low]
    arr[right], arr[low + 1] = arr[low + 1], arr[right]

    return low + 1