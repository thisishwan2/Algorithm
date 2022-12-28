#12851

import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())
visit=[0]*100001
dx=[-1,1,2]


def bfs(x,times):
    q=deque()
    q.append([x,times])
    visit[x]=1
    cnt=0
    res=[]

    while q:
        x,times=q.popleft()
        if x==k:
            res.append(times)
            cnt+=1
            continue

        for i in (x-1,x+1,2*x):
            nx=i
            if 0<=nx<=100000:
                if visit[nx]==0 or visit[nx]==visit[x]+1: #뒷조건을 생각하지를 못했음..
                    q.append([nx,times+1])
                    visit[nx]=visit[x]+1
    return (min(res), cnt)
a=bfs(n,0)
print(a[0])
print(a[1])