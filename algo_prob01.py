from collections import namedtuple
import random,datetime

doc_are_they_equal='''
Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
SOLUTION
for two containers to be equal:
    - containers need to be the same size
    - containers need to have the same content, in this case letters or numbers
    - containers need to have the same element in the same relative position (sequence)
the condition of being able to reverse subarrays any number of times is equivalent to generating any permutation of B, which impacts 3rd condition.
so the position does not matter, but should be replaced by the content (letters or chars) need to appear the same exact amount of times.
this signals using hash or array to count number of appearances. Since alphabets or numbers can be very big, a hash seems best. 
keeping track of the difference (+1 if in A and -1 if in B) will help evaluate.
'''

def are_they_equal(array_a, array_b):
    def addFreq(d, key, value):
        d[key] = (d[key] if key in d else 0) + value
        return

    if len(array_a) != len(array_b):
        return False
    n = len(array_a)
    contentFreq = {}
    for i in range(n):
        addFreq(contentFreq,array_a[i],+1)
        addFreq(contentFreq,array_b[i],-1)
    return all([f == 0 for f in contentFreq.values()])

# print(are_they_equal([1,2,3,4],[1,2,4,3]))
# print(are_they_equal([1,2,3,4],[1,2,3,4]))
# print(are_they_equal([1,2,3,4],[1,2,3,8]))
# print(are_they_equal([1,2,3,4],[1,4,3,2]))

doc_passing_yearbooks='''
Passing Yearbooks
There are n students, numbered from 1 to n, each with their own yearbook. They would like to pass their yearbooks around and get them signed by other students.
You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n (in other words, it includes the integers from 1 to n exactly once each, in some order). The meaning of this list is described below.
Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i-1]. It's possible that arr[i-1] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.
It's guaranteed that, for any possible valid input, each student will eventually receive their own yearbook back and will never end up holding more than one yearbook at a time.
You must compute a list of n integers output, whose element at i-1 is equal to the number of signatures that will be present in student i's yearbook once they receive it back.
Signature
int[] findSignatureCounts(int[] arr)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, n], and all values in arr[i] are distinct.
Output
Return a list of n integers output, as described above.
Example 1
n = 2
arr = [2, 1]
output = [2, 2]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is Student 2.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is Student 1.
Pass 2:
Student 1 signs Student 2's yearbook. Then they pass it to the student at arr[0], which is Student 2.
Student 2 signs Student 1's yearbook. Then they pass it to the student at arr[1], which is Student 1.
Pass 3:
Both students now hold their own yearbook, so the process is complete.
Each student received 2 signatures.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
Pass 1:
Student 1 signs their own yearbook. Then they pass the book to the student at arr[0], which is themself, Student 1.
Student 2 signs their own yearbook. Then they pass the book to the student at arr[1], which is themself, Student 2.
Pass 2:
Both students now hold their own yearbook, so the process is complete.
Each student received 1 signature.
'''

def findSignatureCounts(arr):
    '''
    [2, 4, 3, 1] We can see that person 3 (i=3, assuming array starts at 1) passes to self, therefore just 1 signature.
    [3, 3, 1, 3] Person 1 (signs) and passes to 2 (signs) then 2 passes to 4 (signs) and 4 passes to 1 and stops (since 1 is done), hence 3 signatures
                 so basically the number of signatures is 1 (original) + length(cycle till stops)
                 1->2->4->[1]
                 2->4->1->[2]
                 3->[3]
                 4->1->2->[4]
    Data Structure to Solve it
    Naive Approach:
    '''
    signatures = [0] * len(arr)
    n = len(arr)
    for person in range(1,n+1):
        visit = [person]
        next  = arr[person-1]   # for 0-based index
        while next not in visit:
            visit.append(next)
            next  = arr[next-1]
        signatures[person - 1] = len(visit)
    return signatures

