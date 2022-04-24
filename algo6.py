class Solution:
    def editDistance(self, S_, T_, debug = True):
        iterations = 0
        memoize = {}
        def _eDP(S_,T_,indexS,indexT, debug = True):
            nonlocal iterations, memoize
            iterations += 1
            if (indexS,indexT) in memoize:
                return (memoize[(indexS,indexT)])
            print(f'eDP {iterations} {indexS}:{indexT}') if debug else None
            if indexS >= len(S_):
                # exhausted S_
                return len(T_) - indexT
            if indexT >= len(T_):
                # exhausted T_
                return len(S_) - indexS
            
            if S_[indexS] == T_[indexT]:
                print(f'eDP {iterations} same at {indexS} {indexT}') if debug else None
                return _eDP(S_,T_,indexS+1,indexT+1)
            else:
                return 1 + min(     _eDP(S_,T_,indexS+1,indexT),    # delete
                                    _eDP(S_,T_,indexS+1,indexT+1),  # replace
                                    _eDP(S_,T_,indexS,indexT+1),    # insert
                                )
                # to avoid multiple calls recursive we can anticipate a bit better?

            return 0

        print(f'START {S_} {T_}') if debug else None
        distance = _eDP(S_,T_,0,0, debug)
        return distance

    def editDistanceDP(self, S_, T_, debug = True):
        m = len(S_)
        n = len(T_)
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        # Fill dp[][] in bottom up manner
        for i in range(m + 1):
            for j in range(n + 1):
                print(f'DP {i}{j}') if debug else None
                # If first string is empty, only option is to
                # insert all characters of second string
                if i == 0:
                    dp[i][j] = j    # Min. operations = j
                # If second string is empty, only option is to
                # remove all characters of second string
                elif j == 0:
                    dp[i][j] = i    # Min. operations = i
                # If last characters are same, ignore last char
                # and recur for remaining string
                elif S_[i-1] == T_[j-1]:
                    print(f'DP {i}{j} S_ T_ equal') if debug else None
                    dp[i][j] = dp[i-1][j-1]
                # If last character are different, consider all
                # possibilities and find minimum
                else:
                    print(f'DP {i}{j} S_ T_ different') if debug else None
                    dp[i][j] = 1 + min( dp[i][j-1],        # Insert
                                        dp[i-1][j],        # Remove
                                        dp[i-1][j-1])    # Replace
        return dp[m][n]

class Solution2:
    def sortByD(self, Points, K, debug = True):
        return sorted(Points, key = lambda x: x[0]**2 + x[1]**2)[0:K]

    def sortByCenterMass(self, Points, K, debug = True):
        # find the center of mass
        aMassX = 0
        aMassY = 0
        for x in Points:
            aMassX += x[0]
            aMassY += x[1]
        cMassX = aMassX/len(Points)
        cMassY = aMassY/len(Points)
        print(f'{cMassX} {cMassY}') if debug else None
        distanceCM = {}
        for x in Points:
            distanceCM[tuple(x)] = (x[0] - cMassX)**2 + (x[1] - cMassY)**2
        answer = sorted(distanceCM.items(), key = lambda x:x[1])
        print(answer) if debug else None
        return answer[0:K]

    def wordBreak(word, tokens=[], debug=True):
        print(f'{word} {tokens}') if debug else None
        if word == '':
            return True
        else:
            lword = len(word)
            return any([(word[:i] in tokens) and Solution2.wordBreak(word[i:], tokens) for i in range(1, lword+1)])

    def wordBreak2(word, tokens=[], debug=True):
        print(f'{word} {tokens}') if debug else None
        cleanTokens = []
        for t in tokens:
            if t in word:
                cleanTokens.append(t)
        print(cleanTokens) if debug else None

        def _WB(word,tokens=[], debug=True):
            print(f'{word} {tokens}') if debug else None
            if word == '':
                return True
            else:
                lword = len(word)
                return any([(word[:i] in tokens) and _WB(word[i:], tokens) for i in range(1, lword+1)])

        return _WB(word, cleanTokens, debug)


S = 'geek'
T = 'geek'
# print(Solution().editDistanceDP(S,T,debug=True))

Points = [[10,0], [1,1], [2,2], [3,3], [4,4]]
# print(Solution2().sortByCenterMass(Points,3,debug=True))

# word    = 'ilikesamsung'
# tokens  = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
word    = 'aabb'
tokens  = ['aa','bb', 'aabb','aass', 'c']

print(Solution2.wordBreak2(word,tokens))