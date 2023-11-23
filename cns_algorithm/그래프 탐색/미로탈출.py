from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        if (x,y)==(n-1,m-1):
            return visited[x][y]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1 and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1

print(bfs(0,0))

'''
5 6 
101010
111111
000001
111111
111111

'''