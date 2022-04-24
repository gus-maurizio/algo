class Solution:
    def maxDisjoint(self, A_, debug = True):
        A_.sort(key = lambda x:x[1])
        if debug:
            print(A_)
        maxD = [A_[0]]
        maxDlen = 1
        prev_R = A_[0][1]
        for i in range(1,len(A_)):
            # we compare with previous for overlap
            curr_L = A_[i][0]
            if curr_L > prev_R:
                # add new covering
                maxD.append(A_[i])
                prev_R = A_[i][1]
                if debug:
                    print(A_[i])
        if debug:
            print(maxD)
        return len(maxD)

    def maxCovering(self, A_, debug = True):
        # returns the minimal set that provides max coverage by collapsing overlapping intervals
        A_.sort(key = lambda x:x[0])
        if debug:
            print(A_)
        maxD = []
        prev_L = A_[0][0]
        prev_R = A_[0][1]
        for i in range(1,len(A_)):
            # we compare with previous for overlap
            curr_L = A_[i][0]
            curr_R = A_[i][1]
            if curr_L <= prev_R:
                # they overlap, so extend
                prev_R = curr_R
            else:
                # they do not overlap, add to list and reset previous
                maxD.append([prev_L, prev_R])
                prev_L = curr_L
                prev_R = curr_R    
                if debug:
                    print(maxD)
        maxD.append([prev_L, prev_R])
        if debug:
            print(maxD)
        return maxD

    def unCovered(self, A_, debug = True):
        # returns the uncovered intervals by A_
        _covered = self.maxCovering(A_, False)
        if debug:
            print(_covered)
        _unCovered = []
        prev_R = _covered[0][1]
        for i in range(1,len(_covered)):
            # we compare with previous for overlap
            curr_L = _covered[i][0]
            curr_R = _covered[i][1]
            _unCovered.append([prev_R,curr_L])
            prev_R = curr_R    
            if debug:
                print(_unCovered)
        return _unCovered

    # Maximum number of overlapping Intervals
    def maxOverlap(self, A_, debug = True):
        A_.sort(key = lambda x:x[0])
        print(A_) if debug else None
        _maxOverlap = 0
        # intervals are interpreted as arrival and departure times for intervals, like people to a party
        # arrivals take priority from departures, as in [1,2] [2,3] will be interpreted as 2 people in 2 and 1 in (2,3]
        # split arrival and departures!
        _arrive = sorted([x[0] for x in A_])
        _depart = sorted([x[1] for x in A_])
        _overlap = 0            # will hold how many segments are now there
        print(_arrive, _depart) if debug else None
        iArrive = 0
        iDepart = 0
        while iArrive < len(A_):
            if _arrive[iArrive] <= _depart[iDepart]:
                _overlap +=1
                _maxOverlap = _overlap if _overlap > _maxOverlap else _maxOverlap
                iArrive += 1
            else:
                _overlap -=1
                iDepart += 1
            print(f'{iArrive}, {iDepart}, MAX: {_maxOverlap}, INROOM: {_overlap}') if debug else None

        return _maxOverlap

A = [[1, 4], [2, 3], [4, 6], [8, 9], [2,6], [20,30] ]
# print(Solution().maxDisjoint(A, False))
# print(Solution().maxCovering(A, True))
# print(Solution().unCovered(A, True))
# print(Solution().maxOverlap(A, True))

class Histogram:
    def largestArea(self, H_, debug = True):
        print(H_) if debug else None
        N = len(H_)
        maxArea = 0
        lMin  = [-1] * N
        rMin  = [N-1] * N 
        print(lMin,rMin) if debug else None
        # find the left and right lower element for each bar in the histogram
        # assume left of element 0 has height 0 [-1] and right of element N-1 the same
        for element in range(N):
            # scan for lower value going <-
            for i in range(element,0,-1):
                if H_[i] < H_[element]:
                    lMin[element] = i
                    break
            # scan for lower value going ->
            for i in range(element,N-1):
                if H_[i] < H_[element]:
                    rMin[element] = i -1
                    break
        # now evaluate the areas for each point and choose the largest
        for element in range(N):
            area = H_[element]  * (rMin[element] - lMin[element])
            if area > maxArea:
                maxArea = area
        print([{i:(lMin[i], rMin[i], H_[i]  * (rMin[i] - lMin[i]))} for i in range(N)]) if debug else None
        return maxArea

    def largestArea2(self, H_, debug = True):
        print(H_) if debug else None
        N = len(H_)
        maxArea = 0
        lMin    = [-1] * N
        rMin    = [N] * N 
        s       = [-1]
        print(lMin,rMin) if debug else None
        i       = 0        
        while i < N:
            print(f'{i} {N} {lMin} {rMin} {s}') if debug else None
            while s and (s[-1] != -1) and (H_[s[-1]] > H_[i]):
                rMin[s[-1]] = i
                s.pop()
            if((i > 0) and (H_[i] == H_[i-1])):
                lMin[i] = lMin[i-1]
            else:
                print(f'I>0 {i} {H_[i]} {H_[i-1]}') if debug else None
                lMin[i] = s[-1]
            s.append(i)
            i += 1
        # now evaluate the areas for each point and choose the largest
        for element in range(N):
            area = H_[element]  * (rMin[element] - lMin[element]-1)
            if area > maxArea:
                maxArea = area
        print([{i:(lMin[i], rMin[i], H_[i]  * (rMin[i] - lMin[i]))} for i in range(N)]) if debug else None
        return maxArea


# Histogram - Find largest area
# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. 
# For simplicity, assume that all bars have same width and the width is 1 unit. 

H = [6, 2, 5, 4, 5, 1, 6]
# H = [1, 2, 3, 4, 5, 6]
# H = [6,6,0,6,6,6]

#   |     |
#   | | | |
#   | ||| |
#   | ||| |
#   ||||| |
#  .|||||||.
#   0123456
# 0:(-1,0) 1:(-1,4) 2:(1,2) 3:(1,4) 4:(3,4) 5:(-1,6) 6:(5,6)
print(Histogram().largestArea(H))
print(Histogram().largestArea2(H))

