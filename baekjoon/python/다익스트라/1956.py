#1956

#다익스트라
import sys
input=sys.stdin.readline
import heapq


v,e=map(int, input().split())

hq=[]
dist=[[1e9 for _ in range(v+1)]for _ in range(v+1)]
graph=[[]for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])
    dist[a][b]=c
    heapq.heappush(hq, [c,a,b])


while hq:
    c,a,b=heapq.heappop(hq)

    if a==b:
        print(c)
        break

    for i in graph[b]:
        y=i[0]
        cost=i[1]

        # a->y(다음 노드) 보다 a->중간->y(다음 노드)가 더 비용이 적은 경우
        if cost+c<dist[a][y]:
            dist[a][y]=c+cost
            heapq.heappush(hq, [c+cost,a,y])
else:
    print(-1)

#폴로위드 워샬

'''
import sys
input=sys.stdin.readline

v,e=map(int,input().split())

graph=[[1e9 for _ in range(v+1)]for _ in range(v+1)]

for _ in range(e):
    a,b,c=map(int, input().split())

    graph[a][b]=c


for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

ans=1e9
for i in range(1,v):
    ans=min(ans, graph[i][i])

if ans == 1e9 :
    print(-1)
else :
    print(ans)
    '''