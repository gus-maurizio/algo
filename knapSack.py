import random, datetime
from collections import namedtuple
from readline import parse_and_bind

def subsets(n):
    '''
    returns the subsets of n elements, with boolean indicator for presence of element i
    n = 0 -> []
    n = 1 -> [[F], [T]]
    n = 2 -> [[F,F], [F,T], [T,F], [T,T]]
    '''
    if n == 0:
        return []
    elif n == 1:
        return [[True], [False]]
    else:
        _p = subsets(n-1)
        return [ [False] + p for p in _p ] + [ [True] + p for p in _p ]

# print(subsets(3))

def knap0(W,weights,values,n):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    naive recursive
    '''
    if W == 0 or n == 0:
        return 0
    # remove last item if it does not fit
    if weights[n-1] > W:
        return knap0(W,weights,values, n-1)
    else:
        return max(values[n-1] + knap0(W-weights[n-1],weights,values,n-1),
                                 knap0(W,             weights,values,n-1))

def knap0memo(W,weights,values,n,memo={}):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    naive recursive
    '''
    if W == 0 or n == 0:
        return 0
    # remove last item if it does not fit
    if (W,n) in memo:
        return memo[(W,n)]
    if weights[n-1] > W:
        memo[(W,n)] = knap0(W,weights,values, n-1)
        return memo[(W,n)]
    else:
        if (W-weights[n-1],n-1) not in memo:
            memo[(W-weights[n-1],n-1)] = knap0(W-weights[n-1],weights,values,n-1)
        if (W,n-1) not in memo:
            memo[(W,n-1)] = knap0(W,weights,values,n-1)
        return max(values[n-1] + memo[(W-weights[n-1],n-1)],
                    memo[(W,n-1)])

def knap0DP1(W,wt,val,n):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    Knapsack problem has both properties (overlapping subproblems and optimal substructure) of a dynamic programming problem.     
    In the following recursion tree, K() refers 
    to knapSack(). The two parameters indicated in the
    following recursion tree are n and W.
    The recursion tree is for following sample inputs.
    wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}
                        K(n, W)
                        K(3, 2)  
                    /            \ 
                    /                \               
                K(2, 2)                  K(2, 1)
            /       \                  /    \ 
            /           \              /        \
        K(1, 2)      K(1, 1)        K(1, 1)     K(1, 0)
        /  \         /   \              /        \
        /      \     /       \          /            \
    K(0, 2)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)   K(0, 0)
    Recursion tree for Knapsack capacity 2 
    units and 3 items of 1 unit weight.
    We will construct a temporary array K[][] (DP[][]) in bottom-up manner.
    In a DP[][] table let's consider all the possible weights from '1' to 'W' as the columns and weights that can be kept as the rows.
    The state DP[i][j] will denote maximum value of 'j-weight' considering all values from '1 to ith'. 
    So if we consider 'wi' (weight in 'ith' row) we can fill it in all columns which have 'weight values > wi'. 
    Now two possibilities can take place: 

      -  Fill wi in the given column.
      -  Do not fill wi in the given column.

    '''

    doc = '''

In a DP[][] table let's consider all the possible weights from '1' to 'W' as the columns and weights that can be kept as the rows.
The state DP[i][j] will denote maximum value of 'j-weight' considering all values from '1 to ith'. 
So if we consider 'wi' (weight in 'ith' row) we can fill it in all columns which have 'weight values > wi'. 

    # Build table K[][] in bottom up manner. bottom up means start with 1 element and 0 weight for W
    for i in range(n + 1):
        for w in range(W + 1):
            if  i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    W = 5
    items = {1: 60, 2: 100, 3: 120}      # weight: value dictionary
    wt  = [1,2,3]
    val = [60,100,120]

