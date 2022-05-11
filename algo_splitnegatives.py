import sys

def splitNegatives(a):
    n = len(a)
    cp = 0
    for i in range(n):
        if a[i] < 0:
            cp += 1
    # now we know all positive numbers and 0 re CP [0,1,-1,-2,9] n=5 cp=3
    # we should move them if they are wrong
    i  = 0 
    r  = [0] * n
    lp = 0
    print(n,cp)
    while i < n:
        if a[i] >= 0:
            r[cp] = a[i]
            cp += 1
        else:
            r[lp]  = a[i]
            lp +=1 
        i += 1
    return r
            

N = sys.argv[1] if len(sys.argv) > 1 else 10

P = [12, 11, -13, -5, 6, -7, 5, -3, -6]
# P = [0,1,-1,-2,9]
print(f'P: {P}  R:{splitNegatives(P)}')