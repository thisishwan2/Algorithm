#16928
#문제에서 체스판이라 해서 2차원 리스트 생각했지만, 단편적으로 쭉 늘어나있는 리스트로 생각하면 됨.

import sys
input=sys.stdin.readline
from collections import deque

#사다리 수(n), 뱀의 수(m)
n, m=map(int,input().split())

graph=[0]*101
visit=[0]*101

## 간선이다.
#사다리
for _ in range(n):
    x,y=map(int,input().split())
    graph[x]=y

#뱀
for _ in range(m):
    u,v=map(int, input().split())
    graph[u]=v


def bfs(x):
    q=deque()
    q.append(x)

    while q:
        x=q.popleft()
        if x==100:
            break
        for i in range(1,7):
            nx=x+i
            if 1<=nx<=100 and visit[nx]==0:
                #사다리나 뱀 칸에 갔을때
                if graph[nx]!=0:
                    q.append(graph[nx])
                    #처음 풀때 아래의 if문을 생각하지 않았다. 하지만 문제는 틀렸고, 이유를 찾았다.
                    #반례를 먼저 보면 1 1
                    #             13 99
                    #             8 7
                    #과 같이 예시가 있을때, 아래처럼 if문이 없는경우 7번째 visit가 원래는 1+6이기 때문에 주사위를 한번만 굴려도 되지만,
                    #8의 사다리를 타고 7로 가개 되는 경우 주사위를 1+1+6->7이므로 7에 2번 굴린 값으로 덮어 씌인다.
                    #따라서 한번 visit에 값이 들어간 경우는 변경하지 못하도록 아래의 if문을 작성했다.
                    if visit[graph[nx]]==0:
                        visit[graph[nx]]=visit[x]+1
                    visit[nx]=visit[x]+1
                #그냥 아무것도 아닌 칸을 갔을때
                else:
                    q.append(nx)
                    visit[nx]=visit[x]+1
bfs(1)
print(visit[-1])