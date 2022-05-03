import random

doc_stocksell = '''
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earn by buying on day 0, selling on day 3. 
Again, buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
'''

def minMax(a):
    n = len(a)
    p = 0           # profit
    i = 1
    while i < n:
        p += (a[i] - a[i-1]) if a[i] > a[i-1] else 0
        i += 1
    return p

def largestMinMax(a):
    '''
    Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number. 
    '''
    n = len(a)
    a_min = a[0]
    l_dif = a[0]-a_min
    i = 1
    while i < n:
        l_dif = (a[i] - a_min) if (a[i] - a_min) > l_dif else l_dif
        a_min = a[i] if a[i] < a_min else a_min
        i += 1
    return l_dif


P = [   [100, 180, 260, 310, 40, 535, 695],
        [10],
        [30,20,10],
        [10,5,80,90,30],
    ]

for p in P:
    print(p,minMax(p),largestMinMax(p))