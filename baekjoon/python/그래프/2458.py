import sys

#입력
n, m = map(int, input().split())
height = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    short, tall = map(int, sys.stdin.readline().split())
    height[short-1][tall-1]=1

#플로이드 와샬 알고리즘(한 정점에서 모든 정점으로의 연결 상태를 알아냄.)
for k in range(n): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(n):
        for j in range(n):
            if height[i][k] ==1 and height[k][j] == 1:
                height[i][j] = 1 

#출력
answer = 0
for i in range(n):
    check = 0
    for j in range(n):
        check += height[i][j] + height[j][i] #자신보다 작은사람 + 큰사람
    if check == n-1: #자신의 키 순서를 알 경우(자신제외 이므로 n-1)
        answer += 1
print(answer)