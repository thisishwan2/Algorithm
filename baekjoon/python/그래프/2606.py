import sys
input=sys.stdin.readline
from collections import deque

def bfs(x):
    q=deque()
    q.append(x)
    visited[x]=1

    while q:
        x=q.popleft()
        for i in graph[x]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1



n=int(input())
v=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(v):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[0]*(n+1)

bfs(1)
print(visited.count(1)-1)