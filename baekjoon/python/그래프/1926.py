# 1926
import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    size=1

    while q:
        x,y,=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if n>nx>=0 and m>ny>=0 and graph[nx][ny]==1:
                if visited[nx][ny]==0:
                    q.append([nx,ny])
                    size+=1
                    visited[nx][ny]=1
    return size

n,m = map(int, input().split())
graph=[]
for _ in range(n):
    a=list(map(int, input().split()))
    graph.append(a)

visited=[[0 for _ in range(m)]for _ in range(n)]
cnt=0
width=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            cnt+=1
            width=max(width, bfs(i,j))

print(cnt)
print(width)