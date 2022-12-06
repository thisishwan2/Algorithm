#2667

import sys
from collections import deque
input=sys.stdin.readline
#dfs 일때
def dfs(x,y):
    global cnt

    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and visited[nx][ny]==0:
            cnt+=1
            dfs(nx,ny)
    
n=int(input())

graph=[]*(n)

visited=[[0 for _ in range(n)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=1
res=[]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            dfs(i,j)
            res.append(cnt)
            cnt=1

res.sort()

print(len(res))
for i in res:
    print(i)


#bfs 일때
def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1
                cnt+=1
    return cnt

n=int(input())

graph=[]*(n)

visited=[[0 for _ in range(n)] for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

res=[]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visited[i][j]==0:
            res.append(bfs(i,j))
res.sort()

print(len(res))
for i in res:
    print(i)