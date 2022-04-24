import random

class Counter:
    def __init__(self, name: str):
        self.value = 0
        self.name  = name
    
    def increment(self, delta = 1):
        self.value += delta

    def tally(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f'{self.name}: {self.value}'

    def __repr__(self) -> str:
        return f'{{"{self.name}": {self.value}}}'




myList = [0,1,5,6,7,10,12,14,15,17,20,22]
value  = 12

def binSearch(myList: list[int], value: int) -> int:
    head = 0
    tail = len(myList) - 1
    while (head <= tail):
        print(head,tail, len(myList))
        mid = int(head + (tail - head) / 2)
        if      value == myList[mid]:
            return mid
        elif    value < myList[mid]:
            tail = mid - 1
        elif    value > myList[mid]:
            head = mid + 1
    return -1

def binSearch2(myList: list[int], value: int) -> int:
    head = 0
    tail = len(myList) - 1
    while (head <= tail):
        if value < myList[head] or value > myList[tail]:
            return -1
        print(head,tail, value, myList[head], myList[tail])
        mid  = int(head + (tail - head) / 2)
        midl = int(head + (mid -  head) / 2)
        midh = int(mid +  (tail - mid)  / 2)
        if      value == myList[head]:
            return head
        elif    value == myList[midl]:
            return midl
        elif    value == myList[mid]:
            return mid
        elif    value == myList[midh]:
            return midh
        elif    value == myList[tail]:
            return tail
        elif    value < myList[midl]:
            tail = midl - 1
            head = head + 1
        elif    value < myList[mid]:
            tail = mid  - 1
            head = midl + 1
        elif    value < myList[midh]:
            tail = mid  - 1
            head = midl + 1
        else:
            tail = tail - 1
            head = midh + 1
    return -1



myList = [i for i in range(1,9000,3)]
value = random.randint(0,myList[-1])
# isThere = binSearch(myList, value)
isThere = binSearch2(myList, value)
print(isThere)

# ctr = Counter('mean')
# ctr.increment(delta = 2)
# print(repr(ctr), ctr.tally())