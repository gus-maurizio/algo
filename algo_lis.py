import random,sys

doc_lis='''
longest increasing subsequence of a set of numbers
'''
memo = {}

def getLis(a):
	rl = 0
	rr = []
	loop = 0
	for i in range(len(a)):
		r = [a[i]]
		for j in range(i+1,len(a)):
			loop += 1
			if a[j] >= r[-1]:
				r.append(a[j])
		#print(i,r)
		if len(r) > len(rr):
			rr = [x for x in r]
	return (len(a),len(rr), rr,loop)


def getLisOpt(a):
	if len(a) == 0:
		return []
	candidates = {}
	candidates[1] = [a[0]]
	loop = 0
	for i in range(1,len(a)):
		for k,v in list(candidates.items()):
			#print(loop,len(a),i,k,v,minkey,candidates)
			loop += 1
			if a[i] >= v[-1]:
				v.append(a[i])
			else:
				candidates[i+1] = [a[i]]
		# clean candidates with no chance: same or less length with larger or equal last value
		# a candidate has either a longer list or a smaller last value
		clean = sorted(candidates.items(),key=lambda item: len(item[1]),reverse=True)
		for i,val in enumerate(clean):
			# i is index to clean, val is tuple of k: index to candidates and v: array so far
			if i == 0:
				continue
			loop += 1
			if len(val[1]) <= len(clean[i-1][1]) and val[1][-1] >= clean[i-1][1][-1]:
				del candidates[val[0]]
			# the next line chooses the least value for same length, if removed makes it closer to prev fun			
			if len(val[1]) == len(clean[i-1][1]) and val[1][-1] < clean[i-1][1][-1]:
				del candidates[clean[i-1][0]]				
	answer = sorted(candidates.items(),key=lambda item: len(item[1]),reverse=True)
	maxlen = len(answer[0][1])
	result = [x[1] for x in answer if len(x[1]) == maxlen]
	return (len(a),maxlen,result[0],loop)

def getLisOpt2(a):
    # consider data as stream and keep a list of potential candidates
    # we save the max value of the subset starting with the first value
    # and we keep the lists ordered by length

    def cleanup(N,cMax,cVal,loop):
        # first sort based on length of cVal
        for i in range(1,N):
            j = i
            loop += 1
            while j > i and (len(cVal[j]) > len(cVal[j-1])):
                cVal[j], cVal[j-1] = cVal[j-1],cVal[j]
                cMax[j], cMax[j-1] = cMax[j-1],cMax[j]
                j -= 1
        # now we have some interesting cases... between consecutive, same length elements
        # we need to keep the one with the lowest cMax and discard the rest
        todel = []
        for i in range(0,N):
            loop += 1
            if i < N-1 and len(cVal[i]) == len(cVal[i+1]):
                todel += [i+1] if cMax[i] <= cMax[i+1] else [i]
        for i in todel:
            del cMax[i]
            del cVal[i]
        return cMax[0],cMax[-1],len(cMax),loop

    loop = 1
    if len(a) <= 1:
        return a
    candidatesMax = []
    candidatesVal = []
    # min and max values seen so far!
    smin = smax = a[0]              # load fist element
    candidatesN = 1                 # number of elements in candidatesMax/Val
    candidatesMax.append(a[0])
    candidatesVal.append([a[0]])
    for i in range(1,len(a)):       # loop over 2nd element on
        # think a stream of values, and process elements as they come O(n)
        if   a[i] >= smax:
            # a larger value than anything seen will add to the first (largest) and 
            # knock down all less long values
            candidatesMax[0]    = a[i]
            candidatesVal[0]   += [a[i]]
            candidatesN         = 1           # all values below the first, drop!
            del candidatesMax[1:]
            del candidatesVal[1:]
            smax                = a[i]
            smin                = a[i]
        elif a[i] < smin:
            # a smaller value than anything seen opens a new possibility!
            # check if it can replace the previous smaller
            if len(candidatesVal[-1]) == 1:
                candidatesMax[-1] = a[i]
                candidatesVal[-1] = [a[i]]
                smin              = a[i]
                smax              = candidatesMax[0]  
            else:
                candidatesMax.append(a[i])
                candidatesVal.append([a[i]])
                candidatesN        += 1
                smin                = a[i]
        elif a[i] < smax and a[i] >= smin:
            # this is where it gets interesting! it does not fit in the largest, but can
            # bump any of the others to become larger and potentially more inclusive, knocking down the largest!
            for j in range(1,candidatesN):
                # is this larger or equal the largest value? find the first that matches
                if a[i] >= candidatesMax[j]:
                    candidatesMax[j]  = a[i]
                    candidatesVal[j] += [a[i]]
                    # knock down all the rest!
                    candidatesN       = j + 1
                    del candidatesMax[j+1:]
                    del candidatesVal[j+1:]
                    smin = a[i]         # new min!
                    break               # nothing else to do, all the next elements are useless now
            # we readjusted below the first and largest, so it may not be the largest anymore
            (smax, smin, candidatesN,loop) = cleanup(candidatesN,candidatesMax,candidatesVal,loop)
        # done! go get the next from stream
        loop += 1
    return (len(a),len(candidatesVal[0]),candidatesVal[0],loop)



# P = [10,11, 4, 3, 5,6,21, 1, 50, 41, 60, 80]
# P = [10,20,2,3,4,0,40,4,50,5]
# P = [1384, 1734, 2520, 2452, 1374, 1501, 2582, 106, 1168, 2377, 1962, 995, 198, 2858, 268, 643, 1856, 1965, 2202, 2742, 2915, 2454, 1804, 416, 2637, 2227]
# print(P)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
P = [random.randint(100,max(3000,N)) for _ in range(N)]
# print(getLis(P))
print(getLisOpt(P))
print(getLisOpt2(P))