from pprint import pp
import random

def selectionSort(l):
    print(l)
    iters = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            iters += 1
            if l[j] < l[i]:
                l[i],l[j] = l[j],l[i]
    print(iters,len(l)*(len(l)-1)//2)
    return l

def insertionSort(l):
    print(l)
    iters = 0
    for curr in range(1,len(l)):
        val = l[curr]
        i   = curr - 1
        while i >= 0:
            iters += 1
            if l[i] > val:
                l[i],l[i+1] = val,l[i]
            else:
                break
            i -= 1

    print(iters)
    return l

def quickSort(l):
    if len(l) <= 1:
        return l
    if len(l) == 2:
        return [l[0],l[1]] if l[0] < l[1] else [l[1],l[0]]
    pivotIx  = len(l)-1
    pivotVal = l[pivotIx]
    print('>>>',l,pivotIx,pivotVal)
    left  = [l[i] for i in range(len(l)) if l[i] < pivotVal]
    right = [l[i] for i in range(len(l)) if l[i] >= pivotVal]
    print('+++', left, right)
    return quickSort(left) + quickSort(right)

def mergeSort(l):
    def _merge(l,r):
        print(f'merge {l} {r}')
        i = j = 0
        m = []
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                m.append(l[i])
                i += 1
            else:
                m.append(r[j])
                j += 1
        m.extend(l[i:])
        m.extend(r[j:])
        return m

    if len(l) == 1:
        return l
    if len(l) == 2:
        return [l[0],l[1]] if l[0] < l[1] else [l[1],l[0]]
    print(l)
    pivotIx  = len(l) // 2 
    left  = l[:pivotIx]
    right = l[pivotIx:]

    # print(left, right)
    left  = mergeSort(left)
    right = mergeSort(right)
    return _merge(left,right)

def selectionSortStable(l):
    print(l)
    iters = 0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            iters += 1
            if l[j].split('.')[0] < l[i].split('.')[0]:
                # swap makes sort unstable. try insert                
                # l[i],l[j] = l[j],l[i]
                val = l[j]
                l.insert(i,val)
                del l[j+1]
    print(iters,len(l)*(len(l)-1)//2)
    return l

def quickSortOpti(l):
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    if len(l) == 2:
        return [l[0],l[1]] if l[0] < l[1] else [l[1],l[0]]
    pivotIx  = len(l) // 2 
    pivotVal = l[pivotIx]
    print(id(l),l, pivotIx, pivotVal)
    # we try to avoid allocation and move in place
    # we bring the right elements starting in rightmost and advance from left
    topRight = len(l) -1
    i = 0
    while i < topRight:
        print('+++',i,topRight,l)
        if l[i] < pivotVal:
            i += 1
        else:
            # send to right - careful with current right that has not been evaluated yet
            l[i],l[topRight] = l[topRight],l[i]
            topRight -= 1
    print('>>>', l)
    return quickSortOpti(l[:pivotIx]) + quickSortOpti(l[pivotIx:])


L = [1,2,3,4,5,6,7,8,9,12,10,11]
# print('>>>',selectionSort(L[::-1]))
# print('>>>',selectionSort(L))

# print('>>>',insertionSort(L[::-1]))
# print('>>>',insertionSort(L))

# print('>>>',quickSort(L[::-1]))
# print('>>>',quickSort(L))

# print('>>>',mergeSort(L[::-1]))
# print('>>>',mergeSort(L))

L = [random.randint(1,100) for _ in range(30)]
# print(L)
# L = [22, 44, 66,3,1]
print('>>>',quickSort(L[::-1]))
# print('<<<>>>',quickSortOpti(L))


# L = ['01.0','07.1','11.2','07.3','07.4','01.5']
# print('>>>',selectionSortStable(L[::-1]))
# print('>>>',selectionSortStable(L))

