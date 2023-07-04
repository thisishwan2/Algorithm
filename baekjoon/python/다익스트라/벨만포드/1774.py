#1774

import sys
input=sys.stdin.readline

def bell_ford(start):

    # 시작 노드에 대해 초기화
    distance[start]=0

    # 전체의 n번 라운드 반복
    for i in range(n):
        #모든 간선확인
        for j in range(m):
            now, next, cost = graph[j]
            if distance[now]!=inf and distance[now]+cost<distance[next]:
                distance[next]=distance[now]+cost

                # n번째 라운드에서도 값이 갱신되면 음수 순환이 존재.
                if i==n-1:
                    return True
    return False

n,m=map(int,input().split())
inf = int(1e9) # 무한대 값
distance=[inf]*(n+1)
graph=[]

for i in range(m):
    a,b,c=map(int, input().split())
    graph.append((a,b,c))
            
# 벨만 포드 알고리즘 수행
negative_cycle = bell_ford(1)

# 음수 순환이 존재하면 -1 출력
if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1 출력
        if distance[i] == inf:
            print("-1")
        # 도달할 수 있으면 거리 출력
        else:
            print(distance[i])