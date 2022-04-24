import itertools,operator
# def findsubsets(s, n):
def findsubsets(s, n):
    return [list(i) for i in itertools.combinations(s, n)]
     
# Driver Code
s = [1, 2, 3, 4]
n = 4
 

# print(findsubsets(s, n))
def isRotation(a: str, b: str) -> bool:
    return b in a + a

# print(isRotation('GEEKS', 'ESKGE'))
# 'GEEKS', 'EKSGE'

def overlap(a,b):
    if int(a[0]) <= int(b[0]):
        low,high = a,b
    else:
        low,high = b,a
    if int(low[1]) >= int(high[0]):
        return True
    else:
        return False

A = [[1,2],[3,5],[7,9],[9,11],[13,15],[17,19],[27,29],[1,8],[11,18],[21,28],[4,24],[100,200]]

nodeinfo = {}
for element in A:
    interval    = f'{element[0]}::{element[1]}'
    references  = 1
    if interval in nodeinfo:
        # print(f'duplicate interval {interval} {element}')
        continue
    for node in nodeinfo.keys():
        if overlap(node.split('::'),element):
            # print(f'{node} {interval}')
            references += 1
            nodeinfo[node] += 1
    nodeinfo[interval] = references

sorted_nodes = dict(sorted( nodeinfo.items(),
                            key=operator.itemgetter(1),
                            reverse=True))
print(sorted_nodes)
# the largest disjoint set will have all elements in 1, and the largest number of elements.
# overlapping segments add coverage to multiple intervals, by removing them we get them close to 1
def overlapping(nodeinfo):
    for node in nodeinfo.keys():
        if nodeinfo[node] > 1:
            # print(f'OVERLAPP {node} {nodeinfo[node]}')
            return True
    return False

def nodetrim(nodeinfo):
    high    = 0
    nodes   = []
    for node in nodeinfo:
        if  nodeinfo[node] > high:
            high = nodeinfo[node]
            nodes = [node]
        elif nodeinfo[node] == high:
            nodes.append(node)
    # print(f'REMOVE {high} {nodes}')
    for node in list(nodes):
        # print(f'{node} TBR')
        if nodeinfo[node] > 1:
            del nodeinfo[node]
        for n in nodeinfo.keys():
            if overlap(node.split('::'),n.split('::')):
                # print(f'{node} {n} -1')
                if nodeinfo[n] > 1:
                    nodeinfo[n] -= 1
                if n in nodes:
                    nodes.remove(n)



while (overlapping(nodeinfo)):
    nodetrim(nodeinfo)
print(nodeinfo, len(nodeinfo))
