#1600 벽 부시고 이동하기 2와 매우 유사한 문제

#말은 장애물을 뛰어넘을 수 있다. 나이트 이동방식으로 이동
#원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 
#격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다.

import sys
input=sys.stdin.readline
from collections import deque

h_dx=[-1,-2,-2,-1,1,2,2,1]
h_dy=[-2,-1,1,2,-2,-1,1,2]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#원숭이각 말처럼(나이트 이동) 이동할 수 있는 횟수 
k=int(input())

w,h=map(int, input().split())
graph=[]
for _ in range(h):
    graph.append(list(map(int, input().split())))

def bfs():
    q=deque()
    q.append([0,0,0])
    visit[0][0][0]=1

    while q:
        x,y,cnt=q.popleft()
        if x==h-1 and y==w-1:
            return visit[x][y][cnt]-1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if visit[nx][ny][cnt]==0 and graph[nx][ny]==0:
                    q.append([nx,ny,cnt])
                    visit[nx][ny][cnt]=visit[x][y][cnt]+1
        if cnt<k:
            for i in range(8):
                nx=x+h_dx[i]
                ny=y+h_dy[i]
                if 0<=nx<h and 0<=ny<w:
                    if visit[nx][ny][cnt+1]==0 and graph[nx][ny]==0:
                        q.append([nx,ny, cnt+1])
                        visit[nx][ny][cnt+1]=visit[x][y][cnt]+1
    return -1

visit=[[[0]*(k+1) for _ in range(w)]for _ in range(h)]

print(bfs())