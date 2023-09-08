
# 시간초과 풀이

# import heapq
# def solution(n, roads, sources, destination):
#     answer = []
#     count=0
#     for i in sources:
#         count+=1
#         # 시작점 i, 끝점 destination 인 최단 경로
#         hq=[]
#         heapq.heappush(hq, [0,i])
#         visited=[1e9 for j in range(n+1)]
#         visited[i]=0
#         while hq:
#             dist, x = heapq.heappop(hq)
#             if x==destination:
#                 answer.append(dist)
#                 break
            
#             for j in roads:
#                 a=j[0]
#                 b=j[1]
                
#                 next=0
#                 if a!=x and b==x:
#                     next=a
#                 elif a==x and b!=x:
#                     next=b
                    
#                 if next!=0:
#                     if visited[next]>visited[x]+1:
#                         heapq.heappush(hq, [dist+1, next])
#                         visited[next]=visited[x]+1
#         if len(answer)!=count:
#             answer.append(-1)
#     return answer

from collections import deque

def solution(n, roads, sources, destination):
    # roads를 원하는 2차원 배열로 재배치
    graph=[[] for _ in range(n+1)]
    
    for x,y in roads:
        graph[x].append(y)
        graph[y].append(x)
    
    # destination으로 부터 각 지점까지의 최소 거리를 구하기
    visited=[-1 for i in range(n+1)]
    visited[destination]=0
    q=deque()
    q.append(destination)
    
    while q:
        x = q.popleft()
        
        for next in graph[x]:
            if visited[next]==-1:
                visited[next]=visited[x]+1
                q.append(next)
    
    # sources에 있는 값만 answer로 넣기
    answer = []
    for i in sources:
        answer.append(visited[i])
    
    return answer

print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1,3,5], 5))