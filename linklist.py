class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values=None):
        self.elements = 0
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def __len__(self):
        return self.elements
    
    def __iter__(self):
        current = self.head
        loop    = 0	
        while current:
            loop += 1
            yield current
            current = current.next
            if loop > self.elements:
               current = None
               print('LOOP!')
            
    @property
    def values(self):
        return [node.value for node in self]
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.elements += 1
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)
            
    def add_node_as_head(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        self.elements += 1
        return self.head

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return slow_p
        return None
  

myLL = LinkedList(['a','b','c'])
myLL.add_multiple_nodes(['d','e','f'])
myLL.tail.next = myLL.head
#myLL.tail.next = myLL.head.next.next
print(f'{myLL} loop at: {myLL.detectLoop()}')
