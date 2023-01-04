#1707
#BFS

import sys
input=sys.stdin.readline
from collections import deque

k=int(input())

def bfs(v, group):
    q=deque()
    q.append(v)
    visit[v]=group

    while q:
        x=q.popleft()

        for i in graph[x]:
            if visit[i]==0:
                q.append(i)
                visit[i]=visit[x]*-1
            elif visit[x]==visit[i]:
                return False
    return True



for _ in range(k):
    a,b=map(int, input().split())
    graph=[[]for _ in range(a+1)]
    visit=[0 for _ in range(a+1)]

    for _ in range(b):
        u,v=map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, a+1):
        if visit[i]==0:
            res=bfs(i,1)
            if res==False:
                break
    
    if res==False:
        print("NO")
    else:
        print("YES")

"-----------------------"

#DFS
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

k=int(input())

def dfs(v, group):
    visit[v]=group

    for i in graph[v]:
        if visit[i]==0:
            a=dfs(i, -group)
            if a==False:
                return False
        elif visit[i]==visit[v]:
            return False
    return True

for _ in range(k):
    a,b=map(int, input().split())
    graph=[[]for _ in range(a+1)]
    visit=[0 for _ in range(a+1)]

    for _ in range(b):
        u,v=map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1,a+1):
        if visit[i]==0:
            res=dfs(i,1)
            if res==False:
                break
    
    print("YES" if res else "NO")