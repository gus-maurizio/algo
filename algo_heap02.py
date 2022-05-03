doc_heap = '''
[1,2,3,4,5,6,7] -> [7, 4, 6, 1, 3, 2, 5]

         7                  k = 0 i=0
      /     \
    4        6              k = 1  i=1 & 2  parent = i-1//2
  /   \    /   \
1      3  2     5           k = 2  log2(n) elements 2^k parent i-1//2
'''

import random,math
from re import I

def buildHeap(h):
    '''
    builds a max heap with arr elements
    Rather than starting with a trivial heap and repeatedly adding leaves, Floyd's algorithm starts with the leaves, 
    observing that they are trivial but valid heaps by themselves, and then adds parents. 
    Starting with element n/2 and working backwards, each internal node is made the root of a valid heap by sifting down. 
    The last step is sifting down the first element, after which the entire array obeys the heap property.
    '''
    def _heapify(h,n):
        last  = n - 1
        parent = (last - 1) // 2
        while parent >= 0:
            _bubbleDown(h,parent,last)
            parent -= 1

    def _bubbleDown(h,i,r):
        '''
        Repair the heap whose root element is at index 'i', assuming the heaps rooted at its children are valid.
        bubbles down element i heap property (heap.value >= heap.left.value & heap.right.value)
        assumes heap.left and heap.right are valid heaps (but might not be complete) ! the root might be wrong
        [5, 4, 6, 1, 3, 2, 7] i=0 r=5 (incomplete heap!!!) n=6 n//2=3! only the first 3 elements need inspection.
               5            k = 0  i=0 -> l=4 r=6 (should go up)
            /     \
           4       6        k = 1  
         /   \    /   
        1     3  2          k = 2  
        '''
        root  = i 
        left  = 2*root+1
        while left <= r:            # root has at least one child
            right = 2*root+2
            # print(f'>>in bbd: {root} {left} {right} {i}:{r} {h[root:r+1]}')
            swap = root
            if h[swap] < h[left]:
                swap = left
            if right <= r and h[swap] < h[right]:
                swap = right
            if swap == root:
                return
            # print(f'>>>>in bbd: {root} {swap} {h[i:r+1]}')
            h[swap], h[root] = h[root], h[swap]
            root = swap
            left  = 2*root+1

    # Build the heap in place so that largest value is at the root
    n = len(h)
    _heapify(h,n)
    # print(h)
    en = n - 1      # last element
    while en > 0:
        h[0], h[en] = h[en],h[0]    # move highest to last position
        en -= 1                     # shorten heap! and balance element 0 down
        # print(f'bbd call--> 0:{en} {h[:en+1]} {h[en+1:]}')
        _bubbleDown(h,0,en)
    return h

P = [1,2,3,4,5,6,7]
P = [7,1,3,3,2,5,5,5,6,1]
# a balanced heap has 1 + 2 + 4 + 8 + ... 1,3,7,15 2**N-1
P = [random.randrange(0,400) for _ in range(2**6 - 1)]
P = [7,6,5,4,3,2,1]
print(f'{P}')
buildHeap(P)
print(f'{sorted(P) == P} \n{P}')



#             92
#      86                 88 
#  54       85       59       66
# 0  36   13 34    8   24   12  66