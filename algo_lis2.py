import random,sys,math

doc_lis='''
longest increasing subsequence of a set of numbers
'''

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
			for j in range(2,N):
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
			if a[j] >= candidates[j][-1]:
				# remove all elements coming after
				for k in range(j+1,N+1):
					loop += 1
					del candidates[k]
				N = j
				# we should add and check if becomes leader
				candidates[j].append(a[i])
				if len(candidates[j]) == len(candidates[j-1]):
					if candidates[j][-1] < candidates[j-1][-1]:
						# swap them
						candidates[j-1] = candidates[j]
					# remove this element now!
					N = j - 1
					del candidates[j]
				break
	n = len(a)
	return (n,len(candidates[1]),candidates[1],loop,divmod(loop,n))
	
# P = [10,11, 4, 3, 5,6,21, 1, 50, 41, 60, 80]
# P = [10,20,2,3,4,0,40,4,50,5]
# P = [1384, 1734, 2520, 2452, 1374, 1501, 2582, 106, 1168, 2377, 1962, 995, 198, 2858, 268, 643, 1856, 1965, 2202, 2742, 2915, 2454, 1804, 416, 2637, 2227]
# print(P)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 500
P = [random.randint(100,max(3000,2*N)) for _ in range(N)]
# P = range(2*N,3*N,1)
print(getLis(P))
