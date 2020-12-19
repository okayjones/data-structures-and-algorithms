from challenges.array_shift import __version__
from challenges.array_shift.array_shift import array_shift


def test_version():
    assert __version__ == "0.1.0"


def test_array_shift_even_int():
    arr = [2, 4, 6, 8]
    n = 5
    actual = array_shift(arr, n)
    expected = [2, 4, 5, 6, 8]
    assert actual == expected


def test_array_shift_odd_int():
    arr = [4,8,15,23,42]
    n = 16
    actual = array_shift(arr, n)
    expected = [4,8,15,16,23,42]
    assert actual == expected


def test_array_shift_odd_str():
    arr = ['A','B','C','E','F']
    n = 'D'
    actual = array_shift(arr, n)
    expected = ['A','B','C','D','E','F']
    assert actual == expected
    
def test_array_shift_empty():
    arr = []
    n = 1
    actual = array_shift(arr, n)
    expected = "Invalid Input"
    assert actual == expected