def findSignatureCountsOptimized(arr):
    '''
    [2, 4, 3, 1] We can see that person 3 (i=3, assuming array starts at 1) passes to self, therefore just 1 signature.
    [3, 3, 1, 3] Person 1 (signs) and passes to 2 (signs) then 2 passes to 4 (signs) and 4 passes to 1 and stops (since 1 is done), hence 3 signatures
                 so basically the number of signatures is 1 (original) + length(cycle till stops)
                 1->2->4->[1]
                 2->4->1->[2]
                 3->[3]
                 4->1->2->[4]
    Data Structure to Solve it
    Better approach: use a visited set and a cycle set. avoid visiting students twice and every member of a set has as many signatures as members of the set
    '''
    signatures = [0] * len(arr)
    n = len(arr)
    visited = set()
    for person in range(1,n+1):
        if person not in visited:
            visited.add(person)
        else:
            continue
        # we have a person we did not visit before, find the cycle
        cycle = {person}    # self sign at first minute
        next  = arr[person-1]   # for 0-based index
        while next not in cycle:
            cycle.add(next)     # add to this cycle
            visited.add(next)   # so we never visit this person again!
            next  = arr[next-1]
        for p in cycle:
            signatures[p - 1] = len(cycle)
    return signatures


# a = [[1,2], [2,1], [1,3,2,4], [2,4,3,1], [2,3,4,1], [2,3,4,1,6,7,8,5]]
# for p in a:
#     print('>>>',p)
#     # print(findSignatureCounts2(p))
#     print(findSignatureCounts(p))
#     print(findSignatureCountsOptimized(p))

doc_count_subarrays='''
Contiguous Subarrays
You are given an array arr of N integers. For each index i, you are required to determine the number of contiguous subarrays that fulfill the following conditions:
The value at index i must be the maximum element in the contiguous subarrays, and
These contiguous subarrays must either start from or end on index i.
Signature
int[] countSubarrays(int[] arr)
Input
Array arr is a non-empty list of unique integers that range between 1 to 1,000,000,000
Size N is between 1 and 1,000,000
Output
An array where each index i contains an integer denoting the maximum number of contiguous subarrays of arr[i]
Example:
arr = [3, 4, 1, 6, 2]
output = [1, 3, 1, 5, 1]
Explanation:
For index 0 - [3] is the only contiguous subarray that starts (or ends) with 3, and the maximum value in this subarray is 3.
For index 1 - [4], [3, 4], [4, 1]
For index 2 - [1]
For index 3 - [6], [6, 2], [1, 6], [4, 1, 6], [3, 4, 1, 6]
For index 4 - [2]
So, the answer for the above input is [1, 3, 1, 5, 1]
'''

def count_subarrays(arr):
    '''
    given an array [3, 4, 1, 6, 2], element 1 has potentially 5 subarrays, [3],   [3,4], [3,4,1], [3,4,1,6], [3,4,1,6,2]
                                    element 2 has potentially x subarrays  [3,4], [4],   [4,1],   [4,1,6],   [,4,1,6, 2]
    so every element has n (length of array) subarrays.
    Naive Implementation: for each element scan back and forth while elements are <= or >= and add 1.
    '''
    n = len(arr)
    counts = [0] * n
    for i in range(n):
        c = 1   # initialize the count 
        current = arr[i]
        # count to left
        for j in range(i-1,-1,-1):
            # print(f'<<< i={i} j={j}  arr[j]={arr[j]} <= arr[i]={current}?')
            if arr[j] <= current:
                c += 1
            else:
                break
        current = arr[i]
        # count to right
        for j in range(i+1,n):
            # print(f'>>> i={i} j={j}  arr[i]={current} >= arr[j]={arr[j]}?')
            if current >= arr[j]:
                c += 1
            else:
                break
        counts[i] = c
    return counts

