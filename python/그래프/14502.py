#14502

import sys
from collections import deque
import copy
input=sys.stdin.readline

#new_graph = [item[:] for item in graph]
#이중 리스트 복사할 때 이렇게 하는 게 가장 좋더라구요

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs():
    #2인 값의 위치를 미리 큐에 저장
    q=deque()
    copy_graph= copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==2:
                q.append([i,j])

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if copy_graph[nx][ny]==0:
                    copy_graph[nx][ny]=2
                    q.append([nx,ny])
    
    global result
    count=0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j]==0:
                count+=1
    result=max(result, count)

def makewall(cnt):
    if cnt==3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                makewall(cnt+1)
                graph[i][j]=0

n,m=map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

result=0
makewall(0)
print(result)

