
doc_heapsort='''
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. 
It is similar to selection sort where we first find the minimum element and place the minimum element at the beginning. We repeat the same process for the remaining elements.
a = [30,70,50]

        30(0)                 
       /   \         
    70(1)   50(2)

Child (70(1)) is greater than the parent (30(0))

Swap Child (70(1)) with the parent (30(0))
        70(0)                 
       /   \         
    30(1)   50(2)

How to build the heap? 
Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom-up order.
Lets understand with the help of an example:
Input data: [4, 10, 3, 5, 1] n=5 start with index n//2-1= 1!
         4(0)               i = 0
        /   \
     10(1)   3(2)           1, 2 (2i+1 and 2)
    /   \
 5(3)    1(4)               3,4

The numbers in bracket represent the indices in the array 
representation of data.

Applying heapify procedure to index 1:
         4(0)
        /   \
    10(1)    3(2)
    /   \
5(3)    1(4)

Applying heapify procedure to index 0:
        10(0)
        /  \
     5(1)  3(2)
    /   \
 4(3)    1(4)
The heapify procedure calls itself recursively to build heap
heapified array is now: [10,5,3,4,1]

In the second step, a sorted array is created by repeatedly removing the largest element from the heap (the root of the heap), and inserting it into the array. 
The heap is updated after each removal to maintain the heap property. Once all objects have been removed from the heap, the result is a sorted array.

The buildMaxHeap() operation is run once, and is O(n) in performance. 
The siftDown() function is O(log n), and is called n times. Therefore, the performance of this algorithm is O(n + n log n) = O(n log n).

https://en.wikipedia.org/wiki/Heapsort#/media/File:Heapsort-example.gif

Comparison with other sorts
Heapsort primarily competes with quicksort, another very efficient general purpose in-place comparison-based sort algorithm.
Heapsort's primary advantages are its simple, non-recursive code, minimal auxiliary storage requirement, and reliably good performance: 
its best and worst cases are within a small constant factor of each other, and of the theoretical lower bound on comparison sorts. 
While it cannot do better than O(n log n) for pre-sorted inputs, it does not suffer from quicksort's O(n2) worst case, either. 
(The latter can be avoided with careful implementation, but that makes quicksort far more complex, and one of the most popular solutions, introsort, uses heapsort for the purpose.)

Its primary disadvantages are its poor locality of reference and its inherently serial nature; the accesses to the implicit tree are 
widely scattered and mostly random, and there is no straightforward way to convert it to a parallel algorithm.

This makes it popular in embedded systems, real-time computing, and systems concerned with maliciously chosen inputs,such as the Linux kernel. 
It is also a good choice for any application which does not expect to be bottlenecked on sorting.

A well-implemented quicksort is usually 2–3 times faster than heapsort.Although quicksort requires fewer comparisons, this is a minor factor. 
(Results claiming twice as many comparisons are measuring the top-down version; see  Bottom-up heapsort.) 
The main advantage of quicksort is its much better locality of reference: partitioning is a linear scan with good spatial locality, 
and the recursive subdivision has good temporal locality. With additional effort, quicksort can also be implemented in mostly branch-free code, 
and multiple CPUs can be used to sort subpartitions in parallel. Thus, quicksort is preferred when the additional performance justifies the implementation effort.

The other major O(n log n) sorting algorithm is merge sort, but that rarely competes directly with heapsort because it is not in-place. 
Merge sort's requirement for Ω(n) extra space (roughly half the size of the input) 
is usually prohibitive except in the situations where merge sort has a clear advantage:
    When a stable sort is required
    When taking advantage of (partially) pre-sorted input
    Sorting linked lists (in which case merge sort requires minimal extra space)
    Parallel sorting; merge sort parallelizes even better than quicksort and can easily achieve close to linear speedup
    External sorting; merge sort has excellent locality of reference

'''

def heapSort(arr, debug=True):
    def _heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left  = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
    
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[largest] < arr[l]:
            largest = l
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            # Heapify the root.
            _heapify(arr, n, largest)
        return

    n = len(arr)
    print(f'To sort: {arr} start with {n//2-1} and go down') if debug else None
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        print(f'iteration {i}: {arr}')
        _heapify(arr, n, i)
        # print(f'iteration {i}: {arr}')
    print(f'iterations done. Heapified: {arr} now sort') if debug else None
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        _heapify(arr, i, 0)
 
 
# Driver code
arr = [12, 11, 13, 5, 6, 7]
arr = [70,60,50,40,30,20]
arr = [10,20,30,40,50,60]
arr = [ 6, 5, 3, 1, 8, 7, 2, 4] #wikipedia example!
arr = [10,20,30,40,50,60,70,61,51,41,31,21]
heapSort(arr)
n = len(arr)
print(f'Sorted: {arr}')


