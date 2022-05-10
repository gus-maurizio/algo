import random,sys

def quickSort(a,l,r,debug=False):

    def median3(arr,a,b,c):
        if ((arr[a] > arr[b]) ^ (arr[a] > arr[c])):
            return a
        elif ((arr[b] < arr[a]) ^ (arr[b] < arr[c])):
            return b
        else:
            return c

    def _partition(a,l,r):
        # choose partition value and swap with last!
        # p = random.randint(l,r)
        p = median3(a,l,l+(r-l)//2,r)
        a[p],a[r] = a[r],a[p]
        # pivot is last value
        p = r
        i = highmark = l
        while i < r:
            if a[i] < a[p]:
                a[i],a[highmark] = a[highmark], a[i]
                highmark += 1
            i += 1
        a[p],a[highmark] = a[highmark],a[p]
        return highmark

    if l < r:
        p = _partition(a,l,r)
        print(f'--> [{l}:{r}] p:{p} <{a[p]}> {a[l:r+1]}') if debug else None
        quickSort(a,p+1,r,debug)
        quickSort(a,l,p-1,debug)

# P = [10,20,30,40,50,42,31,21,41]
# P = [random.randrange(5000) for _ in range(500)]
# P = [1 for _ in range(5)]
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50
P = [random.randrange(3*N) for _ in range(N)]
print(f'P:{P} qsort n:{len(P)}') #,end=' ')
quickSort(P,0,len(P)-1,debug=False)
print(f'result:{P}')