STEPS:
  - initialize K to 0 across W as column (0-W) and wt as row (0, 1,2,3)
  - loop over rows (i), that is values of wt
    i = 0
    for w in rangeW [loop over columns]
    set all to 0

      0   1   2   3   4   5 (w)
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0|  0|  0|  0|  0|  0|
    |
    V

  - i = 1, first value of wt! 
    for w in rangeW [loop over columns], first value is 0
    for w = 1 ask if wt[0 (i-1)] <= w
    wt[0] == 1 is == to w (1)
        K[1][1] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
        K[1][1] = max(60 + K[0][0], K[0][1]) = 60


      0   1   2   3   4   5 (w)
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0| 60|  0|  0|  0|  0|
    |
    V

    w = 2
    for w = 2 ask if wt[0 (i-1)] <= w
    wt[0] == 1 is < to w (2)
        K[1][2] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
        K[1][2] = max(60 + K[0][1], K[0][2]) = 60


      0   1   2   3   4   5 (w)
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0| 60| 60| 60| 60| 60|
    |
    V

    PHYSICAL MEANING: if only 1 is allowed, the value remains constant across w (60)

  - i = 2
    for w = 1 ask if wt[1 (i-1)] <= w
    wt[1] == 2 is > to w (1)
        K[i][w] = K[i-1][w]
        K[2][1] = K[1][1] = 60


      0   1   2   3   4   5 (w)
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0| 60| 60| 60| 60| 60|
  2 |  0| 60|  0|  0|  0|  0|
 (i)|  0|
    V


      0   1   2   3   4   5 (w)
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0| 60| 60| 60| 60| 60|
  2 |  0| 60|100|160|160|160|
 (i)|  0|
    V

    PHYSICAL MEANING: with 1 already in the sack, when is it better to use 2 to replace, or add 2.

  - FINAL!
      0   1   2   3   4   5
    +---+---+---+---+---+---+-> W
  0 |  0|  0|  0|  0|  0|  0|
  1 |  0| 60| 60| 60| 60| 60|
  2 |  0| 60|100|160|160|160|
  3 |  0| 60|100|160|180|220|
    +---+---+---+---+---+---+
    |
    V

    '''
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    # Build table K[][] in bottom up manner. bottom up means start with 1 element and 0 weight for W
    for i in range(n + 1):
        for w in range(W + 1):
            if  i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    for row in K:
        print('|',end='')
        for col in row:
            print(f'{col:3d}',end='|')
        print()
    return K[n][W]
 

def knap0DP(W,wt,val,n):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    Knapsack problem has both properties (overlapping subproblems and optimal substructure) of a dynamic programming problem.     
    In the following recursion tree, K() refers 
    to knapSack(). The two parameters indicated in the
    following recursion tree are n and W.
    The recursion tree is for following sample inputs.
    wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}
                        K(n, W)
                        K(3, 2)  
                    /            \ 
                   /              \               
                K(2, 2)               K(2, 1)
            /       \                  /    \ 
          /           \              /       \
        K(1, 2)      K(1, 1)        K(1, 1)   K(1, 0)
        /   \         /   \              /       \
       /      \     /       \          /          \
    K(0, 2)  K(0, 1)  K(0, 1)  K(0, 0)  K(0, 1)   K(0, 0)
    Recursion tree for Knapsack capacity 2 
    units and 3 items of 1 unit weight.
    '''
    Item = namedtuple('Item', 'w v')    # more clear, for each Item use w as weight and v as value
    items = sorted([Item(w,v) for w,v in zip(wt,val)], key= lambda x:x[0]) # important to sort by weight
    print(items)
    K = [[0 for _ in range(W+1)] for _ in range(n)]
    # the first row(s) and first column can only be populated by the first element!
    # first row
    for w in range(items[0].w,W+1):
        K[0][w] = items[0].v
    # first columns, up to items[1].w 
    for e in range(n):
        for col in range(items[0].w ,items[1].w):
            K[e][col] = items[0].v
    # now we need to consider what happens when we add elements one by one.
    e = 1
    while e < n:
        for w in range(items[1].w,W+1):
            # we are in item[e], with items[e].w and item[e].v, trying to fill a sack of size w
            # if the item fits in the sack item[e].w <= w, the question is
            #       which one is more valuable, this one of the one already there, or can we fit both?
            # if it does not fit, nothing changes and the previous value (from the previous row) holds
            if items[e].w <= w:
                K[e][w] = max(  K[e-1][w],                          # what is already there for this size of knapsack?
                                K[e-1][w-items[e].w] + items[e].v ) # can we fit both??
            else:
                K[e][w] = K[e-1][w]
        e += 1
    i = 0
    print(f'weight->',end='')
    while i <= W:
        print(f'{i:3d}',end=' ')
        i +=1
    print(f'\n           +{"---+" * W}')
    r = 1
    for row in K:
        print(f'item {r:02d}',end=' ')
        for col in row:
            print(f'{col:3d}',end='|')
        print()
        r += 1
    print(f'           +{"---+" * W}')
    return 0 # K[n][W]


