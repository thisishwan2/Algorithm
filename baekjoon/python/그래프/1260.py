#1260 처음 푼 틀린코드

'''import sys
from collections import deque


def dfs(graph, node, visit_dfs):
    visit_dfs[node]=True

    print(node, end=" ")

    for i in graph[node]:
        if not visit_dfs[i]:
            dfs(graph, i, visit_dfs)

def bfs(graph, node, visit_bfs):
    q=deque([node])
    visit_bfs[node]=True

    while q:
        v=q.popleft()
        print(v, end=" ")

        for i in graph[node]:
            if not visit_bfs[i]:
                q.append(i)
                visit_bfs[i]=True


n, m, v=map(int, sys.stdin.readline().split())

graph=[0]*(m+1)

for i in range(1,m+1):
    a=list(map(int, sys.stdin.readline().split()))
    graph[i]=a

real_graph=[]
#이부분 구현을 내가 알던 예제와 동일하게 만드려고 했지만, 결국 틀렸다.
for i in range(1, n+1):
    a=[]
    for j in range(1,m+1):
        if i in graph[j]:
            lst=list(graph[j])
            lst.remove(i)
            a+=lst
    real_graph.append(a)

real_graph.insert(0, [])

visit_dfs=[False]*(n+1)
visit_bfs=[False]*(n+1)

dfs(real_graph, 1, visit_dfs)
print()
bfs(real_graph, 1, visit_bfs)'''

#이번 문제의 핵심은 양방향이라는 것이다.

from collections import deque

# n=정점개수, m=간선개수, v=탐색시작점
n, m, v = list(map(int, input().split()))

# 인접영행렬
matrix = [[0]*(n+1) for i in range(n+1)]

#방문한곳체크기록할 리스트
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

# 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
for i in range(m):
    a,b=map(int,input().split())
    matrix[a][b]=matrix[b][a]=1 #양방향이므로 a,b = b,a 다 true(연결되어 있다.)

def dfs(v):
    visited_dfs[v]=True
    print(v, end=" ")
    for i in range(1,n+1):
        # visited 가 flase(즉, 아직 방문 안한 노드이고, 인접해있는 노드(matrix==1) 일때)
        if not visited_dfs[i] and matrix[v][i]==1:
            dfs(i)

def bfs(v):
    visited_bfs[v]=True
    q=deque([v])

    while q:
        v=q.popleft()
        print(v,end=" ")
        for i in range(1,n+1):
            if not visited_bfs[i] and matrix[v][i]==1:
                q.append(i)
                visited_bfs[i]=True

dfs(v)
print()
bfs(v)