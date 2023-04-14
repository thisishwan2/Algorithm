# 이 문제는 문제 그대로 로봇이 지나간 경로가 단 하나뿐이다.
# 처음에는 로봇이 간 경로가 아래와 같이 이어지는 경우(?) 그니까 bfs돌릴때 경로가 2개 나올 수도 있겠다 생각했는데,
# #####
    # #
    ### 

# 기본적으로 이문제는 앞으로 갈때 2칸씩 전진하므로 위의 상황을 고려할 필요가 없다.

import sys
input=sys.stdin.readline
from collections import deque

# 상우하좌 방향으로 설정(이유는 좌회전, 우회전을 표현하기 위해 인덱스를 이용할 것이기 때문.)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
directions = ['^','>','v','<']

h,w = map(int, input().split())
graph=[]
for _ in range(h):
    a=list(input().rstrip())
    graph.append(a)

visited=[[0 for _ in range(w)]for _ in range(h)]
ans=[]

#check 함수를 통해 시작점을 얻을 수 있다.
def check(x,y):
    cnt=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<h and 0<=ny<w and graph[nx][ny]=="#":
            start = directions[i]
            cnt+=1
    # 이조건이 결국 현위치에서 갈수있는 상하좌우칸중 #이 하나만 있는것 -> 즉, 출발점
    if cnt>1:
        return False
    return start # 문자열을 반환하는 이유는 파이썬 조건문에서 비어있지 않은 문자열은 True로 인식한다.

#모든 방향의 정보를 담을 bfs 탐색
def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    path=[] #방향을 담을 리스트

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            direction=directions[i] #경로를 문자열로 가져옴 ex ">"

            if 0<=nx<h and 0<=ny<w and graph[nx][ny]=="#" and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny])
                path.append(direction) #경로를 path에 넣음.
    return deque(path) #큐로 path 반환 

for i in range(h):
    for j in range(w):
        if graph[i][j]=="#" and check(i,j): #check가 문자열이 반환되면 True, Flase반환이면 False
            trace = bfs(i,j)
            print(i+1,j+1)
            print(trace[0])

            cur = trace.popleft() #첫번째 시작 방향을 저장.
            cnt=1
            for next in trace:
                if cur == next: #다음 방향의 문자열이 현재 방향 문자열과 같으면
                    cnt+=1

                    if cnt%2==0: #만약 cnt가 2이면 2칸 전진한것이므로
                        ans.append('A')
                        cnt=0
                # 방향이 다르면        
                else:
                    # 현재 방향의 인덱스-1(현위치 기준으로 좌측인덱스)이 다음이면
                    if directions[directions.index(cur)-1]==next:
                        ans.append("L")
                    # 현재 방향의 인덱스+1(현위치 기준으로 우측인덱스)이 다음이면
                    else:
                        ans.append("R")
                    #참고로 위의 ans.append()는 그쪽 방향으로 방향전환하고 한칸 간것을 의미함.
                    cur=next
                    cnt=1 # 한칸 간것으로 설정해줌.
            
            for i in ans:
                print(i, end="")
            exit()