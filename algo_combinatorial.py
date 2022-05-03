import random

def p(n=4,i=0,a=[]):
    if i < n:
        j = 0
        while j < n:
            if j not in a:
                yield from p(n,i+1,a+[j])
            j += 1
    else:
        yield a


def c(n=4,m=2,i=0,a=[]):
    if not ('u' in globals()):
        global u 
        u = set()

    if i < n and len(a) < m:
        j = 0
        while j < n:
            if j not in a:
                yield from c(n,m,i+1,a+[j])
            j += 1
    else:
        if frozenset(a) not in u:
            u.add(frozenset(a))
            yield a

def subsets(n=4):
    masks = [1 << i for i in range(n)]
    alle  = list(range(n))
    for i in range(1 << n):             # loop 2**n times with bit shift from 0 to 2**n. n bits from all 0 to all 1 (2**n-1)
        yield [ss for mask, ss in zip(masks, alle) if i & mask]

def powerset(n=4):
    if n == 0:
        yield set()
    elif n == 1:
        yield set()
        yield {n}
    else:
        for item in powerset(n-1):
            yield {n} | item
            yield item


print('permutations ',list(p(3)))
print('combinations ',list(c(3,2)))
print('all subsets  ',list(subsets(3)))
print('powerset     ',list(powerset(3)))


