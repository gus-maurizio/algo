
doc_mergesort='''
sorting algorithm based on randomized quicksort.
'''
import random
def quickSort(a, debug=False):
    def _partition(a,l,r):
        p = r
        highpoint = l
        i = l
        # print(f'---> part p:{p} <{a[p]}> h:{highpoint} [{l}:{r}] {a}')
        while (i < r):
            if a[i] < a[p]:
                a[i],a[highpoint] = a[highpoint],a[i]
                # print(f'------> part i:{i} <{a[i]}> p:{p} <{a[p]}> h:{highpoint} [{l}:{r}] {a}')
                highpoint += 1            
            i += 1
        a[p],a[highpoint] = a[highpoint],a[p]    
        # print(f'+++> part h:{highpoint} [{l}:{r}] ')
        return highpoint

    def _quickSort(a, l, r):
        if l < r:
            # print(f'--> _QS [{l}:{r}] ')
            p = _partition(a,l,r)
            # print(f'++part {p} [{l}:{r}] ({n}): {a}')
            # return
            _quickSort(a,l,p-1)
            _quickSort(a,p+1,r)
 
    def _randomize(a,l,r):
        i = l + (r-l) // 2
        j = r
        # reverse second half
        while i < j:
            a[i],a[j] = a[j],a[i]
            j -= 1
            i += 1
        # shuffle 
        n = r - l + 1
        i = 0
        while i < n//2:
            j = ((n//2)**2+i) % n
            a[l+i],a[l+j] = a[l+j],a[l+i]
            i += 1
        return

    n = len(a)
    if n <= 1:
        return
    # to improve chances of being on the O(n*logn) average/best case, randomize the input
    # reverse the second half and shuffle. O(n)!
    # _randomize(a,0,n-1)
    # print('rrr--->',a)
    _quickSort(a,0,n-1)
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
P = [ [random.randrange(0,5000) for _ in range(300) ] ]

# P = [   [90, 20, 40, 30, 50, 60] ]

import random
for p in P:
    print(f'sorting  {len(p):3d} >>{p}<<: ')
    quickSort(p,debug=False)
    print(f'             <<{p}>>')


