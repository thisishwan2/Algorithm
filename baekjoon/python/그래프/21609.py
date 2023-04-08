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

#가장큰 블록그룹 찾기
def bfs(x,y,color):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    #기준 블럭
    standard_block_x=x
    standard_block_y=y

    total_cnt, rainbow =1,0 #전체 블록수, 무지개 블럭 수
    normal, rainbow_lst = [[x,y]],[] #일반 블럭, 무지개 블럭 좌표 리스트

    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                # 아직 방문하지 않았고, 일반블럭일때
                if visited[nx][ny]==0 and graph[nx][ny]==color:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    normal.append([nx,ny])
                    total_cnt+=1
                # 아직 빙문하지 않았고, 무지개 블럭일때
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    rainbow_lst.append([nx,ny])
                    total_cnt+=1
                    rainbow+=1
    
    # 무지개의 방문처리는 초기화(이후 탐색에서 중복으로 사용될 수 있음.)
    for x,y in rainbow_lst:
        visited[x][y]=0

    return total_cnt, rainbow, standard_block_x, standard_block_y, normal+rainbow_lst # 총 갯수, 무지개 갯수, 기준블럭, 해당 블럭들의 좌표

# 아랫 방향으로 어디까지 갈 수 있는지 탐색
def gravity_bfs(x,y):
    q=deque()
    q.append([x,y])

    while q:
        x,y=q.popleft()
        nx=x+1
        #범위내에 다음이 빈칸이면,
        if 0<=nx<n and graph[nx][y]==-2:
            q.append([nx,y])
    #갈수있는 제일 아래의 x,y를 반환
    return x,y

#중력작용(검은색 블록 제외 아래로 이동)
def gravity():
    for i in range(n-2,-1,-1): #밑의 한줄 위부터 체크한다.(맨 밑줄은 내려갈 곳이 없음.)
        for j in range(n):
            #블럭이 일반 혹은 무지개 블럭이면
            if graph[i][j]>=0 :
                x,y=gravity_bfs(i,j)
                graph[x][y]=graph[i][j] #이동
                #만약 처음좌표와 탐색결과의 좌표가 같지 않다면,
                if (x,y)!=(i,j):
                    #처음 자리는 빈칸으로 변경
                    graph[i][j]=-2

#회전
def turn():
    turn_graph=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turn_graph[n-j-1][i]=graph[i][j]
    return turn_graph


import sys
input=sys.stdin.readline
from collections import deque

n,m = map(int, input().split()) #n: 격자 크기, m: 색상 개수
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#점수
score=0

#오토 플레이
while 1:
    visited=[[0 for _ in range(n)] for _ in range(n)] #방문 체크
    block_group=[] #블럭 그룹
    count=0 #인접한 블럭 수

    # bfs 탐색할때, i,j 가 기준블럭이 된다.(기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.)
    for i in range(n):
        for j in range(n):
            #방문하지 않았고, 일반 블록일 경우(무지개 블록이 시작하는 경우를 제외) ->  무지개 블럭 부터 탐색할 경우 bfs 에서 같은 색의 블럭을 찾을때 무지개 블럭만 찾게됨.
            if visited[i][j]==0 and graph[i][j]>0:
                res=bfs(i,j,graph[i][j]) # res= (총 갯수, 무지개 갯수, 해당 블럭들의 좌표)
                
                # res 가 None 이 아니고, 전체 블럭의 수가 count 보다 크고 2보다 크거나 같은 경우만 필터링한다.
                if res and count<=res[0] and res[0]>=2:
                    block_group.append(res)
                    count=res[0]
    
    #bfs 탐색을 했는데, 가능한 블럭 그룹이 없으면 종료.
    if len(block_group)==0:
        print(score)
        exit()
    
    # 내림차순으로 정렬
    ans=sorted(block_group, key=lambda x : (-x[0], -x[1], -x[2],-x[3]))
    #정렬 결과중 맨 앞의 것이 조건에 부합하는 블럭 그룹
    ans=ans[0]
    score+=count**2

    # 좌표 빈칸 처리 (빈칸을 -2로 처리)
    for x,y in ans[4]:
        graph[x][y]=-2

    #중력작용
    gravity()

    #90도 반시계 회전
    graph=turn()
    
    #다시 중력
    gravity()


# 놓쳤던 핵심은 바로 레인보우칸은 공유될수 있다. 즉, 한번 bfs 탐색도로 레이보우 칸의 방문은 초기화 시켜줘야함.