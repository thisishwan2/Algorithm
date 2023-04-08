#1012
#2178번 문제와 유사함. 잘 생각해보면 풀 수 있다.

import sys
from collections import deque

t=int(sys.stdin.readline())

for _ in range(t):
    m,n,k= map(int, sys.stdin.readline().split())
    graph=[[0 for j in range(n)] for i in range(m)]
    for i in range(k):
        x,y= map(int, sys.stdin.readline().split())
        graph[x][y]=1

    visited=[[0 for _ in range(n)] for _ in range(m)]

    bachujilung=0


    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    def bfs(x,y):
        q=deque()
        q.append((x,y))

        while q:
            x,y=q.popleft()
        
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<m and 0<=ny<n and graph[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))

    for i in range(m):
        for j in range(n):
            if graph[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                bfs(i,j)
                bachujilung+=1
    print(bachujilung)