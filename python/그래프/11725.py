#처음에 문제의 출력 부분과 예제 출력 부분을 보고 이해를 못했었는데, 문제를 풀어서 얘기해보면
#1번 노드를 루트로 잡고, 그후에 2번 노드의 부모 노드를 순차적으로 출력하면 되는 문제였다.
#상당히 애먹었던 문제

import sys
from collections import deque
sys.setrecursionlimit(1000000)


def dfs(v):
    for i in graph[v]:
        if visited[i]==0:
            #이부분이 부모의 노드를 담는 부분이다.
            visited[i]=v
            dfs(i)

n=int(sys.stdin.readline())

graph=[[] for _ in range(n+1)]

visited=[0]*(n+1)

for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    #메모리 낭비를 줄이기 위해 갈수 있는 그래프 연결 상태만 표시(양방향 연결 대신)
    graph[a].append(b)
    graph[b].append(a)
#1번 노드부터 순차적으로 탐색
dfs(1)

for i in range(2,n+1):
    print(visited[i])