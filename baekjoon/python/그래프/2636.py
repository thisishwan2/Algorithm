#2636

#0에서 0으로 갈때만 큐에 넣고, 0에서 1로 갈때는 치츠가 녹는다.!! 이게 제일 중요한 구현 방법.!
import sys
input=sys.stdin.readline
from collections import deque

h, w=map(int, input().split())
graph=[]
for _ in range(h):
    graph.append(list(map(int, input().split())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

cheese=[]

def bfs():
    visit=[[0 for _ in range(w)] for _ in range(h)]
    q=deque()
    q.append([0,0])
    visit[0][0]=1
    cnt=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny]==0 and visit[nx][ny]==0:
                    q.append([nx,ny])
                    visit[nx][ny]=1
                if graph[nx][ny]==1 and visit[nx][ny]==0:
                    visit[nx][ny]=1
                    graph[nx][ny]=0
                    cnt+=1
    
    cheese.append(cnt)
    return cnt

time=0

while True:
    
    cnt=bfs()
    if cnt==0:
        break
    time+=1
print(time)
print(cheese[-2]) 