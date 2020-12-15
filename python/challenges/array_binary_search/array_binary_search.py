def binary_search(arr: list, key) -> int:
    """Returns the index on a key in a given list using a binary search. Returns -2 if key is not found. 

    Args:
        arr (list): array
        key (any): value to search

    Returns:
        int: array index
    """
    low = 0
    high =  len(arr) - 1

    while low <= high:
        mid = high + low // 2
        
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    
    return -1


def binary_search_recursive(arr, key, idx_offset=0):

    mid_idx = round(len(arr) / 2)
    mid_val = arr[mid_idx]
    
    if key < arr[0] or key > arr[len(arr) - 1]:
        return -1
    if key == mid_val:
        return mid_idx + idx_offset
    elif key > mid_val:
        new_arr = arr[mid_idx:]
        idx_offset += mid_idx
    else:
        new_arr = arr[:mid_idx]

    return binary_search(new_arr, key, idx_offset)