#1719


INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
tmp=[[j for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c
    
for i in range(1,n+1):
    graph[i][i]=0
    tmp[i][i]="-"
   
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j]>graph[i][k]+graph[k][j]:
                graph[i][j]=graph[i][k]+graph[k][j]
                tmp[i][j]=tmp[i][k] #???

for i in range(1,n+1):
    for j in range(1,n+1):
        print(tmp[i][j],end=" ")
    print()

"""

import sys
input=sys.stdin.readline
import heapq

n,m=map(int, input().split())

graph=[[]for _ in range(n+1)]
for _ in range(m):
    num1, num2, time = map(int, input().split())
    graph[num1].append([num2,time])
    graph[num2].append([num1,time])

def dijkstra(start, end):
    hq=[]
    heapq.heappush(hq, [0,start,0, 0])# cost, position, first 집하장
    distance=[sys.maxsize]*(n+1)
    distance[start]=0
    

    while hq:
        cost, start,cnt, node = heapq.heappop(hq)
        if start==end:
            return node
        for i in graph[start]:
            next=i[0]
            dist=i[1]

            if distance[next]>dist+cost:
                if cnt==0:
                    heapq.heappush(hq,[dist+cost, next, cnt+1, next])
                    distance[next]=dist+cost
                else:
                    heapq.heappush(hq,[dist+cost, next, cnt+1, node])
                    distance[next]=dist+cost
            

ans=""

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            ans+="- "
        else:
            res= dijkstra(i,j)
            ans+=str(res)+" "
    ans+="\n"

print(ans.rstrip())
"""