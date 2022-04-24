import random
class Node():
    def __init__(self, value: object):
        self.value  = value
        self.next   = None
        self.prev   = None
    
    def __str__(self) -> str:
        answer = f'node: {self.value} -> '
        if self.next:
            answer += str(self.next)
        return answer

    def back(self) -> str:
        answer = f'bnode: {self.value} <- '
        if self.prev:
            answer += self.prev.back()
        return answer


class LinkedList:
    def __init__(self, name: str = ''):
        self.name = name
        self.head = None
        self.tail = None
        self.len  = 0

    # head and tail point to first and last element or are both None

    def ladd(self, value: object):
        # creates a node, links the nodes if they exist on the left side
        node = Node(value)
        if not self.head:
            # print(f'add {node}')
            self.head = node
            self.tail = node
        else:
            # print(f'ladd {value}')
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.len += 1

    def lpop(self) -> object:
        node = self.head
        if self.head:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            if self.tail == node:
                self.tail = None
        self.len -= 1
        return node

    def radd(self, value: object):
        node = Node(value)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.len += 1

    def rpop(self) -> object:
        node = self.tail
        if self.tail:
            if self.tail.prev: 
                self.tail.prev.next = None 
            self.tail = self.tail.prev 
            if self.head == node:
                self.head = None
        self.len -= 1
        return node.value

    def __str__(self) -> str:
        if self.head:
            return f'{str(self.head)}'

    def back(self) -> str:
        if self.tail:
            return f'{self.tail.back()}'


    def elements(self) -> int:
        return self.len


stack = LinkedList()
stack.ladd('b')
stack.ladd('a')
stack.radd('c')
print(stack)
# stack.rpop()
stack.rpop()
stack.rpop()
stack.rpop()
print(stack.back(), stack.elements())
# print(stack)
