def bubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1
