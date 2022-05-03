from collections import namedtuple
import random,sys

doc_knights = '''
Algorithms to analyze chess knights moves
'''

class ChessBoard:
    Move = namedtuple('Move',['x','y','label'])
    AllowedMoves =  [ (2,1),(2,-1),(-2,1),(-2,-1), (1,2),(1,-2),(-1,2),(-1,-2), ]

    def __init__(self, n=8):
        self.size   = n
        self.board  = [ [-1] * n for _ in range(n)]
        self.moves  = []
    
    def reset(self):
        self.board  = [ [-1] * self.size for _ in range(self.size)]

    def print(self):
        for col in range(self.size):
            print('\n+' + '----+' * self.size)
            print('|', end='')
            for row in range(self.size):
                print(f'{self.board[col][row]:3d} |', end='')
        print('\n+' + '----+' * self.size)

    def printMoves(self):
        for m in self.moves:
            print(f' [{m.label}]: ({m.x},{m.y})',end=' -> ')
        print('done!')

    def history(self):
        print(f'Move history: {self.moves}')

    def place(self,x,y,label=0):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and self.board[x][y] == -1:
            self.board[x][y] = label
            self.moves.append(self.Move(x,y,label))
            return True
        return False

    def clearPos(self,x,y,label=0):
        self.board[x][y] = -1


    def possible(self,x,y):
        possiblePos = []
        for (dx,dy) in self.AllowedMoves:
            if x+dx >= 0 and x+dx < self.size and y+dy >= 0 and y+dy < self.size and self.board[x+dx][y+dy] == -1:
                possiblePos.append((x+dx,y+dy))
        return possiblePos

    def isCovered(self):
        return all(self.board[x][y] >= 0 for x in range(self.size) for y in range(self.size))

    def canCover(self,x,y,move=0):
        # can we cover the whole board from position x,y
        if self.place(x,y,label=move):
            nextPos = self.possible(x,y)
            for p in nextPos:
                if not self.canCover(p[0],p[1],move+1):
                    board.clearPos(p[0],p[1],move+1)
                    continue      
        return self.isCovered()

    def canCoverHeuristic(self,x,y,move=0):
        # can we cover the whole board from position x,y
        if self.place(x,y,label=move):
            nextPos = self.possible(x,y)
            # choose the nextPos with minimal nextPos of nextPos alternatives
            score     = [len(self.possible(np[0],np[1])) for np in nextPos]
            sortPos   = sorted(zip(nextPos,score), key = lambda x: x[1])
            for pz in sortPos:
                p = pz[0]
                if not self.canCoverHeuristic(p[0],p[1],move+1):
                    board.clearPos(p[0],p[1],move+1)
                    continue      
        return self.isCovered()

    def queens(self,i=0,p=[],q=set(),u=set(),v=set()):
        '''
        basically finds all permutations (stored in a vector/list where each position represents a column and the number the row the queen is in)
        but filters each member for not being in identified upwards/downwards diagonals.
        '''
        if i < self.size:
            for j in range(self.size):
                if j not in q and i+j not in u and i-j not in v:
                    yield from self.queens(i+1,p+[j],q | {j},u | {i+j},v | {i-j})
        else:
            yield p

board = ChessBoard(int(sys.argv[1]) if len(sys.argv) > 1 else 6)
board.reset()

cancover = board.canCoverHeuristic(int(sys.argv[2]) if len(sys.argv) > 2 else 0,int(sys.argv[3]) if len(sys.argv) > 3 else 0)
print(f'The board ({board.size}x{board.size}) can be covered: {cancover}')
board.print()
print(len(board.moves), 'moves attempted')
if cancover:
    board.printMoves()

solutions = 0
print("\nAttempting to find solutions to friendly queens...")
for i in board.queens():
    print(f'{solutions:3d} {i} each column indicates row position for that column') if solutions < 20 else None
    solutions += 1
print(f'Board of {board.size:d}x{board.size:d} has {solutions:,d} solutions')
