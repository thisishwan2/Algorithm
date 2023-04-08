#14442
#벽 부수고 이동하기 2(python으론 못품. pypy3로 풀자)

import sys
input=sys.stdin.readline
from collections import deque

n,m,k=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(x,y,cnt):
    q=deque()
    q.append([x,y,cnt]) # x,y,벽을 부셨는짖 아닌지 (0,1), 벽을 부신 횟수
    visit[x][y][cnt]=1

    while q:
        x,y,cnt=q.popleft()
        if x==n-1 and y==m-1:
            return visit[n-1][m-1][cnt]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
            #다음이 벽일때, 부신횟수를 넘지 않고, 다음 이동경로가 방문하지 않았을때
                if graph[nx][ny]==1 and cnt<k:
                    if visit[nx][ny][cnt+1]==0:
                        q.append([nx,ny,cnt+1])
                        visit[nx][ny][cnt+1]=visit[x][y][cnt]+1
         
            #다음이 벽이 아니고, 다음이동경로를 방문하지 않았을 때
                if graph[nx][ny]==0:
                    if visit[nx][ny][cnt]==0:
                        q.append([nx,ny,cnt])
                        visit[nx][ny][cnt]=visit[x][y][cnt]+1
    return -1

#이전의 벽부시기 1과는 다르게 k번 부실수 있으므로 벽을 부셨는지 여구(0,1)에서 벽을 몇번 부셨는지(0,1,2,....,k)의 여부로 방문처리를 해주는게 핵심.
visit=[[[0]*(k+1) for _ in range(m)]for _ in range(n)]
print(bfs(0,0,0))