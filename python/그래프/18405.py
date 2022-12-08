#18405

import sys
input = sys.stdin.readline
from collections import deque

def bfs(data):
    q=deque(data)
    #q.append(data)와 q=deque(data)는 차이가 있다.
    #우선 data는 리스트다. [(),(),()] 형태이다.
    #q=deque를 하면 deque([])가 생긴.
    #q.append(data)같은경우 위에서 deque()을 만들어 주고, 그안에 data를 리스트를 씌워서 더하는 방식이다. 그러면 ([[(),(),()]]) 형태가 된다.
    #q=deque(data)의 경우에는 deque선언괴 동시에 그 안에 data를 넣기 때문에 deque([(),(),()])형태가 된다.

    while q:
        virus, s1, x1, y1 =q.popleft()
        if s1==s: break
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=virus
                    q.append((virus, s+1, nx, ny))
            

n,k = map(int, input().split())

graph=[]
data=[]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    ##핵심##
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j], 0, i, j))

data.sort()

#s초뒤의 , (x,y)의 바이러스는? 존재하지 않으면 0 출력
s, x, y=map(int, input().split())

bfs(data)

print(graph[x-1][y-1])