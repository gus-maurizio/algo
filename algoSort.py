import random, timeit, datetime

'''
Sorting algorithms are selected using criteria such as memory use and stability as well as best, average, and worst-case performance. 
No comparison sort can have better worst-case performance than O(n log(n)). 
Selection sort is one of the simplest sorting algorithms, but it is O(n2) in all cases. 
It requires only O(n) swaps, however, so it may be suitable for data sets where copying is very expensive. 
Insertion sort is efficient when dealing with mostly sorted data sets, where it can have O(n) performance, but average and worst cases are O(n2). 
Quicksort is a divide-and-conquer algorithm that offers O(n log(n)) performance in the best and average cases and O(n2) in the worst case. 
Merge sort is another divide-and-conquer algorithm that offers O(n log(n)) performance in all cases. 
It is especially useful for sorting data sets that cannot fit into memory. 
You can make any sorting algorithm stable by assigning a sequence number to each element and using the sequence number as the tie-breaker in a multi-key sort.
'''

def quickSort(l):
    '''
    Quicksort is a divide-and-conquer algorithm that involves choosing a pivot value from a data set and 
    then splitting the set into two subsets: a set that contains all values less than the pivot and 
    a set that contains all values greater than or equal to the pivot. 
    The pivot/split process is recursively applied to each subset until there
    are no more subsets to split. The results are combined to form the final sorted set.
    in-place [this version!], non-stable, <O(n log(n)),O(n log(n)),O(n2)> - versatile for most cases
    '''
    def quickSortR(l,left,right, debug=False):
        if right-left < 1:
            return
        # we have at least 2 elements - choose pivot
        pivot = l[(left + right) // 2]
        # pivot = l[right]  # another pivot option is the last value
        # print(left,right,pivot,l[left:right+1]) if debug else None
        # we scan both ends to put lower in L and >= in R
        # we use i to represent the right border of L
        # we use j to represent the left border of R
        i = left
        j = right
        while (i <= j):
            while l[i] < pivot:
                i += 1
            while l[j] > pivot:
                j -= 1
            # found elements that are in the wrong place, swap them
            if i <= j:
                l[i],l[j] = l[j],l[i]
                i += 1
                j -= 1
        # print('>>>',i,right,left,j) if debug else None
        if left < j:
            quickSortR(l,left,j)
        if i < right:
            quickSortR(l,i,right)
        return

    n = len(l)
    quickSortR(l,0,n-1)
    return

def selSort(l):
    '''
    Selection sort is one of the simplest sorting algorithms. It starts with the first element in the array (or list) 
    and scans through the array to find the element with the smallest key, which it swaps with the first element. 
    The process is then repeated with each subsequent element until the last element is reached.
    in-place, non-stable, <O(n2),O(n2),O(n2)> - at most n-1 swaps!
    '''
    def selSortR(l,left, debug=False):
        # print(left,len(l),l) if debug else None
        if left >= len(l):
            return
        # find minimum right of left element and swap
        minIdx = left
        i = left + 1
        while i < len(l):
            # print(i,left,len(l)) if debug else None
            if l[i] < l[minIdx]:
                minIdx = i
            i += 1
        # print(minIdx) if debug else None
        l[left], l[minIdx] = l[minIdx], l[left]
        selSortR(l,left+1)
        return

    selSortR(l,0)
    return

def insSort(l):
    '''
    It builds a sorted array (or list) one element at a time by comparing each new element to the already-sorted elements 
    and inserting the new element into the correct location, similar to the way you sort a hand of playing cards.
    in-place, stable, <O(n),O(n2),O(n2)> - efficient for pre-sorted data, suitable for small datasets
    '''
    if len(l) <= 1:
        return
    i = 1   # start with the second element and move forward till the end
    while i < len(l):
        # scan backwards and swap if value is less
        for j in range(i,0,-1):
            if l[j] >= l[j-1]:
                break
            else:
                l[j],l[j-1] = l[j-1],l[j]
        i += 1
    return

def mergeSort(l):
    '''
    Merge sort is another divide-and-conquer algorithm that works by splitting a data set into two or more subsets, 
    sorting the subsets, and then merging them together into the final sorted set.
    NOT in-place, usually stable, <O(n log(n)),O(n log(n)),O(n log(n))> - very large dataset or multiple partially ordered
    best when you need upper bound on performance, but requires O(n) storage
    '''
    n = len(l)
    if n <= 1:
        return
    left  = l[:n//2]
    right = l[n//2:]
    mergeSort(left)
    mergeSort(right)
    # merge values
    r = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            r.append(left[i])
            i += 1
        elif left[i] == right[j]:
            r.append(left[i])
            r.append(right[j])
            j += 1
            i += 1
        else:
            r.append(right[j])
            j += 1
    while i < len(left):
        r.append(left[i])
        i += 1
    while j < len(right):
        r.append(right[j])
        j += 1
    # print(left,right,r)
    for i in range(len(l)):
        l[i] = r[i]
    return


# Driver code to test above
L = [[],[1],[1,2,3,4,5],[5,4,3,2,1], [4,5,3,1,2],[1,1,1], [random.randint(0,100) for x in range(30)]]

mySort = selSort

for l in L:
    mySort(l)
    print(l)



mySorts = [quickSort, mergeSort] #, insSort]

for s in mySorts:
    P = [random.randint(100,10000000) for x in range(20000)]
    start = datetime.datetime.now()    #timeit.timeit()
    s(P)
    end = datetime.datetime.now()
    print(f'executing {s} for {len(P)} random items --- time: {(end-start).total_seconds()}, {P[:10]}')

