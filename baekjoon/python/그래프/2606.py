#2606

import sys
from collections import deque
input=sys.stdin.readline
#컴퓨터 수
computer=int(input())
m=int(input())

graph=[[] for _ in range(computer+1)]
visited=[0]*(computer+1)

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=1
    cnt=0

    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1
                cnt+=1

    return cnt
print(bfs(1))