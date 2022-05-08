import random,sys,math

doc_lis='''
longest increasing subsequence of a set of numbers
'''

def getLisN(a):
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
		if len(r) >= len(rr):
			rr = [x for x in r]
	return (len(a),len(rr), rr,f'{loop:,d} -> O(n) = {loop//len(a)+1}')

def getLis(a):
	if len(a) == 0:
		return []
	candidates = {}
	N = 1
	candidates[N] = [a[0]]
	loop = 1
	for i in range(1,len(a)):
		loop += 1
		if a[i] >= candidates[1][-1]:
			candidates[1].append(a[i])
			for j in range(2,N+1):
				del candidates[j]
			N = 1
			continue
		if a[i] < candidates[N][-1]:
			if len(candidates[N]) > 1:
				N += 1			# increment and create new element
			candidates[N] = [a[i]]
			continue
		# we have a candidate to grow, check from 2 on
		for j in range(2,N+1):
			loop += 1
			if a[i] >= candidates[j][-1]:
				# remove all elements coming after
				for k in range(j+1,N+1):
					loop += 1
					del candidates[k]
				N = j
				# we should add and check if becomes leader
				candidates[j].append(a[i])
				if len(candidates[j]) >= len(candidates[j-1]):
					if candidates[j][-1] < candidates[j-1][-1] or len(candidates[j]) > len(candidates[j-1]):
						# swap them
						candidates[j-1] = candidates[j]
					# remove this element now!
					N = j - 1
					del candidates[j]
				break
	n = len(a)
	return (n,len(candidates[1]),candidates[1],f'{loop:,d} -> O(n) = {loop//n+1} chains: {[len(v) for k,v in candidates.items()]}')
	
# P = [10,11, 4, 3, 5,6,21, 1, 50, 41, 60, 80]
# P = [10,20,2,3,4,0,40,4,50,5]
# P = [1384, 1734, 2520, 2452, 1374, 1501, 2582, 106, 1168, 2377, 1962, 995, 198, 2858, 268, 643, 1856, 1965, 2202, 2742, 2915, 2454, 1804, 416, 2637, 2227]
# print(P)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
P = [random.randint(0,max(3000,2*N)) for _ in range(N)]
# P = [171, 1043, 2255, 2885, 2337, 1480, 1701, 594, 1011, 500, 1556, 2029, 2379, 2749, 2993, 2993]
# P = range(2*N,3*N,1)
print(getLis(P)) 
# print(getLisN(P)) if N < 5001 else None
