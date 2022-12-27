#5427
#불->상근->불 형태로 진행시킨다.(불이 날 예정인 지점은 이동하지 못하므로 불, 상근이 순으로 이동한다)

import sys
input=sys.stdin.readline
from collections import deque

def bfs(x,y):
    visited[x][y]=1
    q.append([x,y])

    while q:
        #이처럼 큐 길이만금 for문이 돌게해서, 정해진 큐가 다 돌면(한번에 갈수있는 움직임) 불이 움직일 차례
        for i in range(len(q)):
            x,y=q.popleft()
            for j in range(4):
                nx=x+dx[j]
                ny=y+dy[j]
                if 0<=nx<h and 0<=ny<w:
                    if buliding[nx][ny]=="." and visited[nx][ny]==0:
                        q.append([nx,ny])
                        visited[nx][ny]=visited[x][y]+1
                #상근이가 (0,0) ~ (h-1,w-1) 범위를 벗어나면 탈출에 성공했으므로 걸린 시간을 출력
                elif nx<0 or nx>=h or ny<0 or ny>=w:
                    print(visited[x][y])
                    return
        fire()
    
    print("IMPOSSIBLE")
    return

def fire():
    #큐에 있는만큼의 불만 움직이도록 큐의 길이만큼 for문을 돌린다.
    for i in range(len(fq)):
        x,y=fq.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<h and 0<=ny<w:
                if buliding[nx][ny]==".":
                    fq.append([nx,ny])
                    buliding[nx][ny]="*"

t= int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(t):
    w, h=map(int, input().split())
    buliding=[]
    for _ in range(h):
        buliding.append(list(map(str, input().rstrip())))
    
    fq=deque()
    q=deque()
    visited=[[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if buliding[i][j]=="@":
                x,y=i,j
                buliding[i][j]="."

            elif buliding[i][j]=="*":
                fq.append([i,j])
    fire()
    bfs(x,y)