#13549

#원래 이 문제는 단순한 BFS를 요구하는 문제가 아닙니다. 왜냐하면, BFS를 하기 위해서는 모든 간선의 가중치가 동일해야 한다는 전제 조건이 필요하기 때문입니다. 
# 이 문제는 가중치가 0인 간선이 있기 때문에 일반적으로는 단순한 BFS를 쓸 수 없으나, 문제의 특성 때문에 방문 순서에 따라서 단순 BFS로도 우연히도 항상 정답을 찾을 수 있을 뿐입니다. 
# 왜 하필 이 순서로 하면 항상 정답이 나오는가를 증명하는 건 매우 복잡한 일입니다.
#이 문제를 보다 일반화된 경우 (가중치가 0인 간선이 있는 경우)에 대해 해결하려면, 즉, 이 문제의 의도대로 풀려면 다음과 같은 방법들을 사용할 수 있습니다.

#다익스트라 알고리즘
#0-1 BFS: 가중치가 0인 간선에 연결된 정점은 큐의 맨 뒤가 아닌 맨 앞에 넣는 방법
#* 2를 별도의 간선으로 생각하지 않고, +1이나 -1에 의한 좌표를 큐에 넣을 때 그 좌표의 2의 거듭제곱 배인 좌표들을 전부 큐에 넣는 방법

#다익스트라
import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
INF = 1e9

# dijkstra 함수
def dijkstra(N,K):
    dist = [INF]*(100001)
    dist[N] =0 
    hq = []
    heapq.heappush(hq,(0,N))
    while hq:
        #거리, 위치
        w,n = heapq.heappop(hq)
        #(위치와 가중치(거리)))
        for nx in [(n+1,1),(n-1,1),(n*2,0)]:
            if 0<=nx[0]<100001 and dist[nx[0]] > w + nx[1]:
                dist[nx[0]] = w + nx[1]
                #가중치가 작은게 앞으로감.
                heapq.heappush(hq,(dist[nx[0]],nx[0]))
    print(dist[K])
dijkstra(N,K)

#0-1 BFS
# import sys
# input = sys.stdin.readline
# from collections import deque

# n, k =map(int, input().split())

# visit=[0]*(100001)

# def bfs(n):
#     if n==k:
#         return 0
#     q=deque()
#     q.append([n,0])
#     visit[n]=1

#     while q:
#         x, time=q.popleft()
#         if x==k:
#             return time

#         for i in [x*2, x+1, x-1]:
#             if 0<=i<=100000 and visit[i]==0:
#                 visit[i]=1
#                 if i==x*2:
#                     #다른 연산보다 곱하기 2가 우선순위를 가져야 한다. (순간이동은 가중치가 0, 다른 움직임은 1)
#                     q.appendleft([i,time])
#                 else:
#                     q.append([i,time+1])

# print(bfs(n))
