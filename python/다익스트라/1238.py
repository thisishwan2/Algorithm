import sys
input=sys.stdin.readline
import heapq

n,m,x = map(int, input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,t=map(int, input().split())
    graph[a].append([b,t])

def djikstra_start(start):
    distance=[sys.maxsize]*(n+1)
    hq=[]
    heapq.heappush(hq, [0,start])
    distance[start]=0

    while hq:
        dist, start = heapq.heappop(hq)

        if start==x:
            return dist

        for i in graph[start]:
            next=i[0]
            cost=i[1]

            if distance[next]>cost+dist:
                heapq.heappush(hq, [cost+dist,next])
                distance[next]=cost+dist

def djikstra_end(start,end):
    distance=[sys.maxsize]*(n+1)
    hq=[]
    heapq.heappush(hq, [0,start])
    distance[start]=0

    while hq:
        dist, start = heapq.heappop(hq)

        if start==end:
            return dist

        for i in graph[start]:
            next=i[0]
            cost=i[1]

            if distance[next]>cost+dist:
                heapq.heappush(hq, [cost+dist,next])
                distance[next]=cost+dist

ans=[]

for i in range(1,n+1):
    res1=djikstra_start(i)
    res2=djikstra_end(x,i)

    ans.append(res1+res2)

print(max(ans))