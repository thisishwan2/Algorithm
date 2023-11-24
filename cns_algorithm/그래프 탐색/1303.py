import sys
input=sys.stdin.readline
from collections import deque
import math
dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int, input().split())
graph=[]
w=0
b=0
for _ in range(m):
    graph.append(list(map(str, input().rstrip())))

def bfs(x,y,color):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    count=1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]==color:
                q.append([nx,ny])
                visited[nx][ny]=1
                count+=1
    return count


visited= [[0 for _ in range(n)]for _ in range(m)]

for i in range(m):
    for j in range(n):
        if visited[i][j]==0:
            if graph[i][j]=="W":
                w+=math.pow(bfs(i,j,"W"),2)
            else:
                b+=math.pow(bfs(i,j,"B"),2)

print(str(int(w))+" "+str(int(b)))