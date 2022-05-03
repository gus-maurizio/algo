def permutations(n,i=0,p=[]):
    if i < n:
        for j in range(n):
            if j not in p:
                print(f'> {i} {j} {p}')
                yield from permutations(n,i+1,p+[j])
    else:
        print(f'>>> {i} {p}')
        yield p

u = []
def combinations(n,m,i=0,c=[]):
    global u
    if i < n and len(c) < m:
        for j in range(n):
            if j not in c:
                yield from combinations(n,m,i+1,c+[j])
    else:
          if frozenset(c) not in u:
            u.append(frozenset(c))
            yield c

def queens(n,i=0,q=[],u=[],v=[]):
    '''
    basically finds all permutations (stored in a vector/list where each position represents a column and the number the row the queen is in)
    but filters each member for not being in identified upwards/downwards diagonals.
    Diagonal properties...
    00100
    01000
    00100
    00010

    column 0 has no elements, column 1 has element in row 1. Downward diagonal ([1,1]->[2,2->[3,3]]) has col-row constant (0)
    Upward diagonal ([1,1]->[2,0]]) has col+row constant (2)

    Diagonal coordinate system (as opposed to the cartesian col/row)
    +------------------------> col
    |/// \\
    |// X \\
    |/     \\
    |
    V
    row
    [u,v] [col+row,col-row]
    [0,0] -> [0,0]  [1,0] -> [1,-1]
    [0,1] -> [1,1]  [1,1] -> [2,0]
    [0,2] -> [2,2]  [1,2] -> [3,1]
    [0,x] -> [x,x]  [1,x] -> [1+x,x-1]
    '''
    if i < n:
        for j in range(n):
            if j not in q and i+j not in u and i-j not in v:
                yield from queens(n,i+1,q+[j],u + [i+j], v + [i-j])
    else:
        yield q

def queensOpt(n,i=0,p=[],q=set(),u=set(),v=set()):
    '''
    basically finds all permutations (stored in a vector/list where each position represents a column and the number the row the queen is in)
    but filters each member for not being in identified upwards/downwards diagonals.
    '''
    if i < n:
        for j in range(n):
            if j not in q and i+j not in u and i-j not in v:
                yield from queensOpt(n,i+1,p+[j],q | {j},u | {i+j},v | {i-j})
    else:
        yield p

def test(n,i=0,d=set()):
    if i < n:
        d.add(i)
        yield from test(n,i+1,d)
    else:
        yield d
# for t in test(3):
#     print(t)

board = 5
solutions = 0
for i in queensOpt(board):
    print(f'{solutions:3d} {i}')
    solutions += 1
print(f'Board of {board:d} has {solutions} solutions')
