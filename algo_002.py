class Node:
    def __init__(self, value):
        self.left   = None
        self.right  = None
        self.value  = value

    def __str__(self):
        answer = ""
        if self.left:
            answer += str(self.left) + ", "
        answer += str(self.value)
        if self.right:
            answer += ", " + str(self.right)
        return answer

    def add(self, value):
        if self.value == value:
            return
        if value < self.value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.add(value)

    def find(self, value):
        answer = False
        if      value == self.value:
            answer = True
        elif    self.left and value < self.value:
            # print(value,"left", self.value)
            answer = self.left.find(value)
        elif    self.right and value > self.value: 
            # print(value,"right", self.value)
            answer = self.right.find(value)
        return answer



root = Node("m")
root.add("b")
root.add("a")
root.add("c")
root.add("k")
root.add("m")
root.add("z")
root.add("y")
# root.right  = Node("c")
print(root)
print(root.find("p"))