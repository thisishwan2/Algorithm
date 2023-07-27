#17144 로테이션이 조금까다로웠음.
# 확산은 생각보다 쉬움.

import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def spread():
    room_spread=[[0 for _ in range(c)]for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if room[i][j]>0:
                dir_cnt=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        if room[nx][ny]!=-1:
                            dir_cnt+=1
                            room_spread[nx][ny]+=room[i][j]//5
                
                room[i][j]=room[i][j]-((room[i][j]//5)*dir_cnt)

    
    for i in range(r):
        for j in range(c):
            room[i][j]=room[i][j]+room_spread[i][j]

def moveup(air_x, air_y):

    for i in range(air_x-2,-1,-1):
        room[i+1][0]=room[i][0]
    
    for i in range(1, c):
        room[0][i-1]=room[0][i]
    
    for i in range(0, air_x):
        room[i][c-1]=room[i+1][c-1]
    
    for i in range(c-1,1,-1):
        room[air_x][i]=room[air_x][i-1]
    
    room[air_x][air_y+1]=0

def movedown(air_x, air_y):

    for i in range(air_x+2,r):
        room[i-1][0]=room[i][0]
    
    for i in range(c-1):
        room[r-1][i]=room[r-1][i+1]

    for i in range(r-2,air_x-1,-1):
        room[i+1][c-1]=room[i][c-1]
    
    for i in range(c-1,0,-1):
        room[air_x][i]=room[air_x][i-1]
    
    room[air_x][air_y+1]=0

r,c,t= map(int, input().split())
room=[]
for _ in range(r):
    room.append(list(map(int, input().split())))

# 앞에 있는 것이 윗쪽 공기청정기, 뒤에 있는 것이 아래쪽 청정기
air_cleaner=[]

for i in range(r):
    for j in range(c):
        if room[i][j]==-1:
            air_cleaner.append([i,j])

cnt=0
while t!=cnt:
    spread()
    moveup(air_cleaner[0][0], air_cleaner[0][1])
    movedown(air_cleaner[1][0], air_cleaner[1][1])
    cnt+=1


total=2
for i in range(r):
    for j in range(c):
        total+=room[i][j]

print(total)

