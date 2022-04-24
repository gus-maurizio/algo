
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        import itertools

        # def subsets(s,n):
        #     return [list(i) for i in itertools.combinations(s,n)]

        def subsetsN(A, N):
            def bit1count(number):
                count = 0
                x     = 1
                while (x < number + 1):
                    if (x & number):
                        count += 1
                    x = x << 1
                return count

            for i in range(2 ** len(A),0,-1):
                # print(f'{i} {N} {i:010b} {N:010b} {bit1count(i)}')
                if bit1count(i) == N:
                    yield bin(i)[2:].zfill(len(A))


        def overlap(A,mask):
            for i in range(len(A)):
                if mask[i] == '0':
                    continue
                for j in range(len(A)):
                    if mask[j] == '0':
                        continue
                    if i == j:
                        continue
                    eli = A[i]
                    elj = A[j]
                    if eli[0] > elj[0]:
                        eli,elj = elj,eli
                    if eli[1] >= elj[0]:
                        # print(i,j,eli,elj)
                        return True
            return False

        for n in range(len(A),1,-1):
            for mask in subsetsN(A,n):
                # print(f'{n} {mask}')
                if not overlap(A,mask):
                    return n
        return 1



A = [[1,4], [2,3], [4,6], [8,9] ]
A = [[1,4], [2,3], [4,6], [8,9], [8,10]]
A = [ [2,3], [3,5], [6,9] ]
A = [[1,2],[3,5],[7,9],[9,11],[13,15],[17,19],[27,29],[1,8],[11,18],[21,28],[4,24]]
print(A)
print(Solution().solve(A))
