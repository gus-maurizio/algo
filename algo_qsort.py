import random

def quickSort(a,l,r,debug=True):
    def _partition(a,l,r):
        # choose partition value and swap with last!
        p = random.randint(l,r)
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
        quickSort(a,p+1,r)
        quickSort(a,l,p-1)

P = [10,20,30,40,50,42,31,21,41]
P = [random.randrange(5000) for _ in range(500)]
P = [1 for _ in range(5)]

print(f'P:{P} qsort n:{len(P)}') #,end=' ')
quickSort(P,0,len(P)-1,debug=False)
print(f'result:{P}')