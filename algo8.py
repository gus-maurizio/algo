class Node:
    def __init__(self,data,isLeaf=False):
        self.data   = data
        self.isLeaf = isLeaf
        self.left   = None
        self.right  = None
    
    def __repr__(self) -> str:
        if self.isLeaf:
            return repr(self.data)
        else:
            return repr(self.left) + ' ' + (self.data + ' ' + repr(self.right) if self.right else '')

class Solution:
    #   [0 +] A + B * C * D - E
    #        (+)----(+)----(-)
    #        /      /      / \
    #      <0>    <A>    (*) <E>
    #                   /   \
    #                 <B>   (*)
    #                       / \
    #                     <C> <D>


    def expressionTree(self, S_, debug = True):
        topOperators = ['+','-']
        botOperators = ['*','/']

        s = S_.replace(' ','')
        print(f'{s}') if debug else None
        # create root with 0 + 
        root        = Node('+')
        root.left   = Node(0, isLeaf=True)
        currOperand     = None
        currOperator    = '+'
        currTopNode     = root
        currBotNode     = None
        for c in s:
            if   c.isalpha():
                currOperand = c
                # print(currOperand,currOperator) if debug else None
            elif c in topOperators:
                # add the next top level operator to the right of currTopNode
                if currOperator in topOperators:
                    currOperator            = c
                    currTopNode.right       = Node(currOperator)
                    # print(currOperand,currOperator) if debug else None
                    currTopNode.right.left  = Node(currOperand,isLeaf=True)
                    currTopNode             = currTopNode.right
                else:
                    currBotNode.right       = Node(currOperand,isLeaf=True)
                    currOperator            = c
                    currTopNode.data        = c     # fix the operator + added by previous botOperator
            elif c in botOperators:
                # add the next top level operator to the right of currTopNode if first botOperator
                if currOperator in topOperators:
                    currTopNode.right   = Node('+')  # maybe a -? would have to backtrack on this one...
                    currTopNode         = currTopNode.right # move top
                    currOperator        = c
                    currTopNode.left    = Node(currOperator)
                    currBotNode         = currTopNode.left
                    currBotNode.left    = Node(currOperand,isLeaf=True)
                elif currOperator in botOperators:
                    currOperator        = c
                    currBotNode.right   = Node(currOperator)
                    currBotNode         = currBotNode.right
                    currBotNode.left    = Node(currOperand,isLeaf=True)
                currOperator            = c
                   
        # we are left with the last operand
        if  currOperator in topOperators:
            currTopNode.right = Node(currOperand,isLeaf=True)
        elif currOperator in botOperators:
            currBotNode.right = Node(currOperand,isLeaf=True)
        #
        print(repr(root)) if debug else None
        return repr(root)


# S = f'A + B + C - E' # ' * D - E'
S = f'A * B * C * D - E + F - G * H / I'

# S = ' 5 + 4 '

# S = ' 3 * 5 + 4 '
# S = ' 3 * 5 * 2'
# S = ' 3 * 1 * 1 + 5 + 4 - 2 * 5'
print(Solution().expressionTree(S,debug=True))

