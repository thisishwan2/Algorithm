#10282

import sys
input=sys.stdin.readline
import heapq

def dijkstra(x):
    hq=[]
    heapq.heappush(hq, [0,x]) #time, position
    distance[x]=0

    while hq:
        time, x = heapq.heappop(hq)

        for i in graph[x]:
            next=i[0]
            cost=i[1]

            if distance[next]>time+cost:
                heapq.heappush(hq,[time+cost, next])
                distance[next]=time+cost
  

    return distance

t=int(input())
for _ in range(t):
    n,d,c=map(int, input().split()) #컴퓨터 갯수, 의존성 갯수, 해킹당한 컴퓨터 번호
    distance=[sys.maxsize]*(n+1)
    graph=[[]for _ in range(n+1)]
    for i in range(d):
        a,b,s = map(int, input().split()) #a가b를 의존, b 감염 후 s초 후 a도 감염
        graph[b].append([a,s])
    
    cnt=0
    res = dijkstra(c)
    ans=0

    for i in res:
        if i!=sys.maxsize:
            cnt+=1
            ans=max(ans, i)
            
    print(f"{cnt} {ans}")
    
