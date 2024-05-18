import sys
input = sys.stdin.readline

def get_parents(x, parents):
    if x == parents[x]:
        return parents[x]
    return get_parents(parents[x], parents)


def union(x,y,parents):
    x_parent = get_parents(x, parents)
    y_parent = get_parents(y, parents)

    if x_parent<y_parent:
        parents[y_parent]=x_parent
    else:
        parents[x_parent]=y_parent

def find(x,y,parents):
    x_parent = get_parents(x, parents)
    y_parent = get_parents(y, parents)

    if x_parent==y_parent:
        return False
    else:
        return True

v,e = map(int, input().split())

edges = []

for i in range(e):
    a,b,c = map(int, input().split())
    edges.append([a-1,b-1,c])

edges = sorted(edges, key=lambda x:x[2])

parents = [i for i in range(v)]

cost = 0
for i in edges:
    if find(i[0],i[1],parents):
        union(i[0],i[1],parents)
        cost+=i[2]
print(cost)