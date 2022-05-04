import random,sys

def p(n=4,i=0,a=[]):
    if i < n:
        for j in range(n):
            if j not in a:
                yield from p(n,i+1,a+[j])
    else:
        yield a

def c(n=4,m=2,i=0,a=[]):
    if not ('u' in globals()):
        global u 
        u = set()
    if i < n and len(a) < m:
        for j in range(n):
            if j not in a:
                yield from c(n,m,i+1,a+[j])
    else:
        if frozenset(a) not in u:
            u.add(frozenset(a))
            yield a

def subsets(n=4):
    masks = [1 << i for i in range(n)]
    alle  = list(range(n))
    for i in range(1 << n):             # loop 2**n times with bit shift from 0 to 2**n. n bits from all 0 to all 1 (2**n-1)
        yield [ss for mask, ss in zip(masks, alle) if i & mask]

def subsetsm(n=4,m=2):
    # return only subsets of size m (Exactly)
    masks = [1 << i for i in range(n)]
    alle  = list(range(n))
    for i in range(1 << n):             # loop 2**n times with bit shift from 0 to 2**n. n bits from all 0 to all 1 (2**n-1)
        a = [ss for mask, ss in zip(masks, alle) if i & mask]
        if len(a) == m:
            yield a

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

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
m = int(sys.argv[2]) if len(sys.argv) > 2 else (n-1)

print('permutations ',list(p(n)))
print('combinations ',list(c(n,m)))
print('all subsets  ',list(subsets(n)))
print('subsets n,m  ',list(subsetsm(n,m)))
print('powerset     ',list(powerset(n)))


