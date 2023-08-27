import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int, input().split())

lst=[]
for _ in range(n):
    lst.append(list(map(int, input().split())))

visited=[[0 for _ in range(m)]for _ in range(n)]
maxres = 0

def dfs(x,y,sum,cnt):
    global maxres

    if cnt==4:
        maxres=max(maxres, sum)
        return
     
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            visited[nx][ny]=1
            dfs(nx,ny,sum+lst[nx][ny],cnt+1)
            visited[nx][ny]=0
     
def another(x,y):
    global maxres
    for i in range(4):
        tmp = lst[x][y]
        for j in range(3):
            t=(i+j)%4
            nx=x+dx[t]
            ny=y+dy[t]

            if not (0<=nx<n and 0<=ny<m):
                tmp=0
                break
            tmp+=lst[nx][ny]
        maxres=max(maxres, tmp)

for i in range(n):
    for j in range(m):
        visited[i][j]=1
        dfs(i,j,lst[i][j],1)
        visited[i][j]=0
        another(i,j)

print(maxres)