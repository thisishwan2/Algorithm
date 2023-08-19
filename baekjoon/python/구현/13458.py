# 13458

# 1. 현재칸 청소x -> 현재칸 청소
# 2. 현재 칸 상하좌우 중 청소 안된 빈칸이 없을시 -> 바라보는 방향 유지, 한칸 후진가능 할시 한칸 후진후 1번으로 돌아감.
# 2-2. 뒤로 가련느데 벽인 경우 exit
# 3. 현재 칸 상하좌우 중 청소 안된 빈칸 존재시 -> 반시계 회전, 바라보는 방라보는 방향 기준 앞칸 청소 x시 전진, 1번으로 돌아감

import sys
input=sys.stdin.readline

# 0 상, 1 우, 2 하, 3 좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]


n,m=map(int, input().split())
r,c,d = map(int, input().split()) #x,y,방향

room=[]
for _ in range(n):
    room.append(list(map(int, input().split())))

visited=[[0 for _ in range(m)]for _ in range(n)]
count=0
while True:
    if room[r][c]==0 and visited[r][c]==0:
        count+=1
        visited[r][c]=1

    # 주변 4칸중 청소되지 않은 빈칸이 있는 경우
    if (room[r-1][c]==0 and visited[r-1][c]==0) or (room[r][c-1]==0 and visited[r][c-1]==0) or (room[r+1][c]==0 and visited[r+1][c]==0) or (room[r][c+1]==0 and visited[r][c+1]==0):
            
        # 방향 반시계 회전
        if d==0:
            d=3
        else:
            d=d-1
            
        # 바라보는 칸이 빈칸이고 청소되지 않으면 전진
        nr=r+dx[d]
        nc=c+dy[d] # 다음칸

        if room[nr][nc]==0 and visited[nr][nc]==0:
            r=nr
            c=nc

    # 주변 4칸중 청소되지 않은 빈칸이 없는 경우
    else:
        r=r-dx[d]
        c=c-dy[d]

        if room[r][c]==1:
            print(count)
            exit()



