#15685
# 겹칠수 잇음

import sys
input=sys.stdin.readline

graph=[[0 for _ in range(101)]for _ in range(101)]

dx=[0,-1,0,1] #문제에서 y좌표(위아래)
dy=[1,0,-1,0] #문제에서 x좌표(좌우)

n=int(input())
for _ in range(n):
    x,y,d,g = map(int,input().split())
    graph[y][x]=1

    arr=[-1]*(2**g)
    arr[0]=d

    for i in range(1,g+1):
        cnt=2**(i-1)
        for j in range(2**(i-1)-1,-1,-1):
            if arr[j]==3:
                arr[cnt]=0
                cnt+=1
            else:
                arr[cnt]=arr[j]+1
                cnt+=1
    
    for i in arr:
        nx=y+dx[i]
        ny=x+dy[i]
        if 0<=nx<=100 and 0<=ny<=100:
            graph[nx][ny]=1
            x=ny
            y=nx

square=0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1:
            if graph[i][j+1]==1 and graph[i+1][j]==1 and graph[i+1][j+1]==1:
                square+=1

print(square)