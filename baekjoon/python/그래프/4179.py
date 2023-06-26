#4179

import sys
input=sys.stdin.readline
import heapq
from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def f_bfs(f_lst):
    for _ in f_lst:
        x,y=fire.popleft()
        f_visited[x][y]=1

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<nx<=r and 0<ny<=c: #기존 범위(0을 추가하지 않은)안에 있고
                if f_visited[nx][ny]==0: #방문 안했고
                    if graph[nx][ny]!="#": #벽이 아니고
                        graph[nx][ny]="F"
                        f_visited[nx][ny]=1
                        fire.append([nx,ny])

def bfs(x,y, f_lst):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        new_fire=deque(f_lst)
        f_bfs(new_fire)
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if graph[nx][ny]=="0":
                    return visited[x][y]
                
                if 0<=nx<r+2 and 0<=ny<c+2:
                    if graph[nx][ny]!="#" and graph[nx][ny]!="F":
                        if visited[nx][ny]==0:
                            q.append([nx,ny])
                            visited[nx][ny]=visited[x][y]+1
    return "IMPOSSIBLE"
                            
r,c = map(int, input().split())

graph=[["0"] * (c+2)]
for _ in range(r):
    a=input().rstrip()
    a="0"+a+"0"
    graph.append(list(a))
graph.append(["0"] * (c+2))

#지훈 위치 찾기
for i in range(r+2):
    for j in range(c+2):
        if graph[i][j]=="J":
            x=i
            y=j

#불(들) 위치 찾기
fire=deque()
for i in range(r+2):
    for j in range(c+2):
        if graph[i][j]=="F":
            fire.append([i,j])

f_visited=[[0 for _ in range(c+2)]for _ in range(r+2)]
visited=[[0 for _ in range(c+2)]for _ in range(r+2)]
print(bfs(x,y,fire))


            