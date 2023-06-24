# 15591
import sys
input=sys.stdin.readline
from collections import deque

def bfs(v,k):
    q=deque()
    q.append(v)
    visited[v]=1
    cnt=0

    while q:
        v=q.popleft()

        for i in graph[v]:
            if i[1]>=k and visited[i[0]]!=1:
                q.append(i[0])
                cnt+=1
                visited[i[0]]=1
    return cnt
                    
n,q=map(int, input().split())

graph=[[]for _ in range(n+1)]

for _ in range(n-1):
    pi,qi,ri=map(int, input().split())

    graph[pi].append([qi,ri])
    graph[qi].append([pi,ri])

for _ in range(q):
    k,v=map(int, input().split()) #k이상의 usd만, v와 연결된 노드에 대해서만
    visited=[0 for _ in range(n+1)]
    print(bfs(v,k))