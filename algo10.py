def comb(l,iteration = 1):
    print(iteration,l)
    iteration += 1
    if len(l) == 1:
        return [l[0]]
    _c = comb(l[:-1],iteration)
    return [l[-1]] + [l[-1]+i for i in _c] + _c

def perm(l,iteration = 1):
    print(iteration,l)
    iteration += 1
    if len(l) == 1:
        return [l[0]]

    return [l[i]+j for i in range(len(l)) for j in (perm(l[:i]+l[i+1:],iteration) if len(l[:i]+l[i+1:]) > 1 else l[:i]+l[i+1:])]

def chessHorse(N, PosX=0, PosY=0, iteration = 1):
    _board = [[0 for i in range(N)] for _ in range(N)]
    _board[PosX][PosY] = 1
    def covered(board,N):
        return all([board[i][j] > 0 for i in range(N) for j in range(N)])

    def moves(board,N):
        for i in range(N):
            for j in range(N):
                print(f'| {board[i][j]:3d} ',end='')
            print('|')

    def reachable(PosX, PosY, board, N):
        ''' list of reachable positions for a horse in PosX,PosY
            horse can move 2 away (NSEW) and 1 in perpendicular direction
        '''
        allowed  = []
        for i in [[-2,-1], [-2,1], [2,-1], [2,1], [-1,-2], [-1,2], [1,-2], [1,2]]:
            dX,dY = i
            if PosX+dX >= 0 and PosX+dX < N and PosY+dY >= 0 and PosY+dY < N and board[PosX+dX][PosY+dY] == 0:
                allowed.append([PosX+dX,PosY+dY])
        return allowed

    def nextPosition(PosX,PosY,board,N):
        '''
        horse should move to an allowed next position that has minimal covered positions from it
        '''
        score = {}
        for p in reachable(PosX,PosY,board,N):
            score[tuple(p)] = len(reachable(p[0],p[1],board,N))
        # print(score)
        return min(score, key=score.get) if score else None

    # print(_board, covered(_board,N),reachable(2,2,_board,N))
    print((PosX,PosY), end='')
    nPos = nextPosition(PosX,PosY,_board,N)
    while nPos:
        print(' -> ',nPos, end='')
        _board[nPos[0]][nPos[1]] = _board[PosX][PosY] + 1
        PosX, PosY = nPos
        nPos = nextPosition(PosX,PosY,_board,N)
    print()
    moves(_board,N)
    return covered(_board,N)


def knapsack(W,weight):
    '''
    items is a structure of weight: value (unlimited)
    Put items so that sum(weight) <= W and maximize value
    '''
    _weight = sorted(weight.items(), key = lambda x: x[1]/x[0] )
    options = {}
    value   = {}
    print(_weight)
    for i in range(len(_weight)):
        # print(_weight[:i+1])
        j = i
        amount = W
        value[tuple(_weight[:i+1])]  = 0 
        options[tuple(_weight[:i+1])] = {}
        while j >= 0 and amount > 0:
            w,v = _weight[j]
            q   = amount // w 
            r   = amount %  w
            print(f'...... {(w,v)} {q} r:{r} value:{q*v}')
            value[tuple(_weight[:i+1])] += q*v
            amount = r
            options[tuple(_weight[:i+1])][tuple(_weight[j])] = q
            j -=1
        print(f'>>> {_weight[:i+1]} r:{r} value:{value[tuple(_weight[:i+1])]} {options[tuple(_weight[:i+1])]}')
    
    maxValueKey = max(value,key=value.get)
    maxValue    = value[maxValueKey]
    print(f'+++ {maxValue} {options[maxValueKey]}')

# print(sorted(comb(list('zyx'))))
# print(sorted(perm(list('zyx'))))

# print(chessHorse(5))

knapsack(50,{10: 60, 20: 140, 30: 190})