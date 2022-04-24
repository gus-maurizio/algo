import random

def perms(l):
    '''
    given l, a list of different things, return all the possible permutations of elements of l
    [a] -> [[a]]
    [a,b] -> [[a,b],[b,a]]
    '''
    if len(l) == 1:
        return [[l[0]]]
    i = 0
    result = []
    while i < len(l):
        e = l[i]
        _p = permutations(l[:i]+l[i+1:])
        result += [ [e] + _e for _e in _p ]
        i += 1
    return result

def permutations(l):
    '''
    given l, a list of different things, return all the possible permutations of elements of l
    [a] -> [[a]]
    [a,b] -> [[a,b],[b,a]]
    '''
    if len(l) == 1:
        yield [l[0]]
    i = 0
    while i < len(l):
        e = l[i]
        _p = permutations(l[:i]+l[i+1:])
        yield from [ [e] + _e for _e in _p ]
        i += 1

def combinations(l):
    '''
    given l, a list of different things, return all the possible combinations of elements of l [2^n]
    []  -> [[]]
    [a] -> [[],[a]]
    [a,b] -> [[],[a],[b],[a,b]]
    '''
    # print(l)
    if len(l) == 0:
        return [[]]
    if len(l) == 1:
        return [[l[0]], []]
    i = 0
    while i < len(l):
        e = l[i]
        # print(e,l[:i]+l[i+1:])
        _c = combinations(l[i+1:])
        return sorted(([[e] + x for x in _c] + _c),key=lambda x:len(x))
        i += 1


l = ['a','b','c','d']
# print(list(permutations(l)))
print(combinations(l))

# items = { random.randint(1,40): random.randint(50,300) for _ in range(10)}
