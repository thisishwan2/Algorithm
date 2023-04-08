#bfs 풀이법(bottom-up)
import sys
from collections import deque

input = sys.stdin.readline


def solution(a, b):
    #큐에 a랑 cnt를 넣어준다.(cnt초기값 1)
    q = deque([(a, 1)])
    #큐가 빌때 까지
    while q:
        #큐에 있는 a,cnt 를 꺼낸다
        a, cnt = q.popleft()
        if a == b:
            print(cnt)
            return

        #새로운 (노드)를 생성, 문제에서는 아래와 같이 곱하기 2 혹은 뒷자리에 1 붙히는 것만 있음.
        if a * 2 <= b:
            q.append((a * 2, cnt + 1))
        if a * 10 + 1 <= b:
            q.append((a * 10 + 1, cnt + 1))
    #큐가 빌때까지 돌면 답이 없는것이므로 -1출력
    print(-1)


a, b = map(int, input().split())
solution(a, b)

#나의풀이(top-down)
import sys

a,b=map(int, sys.stdin.readline().split())

cnt=1
while b!=a:
    cnt+=1
    temp=b
    if(b%2==0):
        b=b//2
    elif(b%10==1):
        b=b//10


    if temp == b:
        print(-1)
        break
else:
    print(cnt)