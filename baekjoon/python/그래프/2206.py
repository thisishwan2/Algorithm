#2206

import sys
input=sys.stdin.readline
from collections import deque

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().strip())))

#3중 리스트
visit=[[[0]*2 for _ in range(m)]for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q=deque()
    q.append([0,0,0])
    visit[0][0][0]=1


    while q:
        x,y,brk=q.popleft()

        if x==n-1 and y==m-1:
            return visit[x][y][brk]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 벽 안부시고 이동(빈공간->빈공간, 벽부신 공간-> 빈공간)
                if graph[nx][ny]==0 and visit[nx][ny][brk]==0:
                    q.append([nx,ny,brk])
                    visit[nx][ny][brk]=visit[x][y][brk]+1

                #벽 부시고 이동(빈공간 ->벽, 벽->벽 은 안됨)
                if graph[nx][ny]==1 and brk==0:
                    q.append([nx,ny,brk+1])
                    visit[nx][ny][brk+1]=visit[x][y][brk]+1
    return -1
print(bfs())



#----------------내가 푼 정답-------------------
#2206
#벽 한개만 부실 수  있다.

import sys
input=sys.stdin.readline
import heapq
from collections import deque

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().strip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y,0])
    visit[x][y]=1
    wall[x][y]=1

    while q:
        x,y, break_wall=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                #벽 안부신 경우
                if break_wall==0:
                    #다음이 벽이면,
                    if graph[nx][ny]==1 and wall[nx][ny]==0:
                        q.append([nx,ny,break_wall+1])
                        wall[nx][ny]=visit[x][y]+1
                    if graph[nx][ny]==0 and visit[nx][ny]==0:
                        q.append([nx,ny,break_wall])
                        visit[nx][ny]=visit[x][y]+1
                #벽을 부신경우
                elif break_wall==1:
                    #다음이 벽이면
                    if graph[nx][ny]==1:
                        continue
                    #벽이 아니먄
                    if graph[nx][ny]==0 and wall[nx][ny]==0:
                        wall[nx][ny]=wall[x][y]+1
                        q.append([nx,ny,break_wall])
    return break_wall

visit=[[0 for _ in range(m)] for _ in range(n)]
wall=[[0 for _ in range(m)] for _ in range(n)]
a=bfs(0,0)
if visit[n-1][m-1]==0 and wall[n-1][m-1]==0:
    print(-1)
elif wall[n-1][m-1]!=0 and visit[n-1][m-1]!=0:
    print(min(wall[n-1][m-1], visit[n-1][m-1]))
elif a==1:
    print(wall[n-1][m-1])
elif a==0:
    print(visit[n-1][m-1])