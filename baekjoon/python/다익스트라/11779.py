#11779

import heapq
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[]for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])

start, end = map(int, input().split())

distance=[sys.maxsize]*(n+1)
node = [0]*(n+1) # 이번 문제의 핵심인 이전 노드를 넣어주는 리스트이다. ex) 이번에 next가 5인데, 현재 노드가 3이면 node[5]=3을 해줌,
#이렇게 하는 이유는 end 포인트에서 역추적을 할 수 있기 때문이다. 역추적을 하면 당연히 최적의 경로가 나옴.
#왜냐면 다익스트라의 특징인 최단 거리로 방문하는것을 생각하면, 이미 방문처리가 된곳은 최단거리로 온 곳임.

def dijkstra(start, end):
    hq=[]
    distance[start]=1
    heapq.heappush(hq, [0,start]) #cost, start, 방문 노드

    while hq:
        dist, x = heapq.heappop(hq)
        if x==end:
            return dist
        
        for i in graph[x]:
            next=i[0]
            cost=i[1]

            if distance[next]>=dist+cost:
                distance[next]=dist+cost
                heapq.heappush(hq, [dist+cost, next])
                node[next]=x


total_cost = print(dijkstra(start, end))

road=[end]
now=end

while now!=start:
    now = node[now]
    road.append(now)
road.reverse()

print(len(road))
print(" ".join(map(str, road)))
