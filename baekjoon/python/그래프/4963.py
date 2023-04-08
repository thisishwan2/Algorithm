#4963
#bfs
#visit을 설정하지 않아도 된다. 왜냐하면, 지나간 섬은  다시 돌아갈 일이 없으므로 0(바다)로 바꿔준다.
import sys
from collections import deque

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def bfs(x,y):
    graph[x][y]=0
    q=deque()
    q.append((x,y))

    while q:
        x, y= q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1 :
                q.append((nx,ny))
                graph[nx][ny]=0


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0: break
    graph=[]
    cnt=0
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)

#dfs
import sys
sys.setrecursionlimit(10000)
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def dfs(x,y):
    graph[x][y]=0

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
            dfs(nx,ny)




while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0: break
    graph=[]
    cnt=0
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)