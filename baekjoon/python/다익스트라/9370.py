import sys
input=sys.stdin.readline
import heapq

t=int(input())

def djikstra(start):
    hq=[]
    heapq.heappush(hq,[0, start])
    distance=[sys.maxsize for _ in range(n+1)]
    distance[start]=0

    while hq:
        dist, x = heapq.heappop(hq)
        
        for next,n_distance in graph[x]:
            n_dist=n_distance+dist

            if distance[next]>n_dist:
                heapq.heappush(hq, [n_dist,next])
                distance[next]=n_dist
    return distance

for _ in range(t):
    n,m,t = map(int, input().split()) #교차로 도록 목적지후보 갯수
    s,g,h = map(int, input().split()) #예술가 출발지, 예술가들이 지나고 있는 교차로 사이 길

    graph=[[]for _ in range(n+1)]
    target=[]
    result=[]

    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])
    
    for _ in range(t):
        target.append(int(input()))

    first= djikstra(s)
    g_ = djikstra(g)
    h_ = djikstra(h)

    ans=[]

    for i in target:
        if first[h]+h_[g]+g_[i]==first[i] or first[g]+g_[h]+h_[i]==first[i]:
            ans.append(i)
    ans.sort()
    print(*ans)