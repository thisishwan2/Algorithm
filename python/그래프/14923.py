#14923
#생각나는 풀이법은 벽 하나 없어고 탐색해서 거리를 리스트에 저장해서 최소값 찾기(단점 브루트포스로 벽을 하나씩 없애야돼서 시간이 오래걸림)(범위가 100이라 이렇게 하면 안된다.)
#위의 방법은 결국 시간초과가 난다.
#그럼 어떻게 해아할까?
#벽을 부셨을때와 안부셨을때를 나눠서 진행해줘야 한다.
#즉, 3차원 리스트를 이용하여 부셨을때와 안부셨을때를 나누고, 큐에 카운트정보와 부셨는지 안부셨는지를 알려주는 정보를 이용한다.

from collections import deque
n, m=map(int, input().split())
hy, hx=map(int, input().split())
ey, ex=map(int, input().split())

hy, hx, ey, ex=hy-1, hx-1, ey-1, ex-1

graph=[list(map(int, input().split())) for _ in range(n)]

dy, dx=[-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(y, x):
    q=deque()
    q.append((y, x, 0, 1))

    #리스트를 3차원으로 만들어서 마지막 요소가 0이면 벽을 안부시고, 1이면 벽을 부신것이다.
    visited=[[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

    #0=벽부심, 1=벽안부심
    visited[y][x][1]=1
    while q:
        #magic 변수에 벽 부심 여부를 담는다. 카운트 정보도 같이 큐에 담는다.
        y, x, cnt, magic=q.popleft()
        if (y, x)==(ey, ex):
            return cnt
        for i in range(4):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                #이동한 위치가 이미 한번 온곳이면 넘어간다.
                if visited[ny][nx][magic]:
                    continue
                #이동한 위치가 벽이고, 벽을 아직 안부셨을때
                if graph[ny][nx]==1 and magic==1:
                    visited[ny][nx][0]=1
                    q.append((ny, nx, cnt+1, magic-1))
                #이동한 위치가 벽이 아닐때
                elif graph[ny][nx]==0:
                    visited[ny][nx][magic]=1
                    q.append((ny, nx, cnt+1, magic))
    #큐가 빌때까지 돌았는데도 도착못하면 -1
    return -1
print(bfs(hy, hx))

'''

시간초과 풀이

import sys
input=sys.stdin.readline
from collections import deque
import copy

n,m=map(int, input().split())
#현 위치
hx,hy=map(int, input().split())
#미로 탈출 위치
ex,ey=map(int,input().split())

#hx,hy,ex,ey다 1부터 시작이니 graph에 0으로 된 행열 하나 추가
graph=[[0]*(m+1)]

for _ in range(n):
    graph.append([0]+list(map(int, input().split())))



dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    visit=[[0 for _ in range(m+1)]for _ in range(n+1)]
    q=deque()
    q.append([x,y])
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        if x==ex and y==ey:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 1<=nx<=n and 1<=ny<=m:
                if visit[nx][ny]==0 and destropy_graph[nx][ny]==0:
                    visit[nx][ny]=1+visit[x][y]
                    q.append([nx,ny])
    res.append(visit[ex][ey]-1)

res=[]
destropy_graph=copy.deepcopy(graph)

for i in range(1,n+1):
    for j in range(1,m+1):
        if destropy_graph[i][j]==1:
            destropy_graph[i][j]=0
            bfs(hx,hy)
            destropy_graph=copy.deepcopy(graph)

print(min(res))
'''