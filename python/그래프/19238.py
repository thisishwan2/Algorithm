# m명의 손님을 태우는 것이 목표 -> 목표 미달성시 -1출력
# 택시가 가장 가까운 승객을 태워서, 해당 승객의 목적지로 데려다준다.
# 가장 가까운 승객이 여러명일 경우, 행번호가 작은 승객 그 다음으로 열번호가 가장 작은 승객을 태운다.
# 승객을 목적지로 이동시키면, 그 승객을 태워 이동하며 소모한 연료의 두배가 충전된다.(연료=거리)
# 이동중 연료가 바닥나면 실패. 단, 승객에 목적지에 도달해서 연료가 바닥난 경우는 실패로 간주하지 않음.
# 연료의 양을 구한다.

# 문제를 풀 때 주의해야할 점 택시가 승객에게 못가는 경우, 승객을 태운 택시가 목적지로 못가는 경우 두 경우는 실패한것이다.
# 따라서 실패의 경우는 연료가 바닥나거나, 택시->승객 을 못하거나, 승객->목적지 를 못하는 경우

import sys
input=sys.stdin.readline
from collections import deque

n,m,fuel=map(int, input().split()) #격자 크기, 승객 수, 연료량
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

start_x,start_y=map(int, input().split()) #운전 시작 칸

# 주어진 좌표의 그래프는 1부터 이므로 -1을 해준다.
start_x, start_y = start_x-1, start_y-1
for i in range(m):
    pass_fir_x,pass_fir_y,pass_end_x,pass_end_y=map(int, input().split())
    graph[pass_fir_x-1][pass_fir_y-1]=(pass_end_x-1,pass_end_y-1) #승객의 위치에 목적지 좌표 삽입

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#택시가 승객을 태우러 가는 과정
def bfs(x,y,dist):
    q=deque()
    visited=[[0 for _ in range(n)]for _ in range(n)]
    q.append([x,y,dist])
    visited[x][y]=1
    passanger=[]
    max_dist=sys.maxsize

    while q:
        x,y,dist=q.popleft()
        if dist>max_dist: 
            continue
        # x,y가 승객좌표일때
        if graph[x][y]!=0 and graph[x][y]!=1:
            passanger.append([dist,x,y])
            max_dist=dist

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visited[nx][ny]==0:
                    q.append([nx,ny,dist+1])
                    visited[nx][ny]=1

    if passanger:
        return sorted(passanger)
    else:
        return False

# 승객의 목적지를 가는 과정
def move(x,y, endx,endy,dist):
    q=deque()
    visited=[[0 for _ in range(n)]for _ in range(n)]
    q.append([x,y,dist])
    visited[x][y]=1

    while q:
        x,y,dist=q.popleft()
        if (x,y)==(endx,endy):
            return dist
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=1:
                if visited[nx][ny]==0:
                    q.append([nx,ny,dist+1])
                    visited[nx][ny]=1

while m>0:
    res=bfs(start_x,start_y,0)

    #bfs 결과가 false면 승객을 못태운것이므로 -1
    if not res:
        print(-1)
        exit()
    
    near_pass=res[0]
    use_fuel=near_pass[0]
    x=near_pass[1]
    y=near_pass[2]

    fuel=fuel-use_fuel
    #연료가 0보다 적으면 실패
    if fuel<0:
        print(-1)
        exit()
    
    #목적지 좌표 설정
    pass_end_x, pass_end_y = (graph[x][y])[0], (graph[x][y])[1]
    graph[x][y]=0 #승객 위치는 빈칸으로 변경

    use_fuel=move(x,y,pass_end_x,pass_end_y,0)

    #move의 결과가 false면 목적지를 도달 못했으므로 실패
    if not use_fuel:
        print(-1)
        exit()
    
    fuel=fuel-use_fuel
    if fuel<0:
        print(-1)
        exit()
    
    fuel=fuel+2*use_fuel

    start_x=pass_end_x
    start_y=pass_end_y
    m-=1

print(fuel)
