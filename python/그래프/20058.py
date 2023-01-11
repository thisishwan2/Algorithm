#20058 마법사 상어와 파이어스톰
#배열의 회전과 bfs를 이용

import sys
input=sys.stdin.readline
import copy
from collections import deque


#구역을 나눠 90도 돌리는 함수
def turn(level):
    new_graph=copy.deepcopy(graph)
    split_len=(2**level) # 격자 한면 길이

    #배열 돌리기 알고리즘
    #간격은 격자 한명의 길이 만큼 
    for y in range(0, graph_len, split_len):
        for x in range(0, graph_len, split_len):
            for i in range(split_len):
                for j in range(split_len):
                    #여기가 핵심
                    new_graph[y+j][x+split_len-i-1]=graph[y+i][x+j]
    return new_graph

#녹이는 과정
def melting():
    new_graph=copy.deepcopy(graph)

    q=deque()
    q.append([0,0])
    visit[0][0]=1

    while q:
        cnt=0
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<graph_len and 0<=ny<graph_len:
                if visit[nx][ny]==0:
                    visit[nx][ny]=1
                    q.append([nx,ny])
                if graph[nx][ny]>=1:
                    cnt+=1
        if cnt<3 and graph[x][y]>=1:
            new_graph[x][y]=graph[x][y]-1
    
    return new_graph

#덩어리 갯수 세는 과정
def area(x,y):
    
    q2=deque()
    q2.append([x,y])
    visited[x][y]=1
    areas=1

    while q2:
        x,y=q2.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<graph_len and 0<=ny<graph_len:
                if visited[nx][ny]==0 and graph[nx][ny]!=0:
                    areas+=1
                    q2.append([nx,ny])
                    visited[nx][ny]=1
    areas_cnt.append(areas)

#n: 격자의 제곱수, q: 파이어 스톰 시전횟수
n,q=map(int, input().split())

graph=[]
for _ in range(2**n):
    graph.append(list(map(int, input().split())))

#그래프의 한면 길이
graph_len=2**n
#단계를 넣을 리스트
l=list(map(int,input().split()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#l에 있는 단계를 하나씩 시행
for L in l:
    graph=turn(L)
    #돌린 그래프 방문처리 리스트
    visit=[[0 for _ in range(graph_len)] for _ in range(graph_len)]
    graph=melting()


areas_cnt=[]
total=0
visited=[[0 for _ in range(graph_len)] for _ in range(graph_len)]
for i in range(graph_len):
    for j in range(graph_len):
        
        total+=graph[i][j]
        if visited[i][j]==0 and graph[i][j]!=0:
            area(i,j)

print(total)
print(max(areas_cnt) if len(areas_cnt)!=0 else 0)