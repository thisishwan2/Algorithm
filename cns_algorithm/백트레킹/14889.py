import sys
input=sys.stdin.readline

n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

total=0
for i in range(n):
    for j in range(n):
        total+=graph[i][j]

# 두 리스트 간의 차이 계산
def cal(tmp):
    sumation=0
    for i in range(len(tmp)):
        for j in range(i+1, len(tmp)):
            x=tmp[i]
            y=tmp[j]
            sumation+=graph[x][y]+graph[y][x]
    return sumation


def back():
    if len(tmp)==n//2:
        one=cal(tmp)
        two=cal([x for x in candi if x not in tmp])

        ans.append(abs(one-two))
        return

    for i in range(n):
        if (len(tmp)==0):
            tmp.append(i)
            back()
            tmp.pop()

        elif ((i not in tmp) and (i>tmp[-1])):
            tmp.append(i)
            back()
            tmp.pop()

tmp=[]
candi=[]
ans=[]
for i in range(n):
    candi.append(i)
back()
print(min(ans))