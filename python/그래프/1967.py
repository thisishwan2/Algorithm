#1967
#처음에 많이 헤맨 문제, 조합을 이용해서 모든 경우의 수를 다 탐색하기도 했고,
#1에서 12까지 시작노드로 잡고 젤 먼 위치를 리스트에 담아서, 그중 젤 큰 값을 찾는 방법을 썼다.
#그러나 메모리초과를 줄일 수 없었다.
#해답은 간단했다. 어느 노드에서든 가장 먼 노드를 구한뒤, 그 노드에서 가장 먼 노드를 구하면
#그 두 노드 사이의 가중치가 결국 답이다. 이러면 시간 메모리 둘다 줄일 수 있다.


import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dfs(v):
    visit[v]=1
    for next, a in graph[v]:
        if visit[next]==0:
            distance[next]=distance[v]+a
            dfs(next)


visit=[0]*(n+1)
distance=[0]*(n+1)
dfs(1)

max_idx=distance.index(max(distance))

visit=[0]*(n+1)
distance=[0]*(n+1)
dfs(max_idx)
print(max(distance))



'''
내가 풀은 오답 풀이
내 생각엔 다 맞는 풀이지만 메모리 초과를 풀지 못해서 틀린듯?

#1967
import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

n=int(input())
graph=[[]for _ in range(n+1)]
weight=[[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n-1):
    mom, kid, num = map(int, input().split())
    graph[mom].append(kid)
    graph[kid].append(mom)

    weight[mom][kid]=num
    weight[kid][mom]=num

res=[]
def bfs(a,b):
    visit=[0]*(n+1)
    num=0
    q=deque()
    q.append([a, num])
    visit[a]=1
    

    while q:
        x, num=q.popleft()
        if x==b:
            res.append(num)
            break
        for dx in graph[x]:
            q.append([dx, weight[x][dx]+num])

combis=list(combinations(range(1, n+1), 2))

for combi in combis:
    a=combi[0]
    b=combi[1]
    bfs(a, b)

print(max(res))

-----------------------------------------

#1967
import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque

n=int(input())
graph=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


combis=list(combinations(range(1,n+1),2))
res=[]
def dfs(a,b,num):
    if a==b:
        res.append(num)
        return
        
    visit[a]=1
    for i in graph[a]:
        if visit[i[0]]==0:
            dfs(i[0], b, num+i[1])

for combi in combis:
    visit=[0]*(n+1)
    dfs(combi[0],combi[1],0)

print(max(res))

------------------------------------------------

import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)
#조합을 써서 for문을 다 돌리면 메모리 초과가남.
#1에서 12까지 dfs돌려서 큰값들을 리스트에 넣고, 맥스 때리면될듯?
# 이 풀이도 마찬가지로 메모리 초과
n=int(input())
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n-1):
    a,b,c=map(int, input().split())
    graph[a][b]=c
    graph[b][a]=c

def dfs(start,num):
    visit[start]=1

    for i in range(1,n+1):
        if graph[start][i]!=0 and visit[i]==0:
            res.append(num+graph[start][i])
            dfs(i, num+graph[start][i])
    return max(res)

result=[]
for i in range(1,n+1):
    visit=[0]*(n+1)
    res=[]

    result.append(dfs(i,0))

print(max(result))


'''