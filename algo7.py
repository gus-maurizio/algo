class Solution:
    def bc(self, S_, debug = True):
        operators = {'+': 3,'-':3 ,'*':2 ,'/': 2}
        result = 0
        work = S_.replace(' ','')
        print(work,operators,eval(S_)) if debug else None
        values  = []
        oper    = []
        i       = 0
        valIx   = 0
        while i < len(work):
            print(i,work[i]) if debug else None
            if work[i] in operators:
                # before appending see if i can purge the stack for high priority
                values.append(int(work[valIx:i]))
                while (oper and oper[-1] in ['*','/']):
                    o = oper.pop()
                    b = values.pop()
                    a = values.pop()
                    values.append(b * a if o == '*' else b // a)
                oper.append(work[i])
                valIx = i+1
            i += 1
        # push last value
        values.append(int(work[valIx:i]))
        print(values,oper) if debug else None
        while len(oper):
            o = oper.pop()
            b = values.pop()
            a = values.pop()
            values.append(b * a if o == '*' else a // b if o == '/' else b + a if o == '+' else a - b )
           
        return values.pop() if values else None
    
# S = ' 3 * 5 + 4 / 2'
# S = ' 3 * 5 * 2'
S = ' 3 * 1 * 1 + 5 + 4 - 2 * 5'
print(Solution().bc(S,debug=True))

class Solution2:
    def calculate(self, s: str) -> int:
        inner, outer, result, opt = 0, 0, 0, '+'
        for c in s + '+':
            if c == ' ': continue
            if c.isdigit():
                inner = 10 * inner + int(c)
                continue
            if opt == '+':
                result += outer
                outer = inner
            elif opt == '-':
                result += outer
                outer = -inner
            elif opt == '*':
                outer = outer * inner
            elif opt == '/':
                outer = int(outer / inner)
            inner, opt = 0, c
        return result + outer