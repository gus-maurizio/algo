import random,math

def buildHeap(arr,n):
    '''
    builds a max heap with arr elements
    '''
    h = []
    # n = len(arr)
    if n <= 1:
        h = [x for x in arr]
        return h
    # adding to heap happens by adding (right) and balancing
    i = 0
    z = 0
    while i < n:
        h.append(arr[i])
        # is the heap property maintained?
        # element at i needs to be lower than parents!
        p = (i - 1) // 2    # compute parent
        j = i               # this child
        # print(f'j:{j} p:{p}: {h[j]} > {h[j]}')
        z += 1
        while (p >= 0):
            if h[j] > h[p]:
                h[j], h[p] = h[p], h[j]
            j = p
            p = (p - 1) // 2
            z += 1
        i += 1
    print(f'--- n:{n} O(n*logn): {n*int(math.log2(n)):d} iters:{z}')
    return h

P = [1,2,3,4,5,6,7]
# a balanced heap has 1 + 2 + 4 + 8 + ... 1,3,7,15 2**N-1
# P = [random.randrange(0,100) for _ in range(2**6 - 1)]
H = buildHeap(P,len(P))
print(f'{P}: {H}')

while len(H)>0:
    print(f'<{H[0]}>', end=' ')
    H = buildHeap(H[1:],len(H[1:]))
print()


#             92
#      86                 88 
#  54       85       59       66
# 0  36   13 34    8   24   12  66