#1446
# 지름길은 일방통행이고, 고속 도로는 역주행 불가능

import sys
input=sys.stdin.readline
import heapq

n,d=map(int, input().split()) #지름길 개수, 고속도로 길이

#출발노드 start, 도착 노드 end, 따라서 출발노드 인덱스의 값으로[end, dist]를 넣음

graph=[[] for _ in range(d+1)]

#지름길을 제외하고, 기본적으로 거리는 1이다.
for i in range(d):
    graph[i].append([i+1,1])
# 도착 위치를 넘는 도착 노드는 추가할 필요 없음.
for i in range(n):
    start, end, dist = map(int, input().split())
    if end>d: continue
    graph[start].append([end,dist])

#거리를 담을 distance 생성
INF=sys.maxsize
distance=[INF]*(d+1)
distance[0]=0

def djikstra(dist,x):
    hq =[]
    heapq.heappush(hq,[dist,x])

    while hq:
        dist, x = heapq.heappop(hq)
                
        # 특정 출발 노드에서 갈 수 있는 도착 노드와 거리를 꺼낼것임.
        for i in graph[x]:
            cost=dist+i[1] #도착 노드까지의 거리

            #도착 노드의 거리가 도착 노드의 기존 거리보다 작다면
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(hq, [cost,i[0] ])

djikstra(0,0)

print(distance[d])