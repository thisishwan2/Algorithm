#5567

# 자신의 친구와 친구의 친구를 초대
import sys
from collections import deque

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]

visited=[0]*(n+1)

for _ in range(m):
    ai,bi = map(int, sys.stdin.readline().split())
    #bi와 ai도 친구관계이다. 
    graph[ai].append(bi)
    graph[bi].append(ai)

res=[]

def bfs(start):
    q=deque()
    q.append(start)

    while q:
        a=q.popleft()
        for i in graph[a]:
            if visited[i]==0 and i!=1:
                q.append(i)
                visited[i]=visited[a]+1
                if visited[i]<=2:
                    res.append(i)
bfs(1)
print(len(res))