def knap(W,items, debug=True):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
    Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this 
    subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).
    '''
    if not items:
        return {}
    weights = [w for w in items.keys()]
    values  = [v for v in items.values()]
    # if all fit in W sum values!
    if sum(weights) <= W:
        return ([(k,v) for k,v in items.items()], sum(values))
    # print(weights,values) if debug else None
    # we consider a presence vector where each element can be present or not
    maxV = 0
    bestOption = None
    for option in subsets(len(weights)):
        w = 0 
        v = 0
        for case in zip(option,weights,values):
            w += case[1] if case[0] else 0
            v += case[2] if case[0] else 0
        # print(f'option {option} {w} {v}') if w <= W else None
        if v > maxV and w <= W:
            bestOption, maxV = option, v
    res  = [(weights[i],values[i]) for i,x in enumerate(bestOption) if x]
    resW = sum([r[0] for r in res])
    print(W,resW)
    return (res, maxV, resW, W)

def countSetBits(n):
    if (n == 0):
        return 0
    else:
        return 1 + countSetBits(n & (n - 1))

def knap2(W,items, debug=True):
    '''
    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
    In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
    Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this 
    subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).
    '''
    if not items:
        return {}
    weights = [w for w in items.keys()]
    values  = [v for v in items.values()]
    # if all fit in W sum values!
    if sum(weights) <= W:
        return ([(k,v) for k,v in items.items()], sum(values))
    # order by weight
    oW = sorted(weights)
    # print(oW) if debug else None
    remainWmin  = W
    remainWmax  = W
    i = len(oW) - 1
    j = 0
    minW = 0
    maxW = 0
    while i >= 0:
        if oW[i] <= remainWmin:
            remainWmin  -= oW[i]
            minW += 1
        if oW[j] <= remainWmax:
            remainWmax  -= oW[j]
            maxW += 1
        i  -= 1
        j  += 1
    minInt = (1 <<minW) -1
    maxInt = ((1 <<maxW) - 1) << (len(oW)-maxW)
    print(f'at least bits set {minW} {maxW} {minInt:0{len(oW)}b} {maxInt:00{len(oW)}b}')
    validCombinations = [f'{x:0{len(oW)}b}' for x in range(minInt,maxInt+1) if countSetBits(x) in range(minW,maxW+1)]
    # print(validCombinations)
    maxValue = 0
    bestComb = None
    for c in validCombinations:
        cValue  = sum([values[x]  for x,xdigit in enumerate(c) if xdigit == '1'])
        cWeight = sum([weights[x] for x,xdigit in enumerate(c) if xdigit == '1'])
        if cWeight > W:
            continue
        if cValue > maxValue:
            bestComb = c
            maxValue = cValue
            print(c,maxValue)
    res  = [(weights[x],values[x]) for x,xdigit in enumerate(bestComb) if xdigit == '1']
    resW = sum([r[0] for r in res])
    print(W,resW)
    return (res,maxValue, resW,W)


W = 30
items = {3: 60, 4:65, 5:70, 8: 100, 10:140, 12: 120, 20: 200}      # weight: value dictionary

# items = { random.randint(1,40): random.randint(50,300) for _ in range(25)}
# W = sum([w for w in items.keys()]) - 20
# problem statement: put these items in a knapsack of capacity W to get the maximum total value in the knapsack
startK = datetime.datetime.now()
print(knap0DP(W,[x for x in items.keys()],[x for x in items.values()],len(items)))
startK2 = datetime.datetime.now()
print(knap2(W,items))
startK3 = datetime.datetime.now()
print(knap0(W,[x for x in items.keys()],[x for x in items.values()],len(items)))
end = datetime.datetime.now()
print(f'executing for {W} {len(items)} --- time: {(startK2-startK).total_seconds()},{(startK3-startK2).total_seconds()},{(end-startK3).total_seconds()}')