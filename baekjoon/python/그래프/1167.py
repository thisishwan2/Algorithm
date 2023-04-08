#1167
#bfs
# 아무 한 노드에서 제일 먼 노드를 찾고, 그 노드에서 젤 먼 노드를 찾음.
import sys
input=sys.stdin.readline
from collections import deque
v=int(input())
graph=[[]for _ in range(v+1)]

for _ in range(v):
    a=list(map(int,input().split()))
    a.pop(-1)
    for i in range(1,len(a),2):
        graph[a[0]].append([a[i],a[i+1]])

def bfs(x):
    q=deque()
    q.append(x)
    visited=[-1]*(v+1)
    visited[x]=0

    while q:
        x=q.popleft()
        for i in graph[x]:
            if visited[i[0]]==-1:
                q.append(i[0])
                visited[i[0]]=visited[x]+i[1]
    return visited.index(max(visited)), max(visited)

idx,distance=bfs(1)
res_idx, res_distance=bfs(idx)
print(res_distance)