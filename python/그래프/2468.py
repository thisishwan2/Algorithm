#2468
#문제는 1~n-1 까지의 비가 내릴때 잠기지 않는 안전한 영역의 최대 개수를 찾는 문제

import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y,i):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        x,y = q.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>i and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1


n= int(input())

graph=[]
res=[]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#최대 비의양
maxi=0

for _ in range(n):
    a=list(map(int, input().split()))
    maxi=max(maxi,max(a))
    graph.append(a)

#비의 양(아무 지역도 물에 잠기지 않을 수도 있다.)
for i in range(0,maxi):
    visited=[[0]*n for _ in range(n)]
    cnt=0
    for j in range(n):
        for k in range(n):
            #비의 양보다 크고, 방문하지 않은곳.
            if graph[j][k]>i and visited[j][k]==0:
                bfs(j,k,i)
                cnt+=1
    res.append(cnt)

print(max(res))
