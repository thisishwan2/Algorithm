#6087

# 1. 기본적인 로직은 bfs 탐색을 할때 한쪽 방향을 먼저 다 탐색한다.(for i in range(4) 일때 0:상 먼저 일렬 탐색, 1:하 먼저 일렬탐색 ..)
# 2. 기본적으로 다음 탐색 부분이 방문하지 않았을때(vistied[nx][ny]==-1)/ 방문 조건은 배열안에서 움직일때 (0<= <h, 0<= <,w), 벽이 아닐때(!="*") 두가지 이다.
# 3. 만약 이미 방문했다면, 위의 두가지 방문 조건(배열안에서, 벽 아닐때) + 다음 진행하는 칸의 >= 현재 칸+1 이라면 탐색을 진행한다.
# 3-1. 다음 진행하는 칸의 값 >= 현재 칸 +1 에서 크거나 같다가 되는 이유는 현재칸 + 1이 작은경우는 당연히 해당된다. 
# 하지만 같은 경우는 이전 탐색경로보다, 현재 탐색경로가 미래에 더 최적의 경로 일 수 있기 때문에 같은 경우도 허용한다, 

#일반적인 bfs 탐색을 하면, 재방문할때 문제가 발생한다,

import sys
from collections import deque

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=0

    while q:
        x,y=q.popleft()
        if (x,y)==(end_x,end_y):
            return visited[x][y]-1
        for i in range(4):
            d=1 #한쪽 방향을 먼저 탐색하기 위한 변수
            while True: #한쪽을 탐색하기 위한 while문
                #dx,dy에는 1혹은 -1만 들어가기 때문에 *d를 해줘서 일렬로 탐색할 수 있도록 한다.
                nx=x+dx[i]*d
                ny=y+dy[i]*d
                # 배열안에 있을 때
                if not(0<=nx<h and 0<=ny<w):
                    break
                # 벽이 아닐때
                if graph[nx][ny]=="*":
                    break
                # 이미 방문 했다면, 현재값+1 이 이미 방문한 값보다 크다면
                if visited[nx][ny]<visited[x][y]+1 and visited[nx][ny]!= -1:
                    break
                #위의 세 조건을 통과하면
                q.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1
                d+=1


input=sys.stdin.readline

w,h=map(int, input().split())
graph=[]

for _ in range(h):
    graph.append(list(map(str, input().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[-1 for _ in range(w)]for _ in range(h)]
c_lst=[]
for i in range(h):
    for j in range(w):
        if graph[i][j]=="C":
            c_lst.append([i,j])

start_x,start_y=c_lst[0][0],c_lst[0][1]
end_x,end_y=c_lst[1][0],c_lst[1][1]

print(bfs(start_x,start_y))