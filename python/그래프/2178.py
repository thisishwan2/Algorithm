#2178
#해야할것이. 그래프를 어떻게 정렬해놓을건지, 그리고 양쪽다 1일 경우 어떻게 처리할지.

import sys
from collections import deque
n,m=map(int, sys.stdin.readline().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

#원래는 좌표상으로는 x가 좌우 y가 상하이다. 그러나 이중 리스트를 잘 생각해보면, [][] 앞이 행을 뒤가 열의 위치를 결정한다. 
dx=[-1,1,0,0] #상 하
dy=[0,0,-1,1] #좌 우

def bfs(x, y):
    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        # 0=상 1=하 2=좌 3=우
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #정해진 범위 안에 있는 조건 그리고 그래프의 위치의 값이 1 이어야하는 조건(이 조건은 결국 이미 한번 지나온길로는 돌아가지 않도록 함. 왜냐면 지나온 칸 만큼 누적시키므로 이미 한번 지나간 칸은 1이 아니다.)
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                q.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    
    return graph[n-1][m-1]
print(bfs(0,0))