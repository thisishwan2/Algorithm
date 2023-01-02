import sys
sys.stdin.readline
from collections import deque
import copy

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    global graph
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and graph[x][y]>0 and bangmoon[nx][ny]==0 and visited[nx][ny]==0:
                    graph[x][y]=graph[x][y]-1

                if (bangmoon[nx][ny]==0 and graph[nx][ny]!=0 and visited[nx][ny]==0):
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    

        bangmoon[x][y]=1

time=0
water=0
while water!=(n*m):
    water=0
    visited=[[0 for _ in range(m)]for _ in range(n)]
    bangmoon=[[0 for _ in range(m)]for _ in range(n)]
    area=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                water+=1
            
            if graph[i][j]!=0 and bangmoon[i][j]==0:
                area+=1
                if area>=2:
                    print(time)
                    exit()
                bfs(i,j)

    time+=1    
print(0)