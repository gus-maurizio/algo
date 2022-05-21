
def simplifyPath(S_, debug = True):
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

 
S = '/a/./b/./c////../d/'
print(simplifyPath(S,debug=True))
