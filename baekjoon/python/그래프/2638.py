#2638 
#  4변 중에서 적어도 2변 이상이 실내온도의 공기와 접촉한 것은 정확히 한시간만에 녹아 없어져 버린다
# 공기에서 공기를 탐색하고, 공기에서 치즈를 만나면 몇면에 붙어있는지 확인(치즈에서 치즈로 탐색하는 방식을 생각하면 이문제는 실패)
# 진짜 중요한점은 모눈 종이 가장자리에는 치즈를 두지 않는다!!!!!! 

#2636번 치즈 문제와 유사
import sys
input=sys.stdin.readline
from collections import deque

def air_bfs(i,j):
    q=deque()
    q.append([i,j])
    visited[i][j]=1

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and real_graph[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                elif real_graph[nx][ny]==1:
                    visited[nx][ny]=visited[nx][ny]+1

n, m=map(int, input().split())
real_graph=[]
for i in range(n):
    real_graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
time=0

while 1:
    visited=[[0 for _ in range(m)] for _ in range(n)]

    air_bfs(0,0)
    #탐색 한바퀴 끝나면 시간+1
    time+=1

    for i in range(n):
        for j in range(m):
            if visited[i][j]>=2:
                real_graph[i][j]=0

    # 공기 카운트
    block_cnt=0
    for i in range(n):
        for j in range(m):
            if real_graph[i][j]==0:
                block_cnt+=1
    #탐색 한번 하고 난 그래프의 공기수가 배열의 크기랑 같으면 break
    if block_cnt==(n*m):
        break
    

print(time)