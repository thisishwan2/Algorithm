#11724
#bfs
import sys
from collections import deque

n,m= map(int, sys.stdin.readline().split())

graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u][v]=graph[v][u]=1
'''
또 다른 그래프 설정 방법. 2중리스트인데 리스트 안에 인접하는 노드 번호를 적어 놓는다.
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

이렇게 그래프를 설정시 이후 코드는 아래아 같다.
# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

'''
visited=[0]*(n+1)

#a는 시작 위치 (루트 노드)
def bfs(a):
    visited[a]=1
    q=deque()
    q.append(a)

    while q:
        a=q.popleft()
        for i in range(1,n+1):
            if visited[i]==0 and graph[a][i]==1:
                q.append(i)
                visited[i]=1

#연결요소 개수
cnt=0

for i in range(1,n+1):
    if visited[i]==0:
        bfs(i)
        cnt+=1

print(cnt)


#dfs
import sys
#재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다.
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다.
# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다.
# 때문에 sys.setrecursionlimit(10000) 처럼 작성해야 한다.
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
