import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

r,c=map(int, input().split())

graph=[]
for _ in range(r):
    graph.append(list(input().rstrip()))

def back(x,y,count):
    global ans
    ans = max(ans, count)


    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in alpha:
            alpha.add(graph[nx][ny])
            back(nx,ny,count+1)
            alpha.remove(graph[nx][ny])

alpha = set()
alpha.add(graph[0][0])
ans=0

back(0,0,1)
print(ans)