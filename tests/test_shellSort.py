from algorithms.shellSort import shellSort


def test_shellSort():
    alist = [4, 6, 8, 7, 5, 1, 2, 3, 9]
    shellSort(alist)
    assert alist == [1, 2, 3, 4, 5, 6, 7, 8, 9]
