#이 문제의 중점은 '시간'이다. 따라서 어느 지점을 처음 방문하면 그게 최단 시간인것. 따라서 재방문을 처리 할 필요가 없음.

import sys
from collections import deque
input=sys.stdin.readline

n,m,k=map(int,input().split()) # k는 벽을 부실 수 있는 횟수(단, 낮에만 부실수 있다.)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

visited=[[[-1 for _ in range(k+1)] for _ in range(m)]for _ in range(n)]


def bfs(x,y,broke):
    q=deque()
    q.append([x,y,broke]) 
    visited[x][y][broke]=1
    sun=1 #sun이 -1이면 낮, 1이면 밤
    count=1 #시간

    while q:
        count+=1 #시간은 매 단계마다 증가
        sun=sun*-1 #처음 bfs시 낮으로 변경하고, 이후로 밤->낮->밤 ...
        for _ in range(len(q)):
            x,y,broke=q.popleft()

            if (x,y)==(n-1,m-1):
                return visited[x][y][broke]
            
            for i in range(4):
                nx=dx[i]+x
                ny=dy[i]+y

                if 0<=nx<n and 0<=ny<m:
                    #다음이 벽이 아니면
                    if graph[nx][ny]==0:
                        # 첫 방문시
                        if visited[nx][ny][broke]==-1:
                            q.append([nx,ny,broke])
                            visited[nx][ny][broke]=count
                    # 다음이 벽이고, k번 미만으로 벽을 부신경우
                    elif broke<k:
                        # 낮이고, 방문 처음 하는 경우
                        if sun==-1 and visited[nx][ny][broke+1]==-1:
                            q.append([nx,ny,broke+1])
                            visited[nx][ny][broke+1]=count
                        # 밤이고, 방문 처음 하는 경우
                        elif sun!=-1 and visited[nx][ny][broke+1]==-1:
                            q.append([x,y,broke])
                            visited[x][y][broke]=count
    return -1

print(bfs(0,0,0))