def shellSort(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap, len(alist)):
            val = alist[i]
            j = i
            while j >= gap and alist[j - gap] > val:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = val
        gap //= 2
