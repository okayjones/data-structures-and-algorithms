from array_binary_search.array_binary_search import binary_search


def test_binary_search_even_left():
    arr = [4,8,15,16,23,42]
    key = 15

    actual = binary_search(arr, key)
    expected = arr.index(key)
    assert actual == expected


def test_binary_search_odd_right():
    arr = [4,8,15,16,23,42,50]
    key = 42

    actual = binary_search(arr, key)
    expected = arr.index(key)
    assert actual == expected


def test_binary_search_out_of_bounds():
    arr = [4,8,15,16,23,42,50]
    key = 75

    actual = binary_search(arr, key)
    expected = -1
    assert actual == expected