import sys
input=sys.stdin.readline
import heapq


n=int(input().rstrip()) #도시의 수
m=int(input().rstrip()) #버스의 수

graph=[[] for _ in range(n+1)]



for i in range(m):
    #버스의 출발도시, 도착지 도시, 비용
    info = list(map(int, input().split()))
    graph[info[0]].append(info[1:])

# 까먹지 말기
INF=1e10
distance=[INF]*(n+1)

start, end = map(int, input().split())

def dijkstra(start, end):
    hq=[]
    heapq.heappush(hq,[0, start]) #(비용, 시작점)
    distance[start]=0

    while hq:
        cost, start = heapq.heappop(hq) 

        # 최초로 나온 값이 최소 비용
        if start== end:
            return cost
        
        # 힙큐에서 뽑은 거리(cost)가 이미 갱신된 거리보다 클 경우(이미 방문을 한셈)
        if distance[start]<cost:
            continue

        # 현재 위치와 연결된 노드를 정보를 i에 담음
        for i in graph[start]:
            cost=distance[start]+i[1] #인접 노드 도착시 비용

            if cost<distance[i[0]]: #만약 인접 노드시 도착비용이 distance[인접노드] 보다 작으면
                distance[i[0]]=cost
                heapq.heappush(hq,[cost, i[0]])

print(dijkstra(start, end))


