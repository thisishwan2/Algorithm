#9205
#생각보다 정말 까다로웠던 문제
#맥주 한박스엔 20개가 있다. 50미터가려면 직전에 한병을 먹음. 
#처음에 설계를 단방향으로 했는데, 양방향으로 설계해야 한다.
#왜냐하면, 편의점 1에서 편의점 2로도 갈 수 있으면서, 편의점 2에서 편의점 1로도 갈 수 있기 때문이다.
#1
#2
#0 0
#1000 1000
#1000 0
#2000 1000

import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[0]=1
    while q:
        x,y=q.popleft()
        for i in range(1,n+2):
            #abs를 안해줘서 음수가 나오는 경우가 발생했다. 즉, -1000 까지 허용인데, -2000 이렇게 되는경우도 그냥 통과됐다. 따라서
            # abs를 해줘서 1000 이하의 값만 통과하도록 한다. 
            # 예)
            # 1
            # 4
            # 2000 0
            # 1000 0
            # 0 0
            # 0 1000
            # 0 2000
            # 1000 2000 
            nx=abs(graph[i][0]-(x))
            ny=abs(graph[i][1]-(y))
            if nx+ny<=1000 and visited[i]==0:
                q.append([graph[i][0],graph[i][1]])
                visited[i]=1

t=int(input())
for _ in range(t):
    n=int(input())
    graph=[]
    visited=[0]*(n+2)

    for _ in range(n+2):
        #집, 쳔의점, 펜타포트 좌표
        x, y= map(int, input().split())
        graph.append([x,y])

    bfs(graph[0][0],graph[0][1])

    if visited[-1]==1:
        print("happy")
    else:
        print("sad")
    '''
    아래와 같이 풀면 예를 들어 펜타포스의 위치가 첫번째 편의점을 들리고, 바로 갈 수 잇는데,
    아래의 코드는 무조건 순차적으로 편의점을 다 돌고 펜타포스를 간다. 이럴때 만약 두번째 편의점이
    멀리있는 경우에는 원래 답음 happy이지만 sad 가 나올 수 있다.
    예)
    1
    2
    0 0(집)
    1000 0(편의점1)
    2000 1000(편의점2)
    1000 1000(펜타포트)

    beer=20
    able_meter=50

    cnt=0
    for _ in range(n+2):
        #집, 쳔의점, 펜타포트 좌표
        x, y= map(int, input().split())
        graph.append([x,y])
    
    for i in range(1, n+2):
        if (graph[i][0]-graph[i-1][0])+(graph[i][1]-graph[i-1][1])<=beer*able_meter:
            cnt+=1
    
    if cnt==n+1:
        print("happy")
    else:
        print("sad")
        '''