import sys
from collections import deque
input = sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,n,m,room):
    q=deque()
    q.append([x,y])

    start = room[x][y]

    visited = [[0 for _ in range(m)]for _ in range(n)]
    visited[x][y]=1

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==0 and room[nx][ny]!=0:
                    q.append([nx,ny])
                    visited[nx][ny]=visited[x][y]+1

    maximum_dist=0

    for i in range(n):
        maximum_dist=max(maximum_dist,max(visited[i]))

    ans = 0
    for i in range(n):
        for j in range(m):
            if maximum_dist == visited[i][j]:
                    ans = max(ans,start+room[i][j])

    # print(ans)
    return ans, maximum_dist



n,m = map(int, input().split())

room = []

for i in range(n):
    room.append(list(map(int, input().split())))

answer=[]

for i in range(n):
    for j in range(m):
        if room[i][j]==0:
            continue
        else:
            ans, dist = bfs(i,j,n,m,room)
            answer.append([dist, ans])

answer = sorted(answer, key=lambda x:(x[0],x[1]), reverse=True)
if len(answer)==0:
    print(0)
else:
    print(answer[0][1])