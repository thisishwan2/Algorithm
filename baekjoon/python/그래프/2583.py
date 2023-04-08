#2583
#미로찾기 2178과 유사
#이 문제는 dfs가 더 빠를것 같다.

import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    area=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1
                area+=1
    res.append(area)

    

m, n, k = map(int, input().split())

graph=[[1 for i in range(n)] for j in range(m)]
visited=[[0 for _ in range(n)] for _ in range(m)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#영역갯수
cnt=0
# 넓이 리스트
res=[]

for _ in range(k):
    #입력받는 값 규칙이 x1,y1은 그대로고, x2, y2는 -1을 해야함. 미로를 그려보면 알 수 있다.
    x1, y1, x2, y2=map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            #i, j유의
            graph[j][i]=0
            visited[j][i]=1

for i in range(m):
    for j in range(n):
        if visited[i][j]==0:
            bfs(i,j)
            cnt+=1

res.sort()
res=[str(a) for a in res]

print(cnt)
print(" ".join(res))

'''
dfs
import sys
sys.setrecursionlimit(10000)

def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)
    return cnt
    
M, N, K = map(int, input().split())
graph = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            res.append(dfs(i, j, 1))
print(len(res))
print(*sorted(res))

'''