def insertionSort(alist):
    for endpoint in range(len(alist) - 1):
        for i in range(endpoint, -1, -1):
            if alist[i] > alist[i + 1]:
                alist[i + 1], alist[i] = alist[i], alist[i + 1]
            else:
                break