def count_subarraysOptimized(arr):
    '''
    given an array [3, 4, 1, 6, 2], element 1 has potentially 5 subarrays, [3],   [3,4], [3,4,1], [3,4,1,6], [3,4,1,6,2]
                                    element 2 has potentially x subarrays  [3,4], [4],   [4,1],   [4,1,6],   [,4,1,6, 2]
    so every element has n (length of array) subarrays.
        arr    = [3, 4, 1, 6, 2]
        output = [1, 3, 1, 5, 1]
        arr    = [1,2,3,2,1]
        output = [1,2,5,2,1]
    
    Better Implementation: recursive find max and split

    '''
    n = len(arr)
    counts = [0] * n

    def count_recursive(arr,n,s,e,counts):
        '''
        we find the maximum and split the array [between s and e], in between the max values
        '''
        if (e-s) == 0:
            counts[e] += 1      # base case
            return
        # find max value
        m = max(arr[s:e+1])
        # split the array and set the maximums
        v = e - s + 1   # how many elements
        i = s
        subS = s
        splits = []
        # print('mvis',m,v,i,e)
        while i <= e:
            if arr[i] == m:
                subE = i-1
                # print('max ',i,subS,subE)
                counts[i] = v   # set the value of the max
                # shall we add it to the splits?
                if subE >= subS:
                    splits.append((subS,subE))
                subS = i+1
            i += 1
        # print('endmax ',i,subS,e)
        if subS <= e:
            splits.append((subS,e))
        # print('+++',splits)
        for i in splits:
            count_recursive(arr,n,i[0],i[1],counts)
        return

    count_recursive(arr,n,0,n-1,counts)
    return counts

def count_subarraysOn(arr):
    '''
    given an array [3, 4, 1, 6, 2], element 1 has potentially 5 subarrays, [3],   [3,4], [3,4,1], [3,4,1,6], [3,4,1,6,2]
                                    element 2 has potentially x subarrays  [3,4], [4],   [4,1],   [4,1,6],   [,4,1,6, 2]
    so every element has n (length of array) subarrays.
        arr    = [3, 4, 1, 6, 2]
        output = [1, 3, 1, 5, 1]
        arr    = [1,2,3,2,1]
        output = [1,2,5,2,1]
    
    Best Implementation: find maximum points from both ends using a stack
    '''
    n       = len(arr)
    counts  = [1] * n   
    # stack will hold the position of the last maximum value
    MaxPoint = namedtuple('max',['position','value'])
    stack   = [MaxPoint(-1,-1)]      # add ficticious prior to stack
    #left
    for i in range(n):
        # if current value at position i is larger than the stack last values, pop until a larger one is found from the past
        while len(stack) > 1 and stack[-1].value <= arr[i]:
            # print(f'element {i} popping from {stack} previous max {stack[-1].value} because {arr[i]} is equal or larger',end='; ' )
            stack.pop()
        counts[i] += i - stack[-1].position - 1      # last element of stack is the current maximum, add distance to that element!
        # print(f'counts for {i}/val={arr[i]}: push to stack {i}-({stack[-1].position})-1 for result={counts[i]}')
        # always append value!
        stack.append(MaxPoint(i,arr[i]))
    # print('LEFT>>>',counts)
    # from right
    stack = [MaxPoint(n,1)]
    for i in range(n - 1, -1, -1):
        while len(stack) > 1 and stack[-1].value <= arr[i]:
            # print(f'element {i} popping from {stack} previous max {stack[-1].value} because {arr[i]} is equal or larger',end='; ' )
            stack.pop()
        counts[i] += stack[-1].position - i - 1
        # print(f'counts for {i}/val={arr[i]}: push to stack {i}-({stack[-1].position})-1 for result={counts[i]}')
        stack.append(MaxPoint(i,arr[i]))
    # print('RIGHT<<<',counts)
    return counts


# a = [ [2,3,0,1,3,2,1]] #, [1,2], [1,2,3,2,1], [3, 4, 1, 6, 2] ]
# a = [ [10,20,30,40], [40,30,20,10], [10,10,10,10], [10,20,20,10] ]

# a = [[1,2,3,3,4,5,6,7,7], [1,2,7,3,3,4,5,6,7], [1,2,7,7,3,3,4,5,6,1]]
P = [random.randint(0,100) for x in range(10000)]
myAlgo = [count_subarrays,count_subarraysOn]
for s in myAlgo:
    start = datetime.datetime.now()    #timeit.timeit()
    r = s(P)
    end = datetime.datetime.now()
    print(f'executing {s} for {len(P)} random items --- time: {(end-start).total_seconds()}, {r[:10]}')



# for p in a:
#     print('---',p)
#     b = count_subarrays(p)
#     # c = count_subarraysOptimized(p)
#     c = count_subarraysOn(p)
#     print('>>> ',b)
#     print('>>> ',c)
#     if b == c:
#         print('+++ match')
#     else:
#         print('--- match')
# a = [10,20] #,70,70,30,40]
# print(a)
# print(count_subarraysOn(a))