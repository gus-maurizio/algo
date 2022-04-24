
doc_mergesort='''
sorting algorithm based on Insertion Sort and Merge Sort.
'''

def mergeSort(a, debug=False):
    MINRUN = 2**5
    def _insertionSort(a, l, r):
        for i in range(l + 1, r + 1):
            j = i
            while j > l and a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1
 

    def _merge(a,s,m,e,debug):
        # termination condition
        s2 = m+1
        print(f'   merge-> {s} to {m} {a[s:m+1]} ; {s2} to {e} {a[s2:e+1]}') if debug else None
        if (a[m] <= a[s2]):
            # print(f'   term-> {s} to {m} ; {s2} to {e} {a[s:e+1]}') if debug else None
            return
        while (s <= m and s2 <= e):
            if (a[s] <= a[s2]):     # right place
                s += 1
            else:
                # value at s2 is less, so save and shift
                value = a[s2]
                index = s2
                # print(f'      shift <{value}> from {s2} to {s}') if debug else None
                while (index != s):
                    a[index] = a[index - 1]
                    index -= 1
                a[s] = value
                m   += 1
                s   += 1
                s2  +=1
        return

    n = len(a)
    numsorts = n // MINRUN + (1 if n % MINRUN > 0 else 0)
    for i in range(numsorts):
        _insertionSort(a, i*MINRUN, min(n,(i+1)*MINRUN) - 1)
    # now we have sequences of MINRUN ordered arrays
    print(f'MINRUN: {MINRUN} {a}') if debug else None
    sortedGroupSize = MINRUN
    groups = n // sortedGroupSize + (1 if n % sortedGroupSize > 0 else 0)
    while (groups >= 1 and sortedGroupSize < n):
        merges = max(groups // 2,1)         # at least 1 merge if we have 1 or more groups, to avoid 1 group and a tail less than sortedGroupSize
        print(f'groups: {groups} of {sortedGroupSize} elements (last might have 1 less) -> perform {merges} merges {a}') if debug else None
        for i in range(0,merges):
            s = sortedGroupSize * 2 * i
            m = s + sortedGroupSize - 1
            e = min(m + sortedGroupSize,n-1)
            print(f'merging {i} {s}:{m} {m+1}:{e}') if debug else None
            _merge(a,s,m,e,debug)
        # perform merge between consecutive sorted groups
        # s = i - 1
        # e = 2*i + 1
        # _merge(a,s,m,e,debug)
        sortedGroupSize *= 2
        groups = n // sortedGroupSize + (1 if n % sortedGroupSize == 1 else 0)
        print(f'----> groups: {groups} of {sortedGroupSize} elements {a}') if debug else None
    return

 
# Driver code
P = [   [40,50,60],
        [80,10,20,30],
        [10,20, 30,40, 50,60, 70,61, 51,41, 31,21],
        [10, 20, 30, 40, 50, 60, 70, 61, 51, 41, 31, 21,5],
        [70,60,50,40,30,20],
        [10,20,30,40,50,60],
        [12, 11, 13, 5, 6, 7],
        [10,10,10,10,10],
        [38,27,43,3,9,82,10],
        [3,2,1],
        [2,1],
        [1],
        []
    ]
# P = [[12,9,3,1,10,20,30,40,8]] #,82,4,5,10]]
P = [[10, 20, 30, 40, 50, 60, 70, 61, 51, 41, 31, 21,5]]

import random
P = [ [random.randrange(0,1000) for _ in range(300) ] ]
for p in P:
    # print(p)
    print(f'sorting  {len(p):3d} >>{p}<<: ')
    mergeSort(p,debug=False)
    print(f'             <<{p}>>')


