#2146
import sys
input= sys.stdin.readline
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,cnt):
    q=deque()
    q.append([x,y])
    visit[x][y]=1
    graph[x][y]=cnt

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and visit[nx][ny]==0:
                q.append([nx,ny])
                visit[nx][ny]=1
                graph[nx][ny]=cnt

def bfs2(v):
    global ans
    dist=[[-1 for _ in range(n)]for _ in range(n)]
    q=deque()

    for i in range(n):
        for j in range(n):
            if graph[i][j]==v:
                q.append([i,j])
                dist[i][j]=0
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]!=0 and graph[nx][ny]!=v:
                    ans = min(ans, dist[x][y])
                    return
                    
                if graph[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append([nx,ny])

n=int(input())
graph=[]
ans=sys.maxsize

for _ in range(n):
    a=list(map(int, input().split()))
    graph.append(a)

visit=[[0 for _ in range(n)] for _ in range(n)]

cnt=2
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and visit[i][j]==0:
            bfs(i,j, cnt)
            cnt+=1

for i in range(2,cnt):
    bfs2(i)

print(ans)