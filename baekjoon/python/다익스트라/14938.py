# 지역의 갯수만큼 1에서 부터 n까지 다익스트라를 실행한다.
# distance에 다음 위치까지의 가중치(거리)를 넣어서 반환해줌
# 함수 이후 distance의 가중치가 수색범위 m 이내일 경우 해당 아이템을 특정변수(cnt)에 더해준다.
# 그렇게 max 값을 출력한다.


import sys
input=sys.stdin.readline
import heapq

n,m,r = map(int,input().split()) #지역의 갯수, 수색범우, 길의 개수
items=list(map(int, input().split()))
graph =[[]for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int, input().split())
    graph[a].append([b,l])
    graph[b].append([a,l])


def dijkstr(x):
    hq=[]
    heapq.heappush(hq, [0,x])
    distance=[sys.maxsize]*(n+1)
    distance[x]=0

    while hq:
        dist, x = heapq.heappop(hq)
        for i in graph[x]:
            if distance[i[0]]>dist+i[1]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(hq, [dist+i[1],i[0]])

    return distance
res=0
for i in range(1,n+1):
    ans = dijkstr(i)
    cnt=0

    for d in range(1,n+1):
        if m>= ans[d]:
            cnt+=items[d-1]
    
    res=max(res,cnt)
    

print(res)


#플로이드 위샬로 푸는 법
INF = int(1e9)

N, M, R = map(int, input().split())
area_item = list(map(int, input().split()))
arr = [[INF] * N for _ in range(N)]

for _ in range(R):
    start, end, dist = map(int, input().split())
    arr[start-1][end-1] = min(arr[start-1][end-1], dist)
    arr[end-1][start-1] = min(arr[end-1][start-1], dist)

#특정노드로 가는 법은 a->b 랑 a->k->b 중 더 작은 가중치가 들어가면 된다.
#(= 다익스트라 distance 결정되는 로직과 비슷함
for k in range(N):
    for a in range(N):
        for b in range(N):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
            if a == b:
                arr[a][b] = 0

max_value = 0

# max 값 구해주기.
for i in range(N):
    temp_value = 0
    for j in range(N):
        if arr[i][j] <= M:
            temp_value += area_item[j]

    max_value = max(max_value, temp_value)

print(max_value)



#_____________________________________

# 최대힙으로 풀어보자.
# import sys
# input=sys.stdin.readline
# import heapq

# n,m,r = map(int,input().split()) #지역의 갯수, 수색범우, 길의 개수
# items=list(map(int, input().split()))
# graph =[[]for _ in range(n+1)]
# for _ in range(r):
#     a,b,l = map(int, input().split())
#     graph[a].append([b,l])
#     graph[b].append([a,l])


# def dijkstr(x):
#     distance = [0]*(n+1)
#     hq=[]
#     heapq.heappush(hq, [-items[x-1],x,0]) #아이템, 위치, 수색범위
#     distance[x]=-items[x-1]
#     cnt=-items[x-1]

#     while hq:
#         item, x, susaek =heapq.heappop(hq)

#         for i in graph[x]:
#             next=i[0]
#             road=i[1]
#             if susaek+road<=m:
#                 if distance[next]> item-items[next-1]:
#                     heapq.heappush(hq, [(item-items[next-1]),next,susaek+road])
#                     if distance[next]!=0:
#                         cnt=cnt-items[next-1]+distance[next]
#                     else:
#                         cnt-=items[next-1]
#                     distance[next]=item-items[next-1]
                    
#     return cnt

# maximum=0

# for i in range(1,n+1):
#     maximum = min(dijkstr(i), maximum)
# print(-maximum)