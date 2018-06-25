from algorithms.binarySearch import binarySearch


def test_binarySearch_odd():
    oddlist = [1, 2, 3, 4, 5, 6, 7]
    assert binarySearch(oddlist, 1)
    assert binarySearch(oddlist, 2)
    assert binarySearch(oddlist, 3)
    assert binarySearch(oddlist, 4)
    assert binarySearch(oddlist, 5)
    assert binarySearch(oddlist, 6)
    assert binarySearch(oddlist, 7)
    assert not binarySearch(oddlist, 0)
    assert not binarySearch(oddlist, 8)


def test_binarySearch_even():
    evenlist = [1, 2, 3, 4, 5, 6]
    assert binarySearch(evenlist, 1)
    assert binarySearch(evenlist, 2)
    assert binarySearch(evenlist, 3)
    assert binarySearch(evenlist, 4)
    assert binarySearch(evenlist, 5)
    assert binarySearch(evenlist, 6)
    assert not binarySearch(evenlist, 0)
    assert not binarySearch(evenlist, 7)
