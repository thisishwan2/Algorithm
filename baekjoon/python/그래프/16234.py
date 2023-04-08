#16234
#생긱버디 구현에 애를 먹었음.
#문제 풀이법
#우선 국경선을 여는 조건을 수행시킬 BFS를 만든다. temp 리스트를 생성해서 국경성 공유하는 나라의 좌표값을 저장한다.
#인구이동을 수행하기 위해, 국경선이 열려있다면 flag를 1로 바꿔 인구 이동 시작을 표시한다. 그리고 연합의 인구수/연합을 이루는 칸의 개수를 해주고, 국경을 공유하는(temp)나라에 인구수를 넣어준다.
#인구 이동이 일어날때마다 res값을 1씩 증가해준다.
#이를 다 수행했으면(국경이 더이상열리지 않으면) flag를 0으로 바꾸고 while문을 break.


import sys
input=sys.stdin.readline
from collections import deque

#N*N: 땅의 크기, L: 인구차 이상, R: 인구차 이하
N,L,R=map(int,input().split())

maps=[]
for _ in range(N):
    maps.append(list(map(int, input().split())))
    
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#국경공유 찾기
def bfs(x,y):
    q=deque()
    #temp 리스트에 국경 공유되는 좌표를 넣는다.
    temp=[]
    q.append([x,y])
    temp.append([x,y])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if L<=abs(maps[nx][ny]-maps[x][y])<=R:
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp

#인구이동 수행되는 날수
res=0

while True:
    visited=[[0]*(N+1) for _ in range(N+1)]
    #국경선이 열린것을 알려줄 변수 설정
    flag=0

    #이중 for문으로 모든 위치의 경우를 다 확인한다.
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j]=1
                #국경선이 열린 temp좌표를 country에 대입
                country= bfs(i,j)
                
                #만약 한번이라도 열렸다면
                if len(country)>1:
                    #국경선이 열림을 표시하고
                    flag=1
                    #연합인구수/연합 칸수
                    number=sum([maps[a][b] for a,b in country]) // len(country)
                    #연합 각 좌표에 인원수 재배정
                    for x,y in country:
                        maps[x][y] = number
    
    #국경선이 열리지 않으면 초기값 0그대로
    if flag==0:
        break

    #한번의 while문마다 하루가 지난다.
    res+=1
print(res)