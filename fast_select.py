def fastSelect(arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th
    # largest element in the given array
    n = len(arr)
    if(k > 0 and k <= n):
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0

        while(i < n // 5):
            median = findMedian(arr, 5 * i, 5)
            setOfMedians.append(median)
            i += 1

        if(5 * i < n):
            median = findMedian(arr, 5*i, n % 5)
            setOfMedians.append(median)

        if(len(setOfMedians) == 1):
            pivot = setOfMedians[0]
        elif(len(setOfMedians) > 1):
            pivot = fastSelect(setOfMedians, len(setOfMedians) // 2)

        for element in arr:
            if element < pivot:
                Arr_Less_P.append(element)
            elif element > pivot:
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)

        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)

        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))

        else:
            return pivot


def findMedian(arr, start, size):
    myList = []
    for i in range(start, start + size):
        myList.append(arr[i])

    myList.sort()
    return myList[size // 2]


arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 2
fastSelect(arr, k)  # Should be 1
