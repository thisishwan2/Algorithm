# 치킨거리는 집과 가장 가까운 치킨집 사이의 거리
# r1-r2 + c1-c2임
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합

# 0 은 빈집, 1은 집 2는 치킨집
# 도시의 치킨 거리가 가장 작게 구하는 프로그램

#2시부터 시작

import sys
input=sys.stdin.readline

n,m=map(int, input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

#치킨집 좌표를 구한다.
chicken=[]
home=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append([i,j])
        elif graph[i][j]==1:
            home.append([i,j])

def back():
    if len(tmp)== m :
        situation.append(list(tuple(tmp)))
        return

    for i in chicken:
        if len(tmp)==0:
            tmp.append(list(tuple(i)))
            back()
            tmp.pop()
        elif len(tmp)!= 0:
            if chicken.index(i)>chicken.index(list(tmp[-1])):
                tmp.append(list(tuple(i)))
                back()
                tmp.pop()

tmp=[]
situation=[]
back()

ans=[]

for i in situation:
    sumation=0
    for j in home:
        minimum = 1000000000
        for k in range(len(i)):
            minimum=min(minimum, abs(j[0]-i[k][0])+abs(j[1]-i[k][1]))

        sumation+=minimum
    ans.append(sumation)

print(min(ans))




