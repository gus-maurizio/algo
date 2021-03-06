from collections import namedtuple
import random

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


board = ChessBoard(6)
board.reset()
board.print()
print(board.possible(0,0))

print(board.canCoverHeuristic(0,0))
board.print()