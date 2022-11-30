#2644

import sys
from collections import deque

#전체 사람 수
n=int(sys.stdin.readline())

#촌수 계산 하는 두 사람의 번호(ex 나와 아버지의 형제)
num1, num2 = map(int,sys.stdin.readline().split())

#부모 자식간의 관계의 수 = 연결된 노드의 수
m=int(sys.stdin.readline())

graph=[[]for _ in range(n+1)]

#방문처리
visited=[0]*(n+1)
#거리를 저장할 리스트(촌수)
res=[0]*(n+1)

for _ in range(m):
    x, y=map(int, sys.stdin.readline().split())
    #그래프를 이렇게 설정해놓으면 num1의 그래프에 대해서만 bfs를 돌게 될것이다.(떨어진 두 그래프는 연결요소가 없기 때문.)
    graph[x].append(y)
    graph[y].append(x) #이부분을 빼먹었다. 처음에는 루트노드를 당연히 1이라고 생각하고 문제를 풀었는데, 예제의 루트가 1이었지, 항상 그럴 보장은 없다.
                        #따라서 문제 풀이를 루트에서 내려가면서 간선마다 1을 더하는게 아닌. 양방향으로 움직일 수 있게 그래프를 만들어 놓고,
                        #촌수계산하는 첫번째 숫자부터 두번째 숫자까지 찾으러 가는 방식으로 바꿨다.

#bfs 
def bfs(v):
    q=deque()
    q.append(v)
    visited[v]=True

    while q:
        v=q.popleft()
        for i in graph[v]:
            if visited[i]==0:
                q.append(i)
                #이 과정이 촌수를 처리하는 과정이다.
                res[i]=res[v]+1
                visited[i]=True
    #촌수 계산하는 두번째 수까지의 거리가 0보다 크면 같은 그래프 안에 있는것이고, 아니면 서로 독립적인 그래프이다
    if res[num2]>0:
        print(res[num2])
    else:
        print(-1)
bfs(num1)

#dfs
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            res[i]=res[v]+1
            dfs(i)