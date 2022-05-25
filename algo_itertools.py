from algo_queens import combinations

from itertools import permutations, combinations,combinations_with_replacement

a='abc'
pset = [''.join(list(x)) for i in range(len(a)+1) for x in combinations(a,i)]
p    = [''.join(list(x)) for x in permutations(a)]
c    = [''.join(list(x)) for x in combinations(a,2)]