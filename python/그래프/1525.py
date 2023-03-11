import sys
input=sys.stdin.readline
from collections import deque
from copy import deepcopy

ans=set()

graph=""
for i in range(3):
    a="".join(map(str, input().split()))
    graph+=a

start=graph.index("0")

d1=[3,-3,1,-1]
d0=[3,-3,1]
d2=[3,-3,-1]


def bfs(x,graph):
    q=deque()
    q.append([x,graph,0])
    ans.add(graph)

    while q:
        x,graph, cnt=q.popleft()
        if graph=="123456780":
            return cnt

        orgin_graph=deepcopy(graph)

        if x%3==0:
            ran=len(d0)
            dx=d0
        elif x%3==1:
            ran=len(d1)
            dx=d1
        elif x%3==2:
            ran=len(d2)
            dx=d2

        for i in range(ran):
            nx=x+dx[i]        
            if 0<=nx<9:
                graph=list(graph)
                str1=graph[x]
                str2=graph[nx]

                graph[nx], graph[x] = str1, str2
                graph="".join(graph)
                if graph not in ans:
                    q.append([nx,graph,cnt+1])
                    ans.add(graph)
                graph=deepcopy(orgin_graph)
    return -1

print(bfs(start,graph))