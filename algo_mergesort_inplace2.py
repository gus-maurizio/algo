
doc_mergesort='''
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then it merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.

https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge_sort_algorithm_diagram.svg
https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge-sort-example-300px.gif

The approach is different. We order contiguous pairs first, and then move up merging

    n=7             [38,27,43,3,9,82,10]
    it 1  comp      [27,38] [3,43]  [9,82] [10]  n/2 comparisons
    it 2  1 merge   [3,27,38,43]    [9,10,82]   
    it 3  2 merge   [3,9,10,27,38,43,82]

Although heapsort has the same time bounds as merge sort, it requires only Θ(1) auxiliary space instead of merge sort's Θ(n). 
On typical modern architectures, efficient quicksort implementations generally outperform merge sort for sorting RAM-based arrays.
On the other hand, merge sort is a stable sort and is more efficient at handling slow-to-access sequential media. 
Merge sort is often the best choice for sorting a linked list: in this situation it is relatively easy to implement a merge sort 
in such a way that it requires only Θ(1) extra space, and the slow random-access performance of a linked list makes some other algorithms 
(such as quicksort) perform poorly, and others (such as heapsort) completely impossible.

As of Perl 5.8, merge sort is its default sorting algorithm (it was quicksort in previous versions of Perl).
In Java, the Arrays.sort() methods use merge sort or a tuned quicksort depending on the datatypes and for implementation efficiency 
switch to insertion sort when fewer than seven array elements are being sorted.
The Linux kernel uses merge sort for its linked lists.
Python uses Timsort, another tuned hybrid of merge sort and insertion sort, that has become the standard sort algorithm in 
Java SE 7 (for arrays of non-primitive types), on the Android platform, and in GNU Octave.

'''

def mergeSort(a, debug=False):
    def _merge(a,s,m,e,debug):
        # termination condition
        s2 = m+1
        print(f'   merge-> {s} to {m} {a[s:m+1]} ; {s2} to {e} {a[s2:e+1]}') if debug else None
        if (a[m] <= a[s2]):
            print(f'   term-> {s} to {m} ; {s2} to {e} {a[s:e+1]}') if debug else None
            return
        while (s <= m and s2 <= e):
            if (a[s] <= a[s2]):     # right place
                s += 1
            else:
                # value at s2 is less, so save and shift
                value = a[s2]
                index = s2
                print(f'      shift <{value}> from {s2} to {s}') if debug else None
                while (index != s):
                    a[index] = a[index - 1]
                    index -= 1
                a[s] = value
                m   += 1
                s   += 1
                s2  +=1
        return

    n = len(a)
    if n <= 1:
        return
    # first order consecutive pairs: 0 and 1, 2 and 3, ...
    for i in range(0,n//2):
        l = 2*i
        r = l + 1
        if a[l] > a[r]:
            a[r],a[l] = a[l],a[r]
    # now we have a set of n//2 consecutive pairs and the last (if odd number) one.
    # we need to perform 
    sortedGroupSize = 2 
    groups = n // sortedGroupSize + (1 if n % sortedGroupSize == 1 else 0)
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
# P = [[10, 20, 30, 40, 50, 60, 70, 61, 51, 41, 31, 21,5]]
for p in P:
    # print(p)
    print(f'sorting  {len(p):3d} >>{p}<<: ')
    mergeSort(p,debug=False)
    print(f'             <<{p}>>')


