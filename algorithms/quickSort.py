def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, lo, hi):
    if lo < hi:
        p = partition(alist, lo, hi)
        quickSortHelper(alist, lo, p - 1)
        quickSortHelper(alist, p + 1, hi)


def partition(alist, lo, hi):
    pivot = alist[hi]
    i = lo - 1
    for j in range(lo, hi):
        if alist[j] < pivot:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i + 1], alist[hi] = alist[hi], alist[i + 1]
    return i + 1
