#7569
#보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다
#하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다.
#철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.
#단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

#3차원으로 풀기.
import sys
input=sys.stdin.readline
from collections import deque

#m=가로, n=세로, h=개수(높이)
m,n,h=map(int, input().split())


box=[]

#3중 리스트 생성(x,y,z)로 3차원이기때문
for _ in range(h):
    graph=[]
    for _ in range(n):
        a=list(map(int, input().split()))
        graph.append(a)
    box.append(graph)
         

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

def bfs():
    q=deque()

    for i in range(h): #z
        for j in range(n): #y
            for k in range(m): #x
                if box[i][j][k] == 1:
                    q.append((i,j,k))
                
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            #원래 x,y 만 있을때는 nx를 상하 ny를 좌우로 했었는데, 3중리스트가 되면서 아래처럼 바뀜.
            nx=x+dx[i] #좌우
            ny=y+dy[i] #상하
            nz=z+dz[i] #위아래
            if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                if box[nz][ny][nx]==0:
                    box[nz][ny][nx]=box[z][y][x]+1
                    q.append([nz,ny,nx])


bfs()
ans=0

for i in range(h):
    for j in range(n):
        for k in range(m):

            if box[i][j][k]==0:
                print(-1)
                exit()
            ans=max(ans, box[i][j][k])

print(ans-1)
