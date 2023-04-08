#9328

import sys
input=sys.stdin.readline
from collections import deque

#그래프의 가장자리를 감싸는 빈칸 생성(이렇게 하면 굳이 그래프의 가장자리를 찾지 않아도 된다.)
def new_map():
    for i in graph:
        i.insert(0,".")
        i.append(".")
    graph.insert(0, ["."]*(w+2))
    graph.append(["."]*(w+2))

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited=[[0 for _ in range(w+2)] for _ in range(h+2)]
    visited[x][y]=1
    file=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<h+2 and 0<=ny<w+2 and visited[nx][ny]==0:
                
                #다음칸이 빈칸
                if graph[nx][ny]==".":
                    q.append([nx,ny])
                    visited[nx][ny]=1

                #다음 칸이 열쇠면 방문과 큐를 초기화 시켜야하고, 키를 저장한다.
                elif str(graph[nx][ny]).islower():
                    keys.append(str(graph[nx][ny]))
                    q.clear()
                    visited=[[0 for _ in range(w+2)] for _ in range(h+2)]
                    q.append([nx,ny])
                    graph[nx][ny]="."
                    visited[nx][ny]=1

                #다음칸이 대문자=문일경운
                elif str(graph[nx][ny]).isupper():
                    if str(graph[nx][ny]).lower() in keys:
                        visited[nx][ny]=1
                        graph[nx][ny]="."
                        q.append([nx,ny])

                #다음칸이 문서일 경우
                elif graph[nx][ny]=="$":
                    visited[nx][ny]=1
                    file+=1
                    graph[nx][ny]="."
                    q.append([nx,ny])

    print(file)            

t = int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(t):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    keys = list(map(str,input().strip()))

    #열수 있는 문은 미리 열어 놓는다.
    for i in range(h):
        for j in range(w):
            if graph[i][j].isupper()==True and graph[i][j].lower() in keys:
                graph[i][j]="."
    
    new_map()
    bfs(0,0)





"""

처음푼 틀린코드

import sys
input=sys.stdin.readline
from collections import deque

t=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
alphabet_list_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_list_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


for _ in range(t):

    h,w = map(int, input().split())

    graph=[]
    for _ in range(h):
        graph.append(list(input().rstrip()))
    key_lst=list(input().rstrip())

    key_dict={}
    for i in key_lst:
        key_dict[i]=i.upper()

    def bfs(x,y):
        global file
        global visited
        
        if graph[x][y] in alphabet_list_upper:
            if str(graph[x][y]).lower() in key_dict:
                graph[x][y]="*"
            else:
                return
        
        q=deque()
        q.append([x,y])
        visited[x][y]=1

        while q:
            x,y,=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<h and 0<=ny<w:
                    #다음칸이 빈칸이고, 방문하지 않은 경우
                    if graph[nx][ny]=="." and visited[nx][ny]==0:
                        q.append([nx,ny])
                        visited[nx][ny]=1
                    #다음칸이 문인데, 키가 있고, 방문하지 않은 경우
                    elif str(graph[nx][ny]).lower() in key_dict and visited[nx][ny]==0:
                        graph[nx][ny]="."
                        q.append([nx,ny])
                        visited[nx][ny]=1
                    #다음칸이 열쇠이고, 방문하지 않은 경우
                    elif str(graph[nx][ny]) in alphabet_list_lower and visited[nx][ny]==0:
                        visited=[[0 for _ in range(w)]for _ in range(h)]
                        visited[nx][ny]=1
                        q.clear()
                        q.append([nx,ny])
                        key_dict[str(graph[nx][ny])]=str(graph[nx][ny]).upper()
                        graph[nx][ny]="."
                    #다음칸이 문서이고, 방문하지 않은 경우
                    elif graph[nx][ny]=="$" and visited[nx][ny]==0:
                        file+=1
                        q.append([nx,ny])
                        visited[nx][ny]=1
                        graph[nx][ny]="."

    file=0
    visited=[[0 for _ in range(w)]for _ in range(h)]
    
    # 탐색전 가장자리 요소 탐색
    for i in range(h):
        if i==0 or i==h-1:
            for j in range(w):
                if graph[i][j]=="*": # 가장자리가 벽이면
                    continue
                elif graph[i][j]==".": #가장자리가 빈칸이면
                    continue
                elif graph[i][j]=="$": #가장자리가 문서면
                    file+=1
                    graph[i][j]="*"
                elif str(graph[i][j]) in alphabet_list_lower: #가장자리에 소문자가 있으면,
                    key_dict[str(graph[i][j])]=str(graph[i][j]).upper()
                    graph[i][j]="*"
        else:
            for j in [0,w-1]:
                if graph[i][j]=="*": # 가장자리가 벽이면
                    continue
                elif graph[i][j]==".": #가장자리가 빈칸이면
                    continue
                elif graph[i][j]=="$": #가장자리가 문서면
                    file+=1
                    graph[i][j]="*"
                elif str(graph[i][j]) in alphabet_list_lower: #가장자리에 소문자가 있으면,
                    key_dict[str(graph[i][j])]=str(graph[i][j]).upper()
                    graph[i][j]="*"
    

    for i in range(h):
        if i==0 or i==h-1:
            for j in range(w):
                if graph[i][j]!="*": 
                    bfs(i,j)
        else:
            for j in [0,w-1]:
                if graph[i][j]!="*":
                    bfs(i,j)
    print(file)
    """