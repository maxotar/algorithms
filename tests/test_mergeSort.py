from algorithms.mergeSort import mergeSort


def test_mergeSort():
    alist = [4, 6, 8, 7, 5, 1, 2, 3, 9]
    mergeSort(alist)
    assert alist == [1, 2, 3, 4, 5, 6, 7, 8, 9]
