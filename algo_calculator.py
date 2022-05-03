import random

doc_calculator = '''
Process a string with numbers, addition and multiplication and give the result
2 * 3 + 4 -> 10
'''

'''
1 * 2  + 4 * 5 + 2
'+' , '*' , 1 , 2 , '+' , '*' , 4 , 5 , 2 , 

'+' , '*' , 1 , 2 , '+' , '*' , 4 , 5 , '+' , '*' , 2 , 7 , '*' , 10 , 20 , 
 1 * 2  + 4 * 5 + 2 * 7 + 10 * 20

'+' , '*' , 1 , 2 , '+' , '*' , 4 , 5 , '+' , '*' , 2 , '*' , 7 , 4 , '*' , 10 , 20 , 
 1 * 2  + 4 * 5 + 2 * 7 * 4 + 10 * 20  

'''

class Node:
    def __init__(self,value,l=None,r=None):
        # print(f'INIT {value} l:{l} r:{r}')
        self.value = value
        self.left  = l
        self.right = r

    def compute(self):
        if self.left == None and self.right == None:
            return self.value
        if self.value  == '+':
            return self.left.compute() + self.right.compute()
        if self.value  == '*':
            return self.left.compute() * self.right.compute()
        return -9999

    def BFS(self):
        print(repr(self.value),',',end=' ')
        if self.left:
            self.left.BFS()
        if self.right:
            self.right.BFS()


def buildTree(e,l,r):
    n = r - l + 1       # number of elements in list e
    if   n <= 1:
        return Node(e[l])
    elif n == 3:
        root = Node(e[l+1],Node(e[l]),Node(e[r]))
        return root 
    # more than 3 we need to find all the lower precedence operators (+)
    if '+' in e[l:r+1]:
        p = e[l:r].index('+')
    else:                       # only low priority elements!
        p = e[l:r+1].index('*')    
    root = Node(e[l+p],buildTree(e,l,l+p-1),buildTree(e,l+p+1,r))
    return root

def makelist(s):
    n = len(s)
    i = 0
    l = []
    operand = 0
    while i < n:
        if   s[i].isdigit():
            operand = 10 * operand + int(s[i])
        elif s[i] in ['*','+']:
            l.append(operand)
            l.append(s[i])
            operand = 0
        i += 1
    l.append(operand)
    return l

def calculator(s):
    # clean and store in list
    n = len(s)
    l = makelist(s)
    # now build the expression tree
    # + has precedence, so find all the + in every odd position!
    root = buildTree(l,0,len(l)-1)
    root.BFS()
    print()
    return root.compute()


P = ' 1 * 2  + 4 * 5 + 2 * 7 * 4 + 10 * 20'
print(P,' computed value: ',calculator(P),' is equal to ',eval(P))