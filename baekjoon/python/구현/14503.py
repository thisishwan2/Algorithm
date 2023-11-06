#14503

# 본 문제의 고생 포인트는 작동 방식에 명시된 '청소되지 않은 빈 칸'이다. 즉, 빈칸이면서 청소도 안되어 있어야 한다. 따라서 청소 됨, 청소 안됨, 빈칸, 벽이 구분되어야 하고, 이동하는 것은 벽만 아니면 이동이 가능한것,

import sys
input = sys.stdin.readline

# 상 우 하 좌(d=0,1,2,3)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m = map(int, input().split())
room = []

x,y,d = map(int, input().split()) # 처음 로봇 청소기 좌표 r,c 방향 d

for i in range(n):
    line = list(map(int, input().split()))
    room.append(line)

count=0
visit=[[0 for i in range(m)]for _ in range(n)]
while True:
    if room[x][y]==0:
        visit[x][y]=1 # 청소 표시

    if d<0:
        d=d+4

    # 현재칸 주변 4칸중 벽이 아니고, 청소되지 않은 빈칸인 경우
    if (room[x-1][y]==0 and visit[x-1][y]==0) or (room[x+1][y]==0 and visit[x+1][y]==0) or (room[x][y-1]==0 and visit[x][y-1]==0) or (room[x][y+1]==0 and visit[x][y+1]==0):

       # 반시계 회전
        d = d - 1

        if room[x + dx[d]][y + dy[d]] == 0 and visit[x+dx[d]][y+dy[d]]==0:
            x = x + dx[d]
            y = y + dy[d]

    else:
        # 바라보는 방향을 유지한채로 한칸 후진 시도후
        if room[x + dx[d - 2]][y + dy[d - 2]] == 0:
            x = x + dx[d - 2]
            y = y + dy[d - 2]
            continue
        else:
            break

sum=0
for i in range(n):
    for j in range(m):
        if visit[i][j]==1:
            sum+=1
print(sum)