from challenges.quick_sort.quick_sort import quick_sort


def test_quick_sort_simple():
    arr = [8, 4, 23, 42, 16, 15]
    expected = [4, 8, 15, 16, 23, 42]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected

def test_quick_sort_reverse():
    arr = [20, 18, 12, 8, 5, -2]
    expected = [-2, 5, 8, 12, 18, 20]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected


def test_quick_sort_few_unique():
    arr = [5, 12, 7, 5, 5, 7]
    expected = [5, 5, 5, 7, 7, 12]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected


def test_quick_sort_nearly_sorted():
    arr = [2, 3, 5, 7, 13, 11]
    expected = [2, 3, 5, 7, 11, 13]
    quick_sort(arr, 0, len(arr) - 1)
    assert arr == expected
