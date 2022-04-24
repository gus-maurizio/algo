
class Solution:
    #   /a/./b/./c/./d/

    def simplifyPath(self, S_, debug = True):
        # /a/./b/.////c/./d/
        path = []
        for c in S_.split('/'):
            if c in ['.','']:
                continue
            print(c) if debug else None
            if c in ['..']:
                if path:
                    path.pop()
            else:
                path.append(c)
        return '/' + '/'.join(path)

    def factorial(self, N_, debug = True):
        if N_ <= 1:
            return 1
        result = 1
        for i in range(2,N_ + 1):
            # print(i)
            result *= i
        return result

    # Function to print permutations of string
    # This function takes three parameters:
    # 1. String
    # 2. Starting index of the string
    # 3. Ending index of the string.
    def permute(self,a, l, r):
        if l == r:
            print (''.join(a))
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                print(f'>>{i} {l},{r} {a}')
                Solution.permute(self,a, l + 1, r)

                # backtrack
                a[l], a[i] = a[i], a[l]
 
# S = '/a/./b/./c////../d/'
# print(Solution().simplifyPath(S,debug=True))
# N = 20
# print(Solution().factorial(N,debug=True))
S = 'ABC'
Solution().permute(list(S),0,len(S)-1)