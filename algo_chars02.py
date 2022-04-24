
doc_numberofways='''
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
'''

def numberOfWaysNaive(arr, k):
    n = len(arr)
    r = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j] == k:
                r += 1
    return r


def numberOfWays(arr, k):
    '''
    optimizing to O(n), but memory hungry
        O(nlogn(n)) is possible with sorting and binary search

    Naive O(n^2) low memory 
        def numberOfWaysNaive(arr, k):
            n = len(arr)
            r = 0
            for i in range(0,n-1):
                for j in range(i+1,n):
                    if arr[i]+arr[j] == k:
                        r += 1
            return r
    '''
    n = len(arr)
    if n < 2:
        return 0
    h = {}
    r = 0
    for i in range(0,n):
        if (k-arr[i]) in h:
            r = r + h[k-arr[i]]
            h[k-arr[i]] += 1
        else:
            h[arr[i]] = 1
        pass
    return r

import random,datetime
P = [[1, 2, 3, 4, 3],[1, 5, 3, 3, 3]]
# P = 'abcdefghijklmNOPQRSTUVWXYZ0123456789'
myAlgo = [numberOfWays,numberOfWaysNaive]
k = 6
for p in P:
    for s in myAlgo:
        start = datetime.datetime.now()    #timeit.timeit()
        print(f'list: {p} ways to add to {k}: <{s(p,k)}> by algo {s}')
        end = datetime.datetime.now()
        # print(f'executing {s}  --- time: {(end-start).total_seconds()}')
