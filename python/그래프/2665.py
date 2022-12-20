#2665

import sys
input=sys.stdin.readline
from collections import deque


n=int(input())

room=[]
for i in range(n):
    room.append(list(map(int,input().rstrip())))

visited=[[-1]*(n) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * n for _ in range(n)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return visited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if room[nx][ny] == 1:
                    q.appendleft((nx, ny)) #이부분이 핵심. 즉, 흰방부터 먼저 탐색한다.(다익스트라의 가중치와 비슷한 원리)
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx, ny))
                    visited[nx][ny]=visited[x][y]+1
    

print(bfs())

#다익스트라 풀이
import sys
input=sys.stdin.readline
import heapq


n=int(input())
room=[]
for i in range(n):
    room.append(list(map(int,input().rstrip())))

visited=[[0]*(n) for _ in range(n)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dijkstra(x,y):
    hq=[]
    heapq.heappush(hq,[0,x,y])
    visited[x][y]=1

    while hq:
        dist, x,y=heapq.heappop(hq)

        if x==n-1 and y==n-1:
            print(dist)
            return
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0:
                visited[nx][ny]=1
                if room[nx][ny]==1:
                    heapq.heappush(hq, [dist, nx, ny])
                else:
                    heapq.heappush(hq, [dist+1, nx, ny])
                    
dijkstra(0,0)

'''
내가 푼 풀이(정답)
import sys
input=sys.stdin.readline
from collections import deque


n=int(input())

room=[]
for i in range(n):
    room.append(list(map(int,input().rstrip())))

distance=[[0]*(n) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    distance[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if distance[nx][ny]==0:
                    if room[nx][ny]==1:
                        distance[nx][ny]=distance[x][y]
                    if room[nx][ny]==0:
                        distance[nx][ny]=distance[x][y]+1
                    q.append([nx,ny])

                elif distance[nx][ny]!=0:
                    if room[nx][ny]==1:
                        if distance[nx][ny]>distance[x][y]:
                            q.append([nx,ny])
                            distance[nx][ny]=distance[x][y]
                    if room[nx][ny]==0:
                        if distance[nx][ny]>distance[x][y]+1:
                            distance[nx][ny]=distance[x][y]+1
                            q.append([nx,ny])

bfs(0,0)
print(distance[n-1][n-1]-1)

'''