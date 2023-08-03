#2151
# 매우 까다로웠던 문제! 다시 풀어보기 모든 경우에 대해 고민해봐야했음.

# *은 못지나감. 그리고 첨 시작위치에서 각 방향으로 뻗어나감. 뻗어나가다가 거울을 만나면 기로에 놓임. 거울 만났을때, 거울을 설치하냐 안하냐가 중요한데,
# 설치하면 방향이 좌우로 바뀌고, 안하면 그대로 지나감.

import sys
input=sys.stdin.readline
from collections import deque

#상하좌우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#변환 방향
change=[(2,3),(2,3),(0,1),(0,1)]

def bfs(x,y,dir,mirror):
    visited=[[[1e9 for _ in range(4)] for _ in range(n)]for _ in range(n)] #방향 고려해서 방문처리
    res=1e9
    for i in q:
        x,y,dir,mirror=i[0],i[1],i[2],i[3]
        visited[x][y][dir]=0


    while q:
        x,y,dir,mirror = q.popleft()

        nx=x+dx[dir]
        ny=y+dy[dir]

        if 0<=nx<n and 0<=ny<n: #범위내
            if graph[nx][ny]=="*": #벽이 아니고
                continue

            # 다음칸이 종점일때
            if (nx,ny)==(end_x, end_y):
                res=min(res, mirror)

            # 다음칸이 빈칸일때
            if graph[nx][ny]==".":
                if visited[nx][ny][dir]==1e9:
                    visited[nx][ny][dir]=visited[x][y][dir]
                    q.append([nx,ny,dir,visited[nx][ny][dir]])  
                else:
                    if visited[nx][ny][dir]> visited[x][y][dir]:
                        visited[nx][ny][dir]=visited[x][y][dir]
                        q.append([nx,ny,dir,visited[nx][ny][dir]])  

            #다음칸이 거울일때 -> 설치하냐, 안하냐 두가지로 나뉨
            if graph[nx][ny]=="!":
                
                #첫방문
                if visited[nx][ny][dir]==1e9:
                    #방향전환과 그대로 직진 둘다
                    #직진
                    visited[nx][ny][dir]=visited[x][y][dir]
                    q.append([nx,ny,dir,mirror])

                    #방향전환
                    for i in change[dir]:
                        visited[nx][ny][i]=visited[x][y][dir]+1
                        q.append([nx,ny,i,visited[x][y][dir]+1])

                #재방문
                else:
                    if visited[nx][ny][dir]>visited[x][y][dir]:
                        visited[nx][ny][dir]=visited[x][y][dir]
                        q.append([nx,ny,dir,visited[nx][ny][dir]]) 
                
                    for i in change[dir]:
                        if visited[nx][ny][i]>visited[x][y][dir]+1:
                            q.append([nx,ny,i,visited[nx][ny][i]])
                            visited[nx][ny][i]=visited[x][y][dir]+1

    return res

n=int(input())

graph=[]
for _ in range(n):
    graph.append(list(map(str, input().rstrip())))


position=[]
for i in range(n):
    for j in range(n):
        if  graph[i][j]=="#":
            position.append([i,j])

start_x, start_y = position[0]
end_x, end_y = position[1]

q=deque()
dirs=[]

# 시작 위치에서 갈 수 있는 방향을 미리 큐에 넣음
for i in range(4):
    nx=start_x+dx[i]
    ny=start_y+dy[i]

    if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny]!="*":
            q.append([start_x,start_y,i,0]) #시작점, 방향, 거울 수
            dirs.append([start_x,start_y,i,0])


print(bfs(dirs[0][0], dirs[0][1], dirs[0][2], dirs[0][3]))