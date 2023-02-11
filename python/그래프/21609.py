#21609

# 블록은 검은색 블록(-1), 무지개 블록(0), 일반 블록(m가지 색상이 있음. m 이하의 자연수로 색상 표현)이 있다.
# 블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 
# 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 
# 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.(가장위, 가장 왼쪽)

# 1. 크기가 가장 큰 블록 그룹을 찾음. 단 여러개일시, 무지개 블록수가 제일 많은 그룹, 그것도 여러개면 가장 아래, 가장 오른쪽 블록
# 2. 찾은 블록그룹의 모든 블록 제거, 그룹에 포함된 블록수의 제곱점을 획득
# 3. 격자에 중력작용(내려갈수 있는 곳까지 내려감.)
# 4. 90반시계 회전
# 5. 격자 중력작용


import sys
input=sys.stdin.readline
from collections import deque

n,m = map(int, input().split()) #n: 격자 크기, m: 색상 개수
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#가장큰 블록그룹 찾기(일반 블록이 하나 이상있고, 일반 블록의 색은 동일해야함., 검은색 블록은 포함 불가. 무지개 블록은 상관없다. 그룹에는 2개 이상의 블록이 있어야함., 인접해야함.)
def bfs(x,y):
    i,j=x,y
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    total_cnt=1 #전체 블록수
    coordinate=[] #블록그룹 좌표 담을 리스트
    coordinate.append([x,y])

    rainbow_lst=[]

    #기준 블럭(기준 블럭은 무지개 블럭일 수 없다.)
    if graph[x][y]!=0:
        gizoon_x=x
        gizoon_y=y
    else:
        gizoon_x,gizoon_y=sys.maxsize,sys.maxsize

    #시작이 무지개 블럭이면, 무지개 블럭 개수를 1로 시작하고, 리스트에 넣는다.
    if graph[x][y]==0:
        rainbow=1
        rainbow_lst.append([x,y])
    else:
        rainbow=0

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                # 아직 방문하지 않았고, 검은색블럭, 빈칸이 아닐때
                if visited[nx][ny]==0 and graph[nx][ny]!=-1 and graph[nx][ny]!=-2:
                    # 그래프가 무지개블럭 혹은 같은색의 일반블럭이면 / 무지개 블럭이 탐색의 시작점이면 i,j=무지개 블럭의 좌표이므로 graph[i][j]=0이고 if문의 두 조건이 같은 것이된다.    
                    if graph[nx][ny]==0 or graph[nx][ny]==graph[i][j]:
                        q.append([nx,ny])
                        visited[nx][ny]=1
                        total_cnt+=1
                        coordinate.append([nx,ny])
                        #만약 무지개 블럭이면
                        if graph[nx][ny]==0:
                            rainbow+=1
                            rainbow_lst.append([nx,ny])
                        #무지개 블럭이 아니고, 일반 블럭이면
                        if graph[nx][ny]!=0:
                            if nx<gizoon_x and ny<gizoon_y:
                                gizoon_x,gizoon_y = nx,ny
    
    for i in rainbow_lst:
        visited[i[0]][i[1]]=0

    if total_cnt>=2 and total_cnt-rainbow>0:
        return total_cnt, rainbow, gizoon_x, gizoon_y, coordinate


def gravity_bfs(x,y):
    q=deque()
    q.append([x,y])

    while q:
        x,y=q.popleft()
        nx=x+1
        if 0<=nx<n and graph[nx][y]==-2:   #graph[nx][y]!=-1 and 
            q.append([nx,y])
    
    return x,y



#중력작용(검은색 블록 제외 아래로 이동)
def gravity():
    for i in range(n-2,-1,-1):
        for j in range(n):
            if graph[i][j]!=-1 and graph[i][j]!=-2 :
                x,y=gravity_bfs(i,j)
                graph[x][y]=graph[i][j]
                if (x,y)!=(i,j):
                    graph[i][j]=-2

score=0

#회전
def turn():
    turn_graph=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turn_graph[n-j-1][i]=graph[i][j]
    return turn_graph



while 1:
    visited=[[0 for _ in range(n)] for _ in range(n)]
    block_group=[] #크기가 같은 블록그룹 모음 리스트
    count=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0 and graph[i][j]!=-1 and graph[i][j]!=-2 and graph[i][j]!=0: #무지객 블록부터 시작하는 경우를 제외한다.(왜냐면 62번째줄을 보자)
                res=bfs(i,j)
                if res and count<=res[0]:
                    block_group.append(res)
                    count=res[0]
    
    if len(block_group)==0:
        print(score)
        exit()
    
    ans=sorted(block_group, key=lambda x : (-x[0], -x[1], -x[2],-x[3]))
    ans=ans[0]
    score+=count**2
    # 좌표 빈칸 처리 (빈칸을 -2로 처리)
    for i in ans[4]:
        graph[i[0]][i[1]]=-2
    
    #중력작용
    gravity()

    #90도 반시계 회전
    graph=turn()
    
    #다시 중력
    gravity()


# 놓쳤던 핵심은 바로 레인보우칸은 공유될수 있다. 즉, 한번 bfs 탐색도로 레이보우 칸의 방문은 초기화 시켜줘야함.