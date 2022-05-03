import random

def count1bits(n):
    c = 0
    i = n
    while i > 0:
        # assume i = 0b0100 (4), i - 1 = 3 0b0011 -> i & (i-1) = 0! sets last non 0 bit to 0
        c += 1
        i = i & (i-1)
    return c

def getn1bits(upto, n):
    i = 0 
    while i <= upto:
        if count1bits(i) == n:
            print(f'{i:03d} {i:08b}')
        i += 1

def genSubsetsSizeN(a, N=2):
    n = len(a)
    upto = 2 ** n
    i = 0 
    ss = []
    while i < upto:
        if count1bits(i) == N:
            bits = f'{i:0{n}b}'
            ss.append([a[j] for j,v in enumerate(bits) if v == '1'])
        i += 1
    return ss



P = [10,20,30,40]
genSubsetsSizeN(P,3)