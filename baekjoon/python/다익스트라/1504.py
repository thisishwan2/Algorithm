#1504
#임의로 주어진 두 정점은 반드시 통과해야함.
# 이 문제의 핵심은 최단 경로의! 길이! 즉, 길이가 짧은게 아니라 과정이 빠른것이라고 생각했는데 아니었다.
# 이문제는 결국 경로가 가장 짧은것을 구하는것이다. 단 v1,v2를 거치면서 경로가 짧아야한다,
# 띠라서 1->v1->v2->n 1->v2->v1->n의 경우만 고려하면 된다.

import sys
input=sys.stdin.readline
import heapq

n, e = map(int, input().split())

graph = [[]for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int, input().split()) # 반드시 통과해야하는 두 정점

def dijkstr(x):
    distance=[sys.maxsize]*(n+1)
    hq=[]
    heapq.heappush(hq,[0,x]) #거리

    distance[x]=0

    while hq:
        dist,x=heapq.heappop(hq)

        for i in graph[x]:
            next=i[0]
            cost=i[1]

            if dist+cost<distance[next]:
                distance[next]=dist+cost
                heapq.heappush(hq,[dist+cost,next])
        
    return distance


origin = dijkstr(1)
v1_dist = dijkstr(v1)
v2_dist = dijkstr(v2)

ans = min(origin[v1]+v1_dist[v2]+v2_dist[n], origin[v2]+v2_dist[v1]+v1_dist[n])
print(ans if ans <sys.maxsize else -1)