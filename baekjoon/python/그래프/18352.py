#18352

import sys
from collections import deque
#n: 도시의 개수, m: 도로의 개수, k: 거리정보, x: 출발 도시번호
n,m,k,x=map(int, sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited=[0]*(n+1)
res=[0]*(n+1)

def bfs(x):
    visited[x]=1
    q=deque()
    q.append(x)
    distance=0
    while q:
        x=q.popleft()
        for i in graph[x]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                res[i]=res[x]+1
    for i in range(len(res)):
        if res[i]==k:
            print(i)
    if k not in res:
        print(-1)

bfs(x)

#다익스트라
import heapq
import sys

#무한대 설정
inf=int(1e9)

#n: 도시의 개수, m: 도로의 개수, k: 거리정보, x: 출발 도시번호
n,m,k,x=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(n+1)]
distance = [inf]*(n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    #연결된 노드, +1할 거리
    graph[a].append(b,1)

def dijkstra(x):
    q=[]
    heapq.heappush(q,(0,x))
    distance[x]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for j in graph[now]:
            cost=dist+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost
                heapq.heappush(q,(cost,j[0]))

dijkstra(x)

answer = []
for i in range(1, n+1):
    if distance[i] == k: answer.append(i)

if len(answer) == 0: print(-1)
else:
    for i in answer: print(i, end='\n')