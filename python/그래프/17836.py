import sys
input=sys.stdin.readline
from collections import deque

n,m,t=map(int, input().split())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))
visit=[[0]*m for _ in range(n)]
sword=10000000

def bfs(x,y):
    global sword
    q=deque()
    q.append([x,y])
    visit[x][y]=1
    
    while q:
        x,y=q.popleft()

        #검을 만나면, 검까지의 시간과 검에서 공주의 위치까지를 더한다.
        if graph[x][y]==2:
            sword=(n-1-x) + (m-1-y) + visit[x][y]-1
        
        #공주의 위치에 도달하면, 검을 만났을때의 값과, bfs로 탐색한 값중 작은 값을 골라서 리턴한다.
        if x==n-1 and y==m-1:
            return min(visit[x][y]-1, sword)
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]!=1:
                if visit[nx][ny]==0:
                    q.append([nx,ny])
                    visit[nx][ny]=visit[x][y]+1
    #공주를 못찾고 q가 다 비면 sword=1000000을 리턴한다.
    return sword

res=bfs(0,0)

print("Fail" if(res>t) else res)


'''
시간초과난 맞는 풀이 처음 이와 같은 방법으로 문제를 풀었다.

#17836

import sys
input=sys.stdin.readline
from collections import deque

n,m,t=map(int, input().split())
graph=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

#검 없이 갈때
def bfs(x,y): 

    def sword_bfs(cnt, x,y):
        ddx=[1,0]
        ddy=[0,1]
        sword_visit=[[0]*(m) for _ in range(n)]
        sword_q=deque()
        sword_q.append([x,y])
        sword_visit[x][y]=cnt

        while sword_q:
            x,y=sword_q.popleft()
            for i in range(2):
                nx=x+ddx[i]
                ny=y+ddy[i]
                if 0<=nx<n and 0<=ny<m:
                    sword_q.append([nx,ny])
                    sword_visit[nx][ny]=sword_visit[x][y]+1
        result.append(sword_visit[n-1][m-1]-1)


    visit=[[0]*(m) for _ in range(n)]
    q=deque()
    q.append([x,y])
    visit[x][y]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:

                if graph[nx][ny]==2:
                    visit[nx][ny]=visit[x][y]+1
                    sword_bfs(visit[nx][ny], nx,ny)
                    graph[nx][ny]=3
                    continue
                if visit[nx][ny]==0 and graph[nx][ny]==0:
                    q.append([nx,ny])
                    visit[nx][ny]=visit[x][y]+1
    result.append(visit[n-1][m-1]-1)

result=[]
bfs(0,0)

if min(result)==-1:
    print("Fail")
elif min(result)>t:
    print("Fail")
else:
    print(min(result))
'''