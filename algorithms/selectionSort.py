def selectionSort(alist):
    for slot in range(len(alist) - 1, 0, -1):
        iMax = 0
        for index in range(1, slot + 1):
            if alist[index] > alist[iMax]:
                iMax = index

        alist[slot], alist[iMax] = alist[iMax], alist[slot]
