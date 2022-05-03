import random, math, statistics

def median_nosort(arr) -> int:
    '''
    Find the position of median that splits in 2 subarrays 
    '''
    def _computeMean(a,n,value):
        above = below = equal = sumval = 0
        i = 0
        while i < n:
            sumval += a[i]
            if  a[i] < value:
                below += 1
            elif a[i] == value:
                equal += 1
            else:
                above += 1
            i += 1
        return (sumval//n, below, equal, above)

    def _testMedian(a,n,guess):
        print('>>',n,guess)
        above = below = equal = 0
        valBelow = valAbove = None
        i = 0
        while i < n:
            # first count how many compared to guess
            if  a[i] < guess:
                below += 1
            elif a[i] == guess:
                equal += 1
            else:
                above += 1
            # secondly, which values are closest to guess from below and above
            if  a[i] < guess:
                if (valBelow == None or a[i] > valBelow):
                    valBelow = a[i]
            elif a[i] > guess:
                if valAbove == None or a[i] < valAbove:
                    valAbove = a[i]
            # loop
            i += 1
        return (below, equal, above, valBelow, valAbove)

    n = len(arr)
    # do a first pass to compute mean and see how many values are above and below a midpoint
    med = P[n//2]
    mean, below, equal, above = _computeMean(P,n,med)
    print(f'first pass: {mean} {below},{equal},{above}')
    # there are three options:
    # we found it (meaning below and above are close enough)
    # or decide between starting with mean or the randomly selected med
    if abs(above - below) >=  4:
        med = mean
    iter = 1
    while abs(below - above) >= n%2+1 and iter < n//2:
        # the value med was close enough! 
        # there are 
        below, equal, above, valB, valA = _testMedian(P,n,med)
        print(f'iteration: {iter} [{below},{equal},{above}] {valB} {valA}')
        if  below < above:
            med = valA
        elif below > above:
            med = valB
        iter += 1
    # reorder the array now
    i = 0 
    answer = [x for x in arr if x < med] + [x for x in arr if x == med] + [x for x in arr if x > med]
    return (med, answer)






# P = [1,2,3,4,5,6,7,8,9]
# P = [1,2,3,4,5,6,7,8,90]
# P = [1,2,3,4,2,6,7,80,90,100]
P = [random.randrange(0,100) for _ in range(20)] + [2000,54,54]
# P = [0, 1, 3, 4, 9, 13, 18, 28, 39, 41, 46, 48, 50, 52, 53, 60, 61, 79, 79, 80]

(med,answer) = median_nosort(P)
print(f'array:{P} median:{med} answer: {answer} {sum([1 for x in answer if x < med])}:{sum([1 for x in answer if x > med])}')