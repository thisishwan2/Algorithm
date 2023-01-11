#7562
#왜 자꾸 틀렸다고 나오지??

import sys
from collections import deque


#체스 이동 가능 경로 (왼쪽 상단부터~오른쪽 상단~왼짝 하단~오른쪽 하단)(주어진 조건의 크기의 판의 모든 곳을 방문할 수 있다.)
dx=[-1, -2, -2, -1, 1, 2, 2, 1] 
dy=[-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(x,y,future_x, future_y):
    q=deque()
    q.append((x,y))
    graph[x][x]=1
    while q:
        x,y=q.popleft()
        if x==future_x and y==future_y:
            print(graph[x][y]-1)    
            return
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny]==0:
                q.append((nx,ny))
                #이 부분이 핵심이다.
                graph[nx][ny]=graph[x][y]+1

t=int(sys.stdin.readline())
for _ in range(t):
    l=int(sys.stdin.readline())
    now_x, now_y=map(int, sys.stdin.readline().split())
    future_x, future_y=map(int, sys.stdin.readline().split())

    #체스판
    graph=[[0]*l for _ in range(l)]
    bfs(now_x,now_y, future_x, future_y)