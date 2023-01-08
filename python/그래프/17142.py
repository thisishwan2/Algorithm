#17142
#문제의 핵심은 비활성화된 바이러스는 0으로 인식이 가능하다.
#즉, 통과할 수 있다.
#또한 동시에 1로도 인식해서 감염시킬 필요가 없다.
#따라서 빈칸이고 방문안했으면 감염시키고, 비활성바이러스인데 방문안했으면 지나만 가고 감염x 

import sys
input=sys.stdin.readline
from collections import deque
import itertools

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs():
    time=0
    cnt=0 #감연된 구역 수
    
    while q:
        if cnt==zero: #빈칸의 수와 감염된 구역 수가 같을때
            return time
        for _ in range(len(q)):
            x,y= q.popleft()
            visit[x][y]=1
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    #다음이 빈칸이고, 방문하지 않았을때
                    if graph[nx][ny]==0 and visit[nx][ny]==0:
                        q.append([nx,ny])
                        visit[nx][ny]=1
                        cnt+=1 #감염시킴
                    elif graph[nx][ny]==2 and visit[nx][ny]==0:
                        q.append([nx,ny])
                        visit[nx][ny]=1

        time+=1
    return -1


two=[]
zero=0 #빈칸 개수
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            two.append([i,j])

        if graph[i][j]==0:
            zero+=1

result=[]
combis=itertools.combinations(two,m)
for combi in combis:
    visit=[[0 for _ in range(n)]for _ in range(n)]
    global cnt
    
    q=deque(combi)
    res = bfs()
    if res!=-1:
        result.append(res)

        
    
if len(result)==0:
    print(-1)
else:
    print(min(result))