from collections import deque
import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m = map(int, input().split())
lst=[]

for _ in range(n):
    lst.append(list(map(int, input().rstrip())))

visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m and lst[nx][ny]==0 and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1

count=0

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and lst[i][j]==0:
            bfs(i,j)
            count+=1
print(count)

'''
4 5
00110
00011
11111
00000
'''