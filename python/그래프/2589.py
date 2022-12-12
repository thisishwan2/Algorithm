#2589

import sys
input=sys.stdin.readline
from collections import deque
#한 칸 이동하는데 한 시간이 걸린다.
#보물의 위치는 보물 위치간의 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 곳에 있다.

m, n =map(int, input().split())
graph=[]

for _ in range(m):
    graph.append(list(input().rstrip()))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

res=[]


def bfs(x, y):
    maxi=0
    visit=[[0 for _ in range(n)] for _ in range(m)]

    q=deque()
    q.append([x,y])
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]=="L" and visit[nx][ny]==0 :
                q.append([nx,ny])
                visit[nx][ny]=visit[x][y]+1
                maxi=max(visit[x][y]+1, maxi)
    return maxi-1

#처음에 시작점과 끝점을 어떻게 잡지 라는 고민이 있었는데,
#범위가 50 50 인것을 보고 브루트포스로 돌려서, 가장 큰 값을 찾는 것이었다.
result=0
for i in range(m):
    for j in range(n):
        if graph[i][j]=="L":
            result=max(result, bfs(i,j))


print(result)