import sys
from collections import deque
input=sys.stdin.readline

# 북, 동, 남, 서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def check_near(x,y,arr):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==0:
                return True

    return False


# 방 크기 n*m
n,m = map(int, input().split())

# 로봇 청소기 처음 좌표 및 바라보는 방향 r,c,d
r,c,d = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

q=deque()
q.append([r,c,d])
cnt = 0

while q:
    x,y,d = q.popleft()

    if arr[x][y]==0:
        cnt+=1
        arr[x][y]=-1

    # 현재 칸의 주변 4칸 중 청소된 칸을 확인
    if (check_near(x,y,arr)): # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        d=(d-1)%4 # 90도 회전(반시계)
        nx = x+dx[d]
        ny = y+dy[d]

        # 바라보는 방향을 기준으로 앞쪽이 청소되지 않은 빈칸인 경우
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==0:
                # 전진
                q.append([nx,ny,d])
                continue
        # 바라보는 방향이 청소되지 않은 칸이면 현재 칸을 큐에 다시 담음
        q.append([x,y,d])

    else: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        # 바라보는 방향을 유지하면서, 후진 할 수 있는지 확인
        back = (d+2)%4

        nx = x+dx[back]
        ny = y+dy[back]

        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] !=1:
                q.append([nx,ny,d])
            else:
                break
print(cnt)

