import sys
input=sys.stdin.readline
from collections import deque

h,w = map(int, input().split())
graph=[]
for _ in range(h):
    a=list(map(str, input().rstrip()))
    graph.append(a)

visited=[[0 for _ in range(w)]for _ in range(h)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def find_dir(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        nx2=x+2*dx[i]
        ny2=y+2*dy[i]

        if 0<=nx2<h and 0<=ny2<w:
            if (graph[nx][ny]=="#" and graph[nx2][ny2] == "#") and (visited[nx][ny]==0 and visited[nx2][ny2] == 0):
                visited[nx][ny]=1
                visited[nx2][ny2]=1
                return i, nx2, ny2
    return -1,-1,-1

def bfs(x,y,dir):
    q=deque()
    q.append([x,y,dir])

    while q:
        x,y,dir = q.popleft()
        next_dir, nx, ny = find_dir(x,y)

        if dir == next_dir:
            directions.append("A")
            q.append([nx,ny,next_dir])
            continue
        elif next_dir == -1:
            continue
        else:
            #방향전환
#  dir이 0일때, 좌는 2, 우는 3/ dir이 1일떼, 좌는 3, 우는2/ dir이 2일때 좌는 1, 우는 0/dir 3일때 좌는0, 우는 1/
            if dir==0:
                if next_dir==2:
                    directions.append("L")
                elif next_dir==3:
                    directions.append("R")
            elif dir==1:
                if next_dir==3:
                    directions.append("L")
                elif next_dir==2:
                    directions.append("R")
            elif dir==2:
                if next_dir==1:
                    directions.append("L")
                elif next_dir==0:
                    directions.append("R")
            elif dir==3:
                if next_dir==0:
                    directions.append("L")
                elif next_dir==1:
                    directions.append("R")
        directions.append("A")
        q.append([nx,ny,next_dir])


directions=["A"]

def start_dir(dir):
    if dir==0:
        print("^")
    elif dir==1:
        print("v")
    elif dir==2:
        print("<")
    else:
        print(">")


for i in range(h):
    for j in range(w):
        if graph[i][j]=="#":
            visited[i][j]=1
            dir,x,y = find_dir(i,j) # 0:상, 1:하. 2:좌, 3:우
            bfs(x,y,dir)
            print(i+1,j+1)
            start_dir(dir)
            print("".join(directions))
            exit()