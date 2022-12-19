#16954

#욱제의 캐릭터는 가장 왼쪽 아랫 칸에 있고, 이 캐릭터는 가장 오른쪽 윗 칸으로 이동해야 한다.
#1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 아래에 행이 없다면 벽이 사라지게 된다. 
#욱제의 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있다.
#벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.(벽이랑 욱제가 겹치면 이동 불가)
# '.'은 빈 칸, '#'는 벽이다.

'''
#1번 풀이 시간 제일 빠름.
import sys
input=sys.stdin.readline
from collections import deque

chase=[]


#상, 하, 좌, 우, 좌상, 우상, 좌하, 우하, 제자리
dx=[-1,1,0,0,-1,-1,1,1,0]
dy=[0,0,-1,1,-1,1,-1,1,0]

for _ in range(8):
    chase.append(list(map(str,input().rstrip())))

q=[(7,0)]
q0=[]
canOut=1

for _ in range(8):
    while q:
        x,y=q.pop()
        if chase[x][y]=="#":
            continue
        else:
            for i in range(9):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<8 and 0<=ny<8:
                    if chase[nx][ny] =="#":
                        continue
                    if (nx,ny) not in q0:
                        q0.append([nx,ny])
    chase.pop()
    chase.insert(0, [".", ".", ".", ".", ".", ".", ".", "."])
    if not q0: canOut=0
    q=q0
    q0=[]
if canOut:print(1)
else: print(0) 
'''


#두번째 풀이

import sys
input=sys.stdin.readline
from collections import deque

chase=[]


#상, 하, 좌, 우, 좌상, 우상, 좌하, 우하, 제자리
dx=[-1,1,0,0,-1,-1,1,1,0]
dy=[0,0,-1,1,-1,1,-1,1,0]

for _ in range(8):
    chase.append(list(map(str,input().rstrip())))

def bfs(x,y):
    q=deque()
    q.append([x,y])

    while q:
        visited = [[0] * 8 for _ in range(8)]
        for _ in range(len(q)):
            x,y=q.popleft()
            if (x,y)==(0,7):
                return 1
            if chase[x][y]=="#":
                continue

            for i in range(9):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<8 and 0<=ny<8 and chase[nx][ny]=="." and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append([nx,ny])
        chase.pop()
        chase.insert(0, [".", ".", ".", ".", ".", ".", ".", "."])
    return 0

print(bfs(7,0))

'''
#처음 풀은 풀이 3차원을 이용해서 제자리에 있는것을 표현
#그런데 굳이 3차원일 필요가 없었다. 왜냐면 방문처리를 벽이 움직일때마다 초기화 시키기 때문이다.
import sys
input=sys.stdin.readline
from collections import deque

chase=[]


#상, 하, 좌, 우, 좌상, 우상, 좌하, 우하, 제자리
dx=[-1,1,0,0,-1,-1,1,1,0]
dy=[0,0,-1,1,-1,1,-1,1,0]

for _ in range(8):
    chase.append(list(map(str,input().rstrip())))

#벽이 이동하는 함수
def move_wall():
        chase.pop()
        chase.insert(0,[".", ".", ".", ".", ".", ".", ".", "."])

#0이 제자리 안있은거 1이 제자리 잇는거
def bfs(x,y):
    q=deque()
    q.append([x,y,0])


    while q:
        visit=[[[0 for _ in range(2)]for _ in range(8)]for _ in range(8)]
        for i in range(len(q)):

            x,y,move=q.popleft()

            if chase[x][y]=="#":
                continue

            if (x,y)==(0,7):
                print(1)
                exit()

            for i in range(9):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<8 and 0<=ny<8:
                    if i==8 and visit[nx][ny][1]==0 and chase[nx][ny]==".":
                        q.append([nx,ny,0])
                        visit[nx][ny][1]=1
                    elif visit[nx][ny][0]==0 and chase[nx][ny]==".":
                        q.append([nx,ny,0])
                        visit[nx][ny][0]=1
           
        move_wall()
    print(0)

bfs(7,0)

'''