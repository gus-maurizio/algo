
doc_mergesort='''
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then it merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See the following C implementation for details.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge_sort_algorithm_diagram.svg
https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge-sort-example-300px.gif

    n=7             [38,27,43,3,9,82,10]
    m=3 (7//2)      [38,27,43,3]            [9,82,10]
    m=(2 1)         [38,27] [43,3]          [9,82] [10]
    log(7) = 3      [38] [27] [43] [3]      [9] [82] [10]
    merge           [27,38] [3,43]          [9,82] [10]
                    [3,27,38,43]            [9,10,82]
                    [3,9,10,27,38,43,82]
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

    def _mergesort(a,s,e,debug):
        print(f'sort-> {s} {e} {a[s:e+1]} ') if debug else None
        if s >= e:
            return
        m = s + (e - s) // 2    # avoids overflows
        _mergesort(a,s,m,debug)
        _mergesort(a,m+1,e,debug)
        _merge(a,s,m,e,debug)
        return

    n = len(a)
    _mergesort(a,0,n-1,debug)
    return

 
 
# Driver code
P = [   [40,50,60],
        [80,10,20,30],
        [10,20, 30,40, 50,60, 70,61, 51,41, 31,21],
        [70,60,50,40,30,20],
        [10,20,30,40,50,60],
        [12, 11, 13, 5, 6, 7],
        [10,10,10,10,10],
        [38,27,43,3,9,82,10],
        []
    ]
P = [[9,82,10]]
for p in P:
    # print(p)
    print(f'sorting <<{len(p)}>> {p}: ', end='')
    mergeSort(p,debug=True)
    print(f'{p}')


