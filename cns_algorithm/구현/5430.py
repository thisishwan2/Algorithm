import sys
input=sys.stdin.readline
from collections import deque


# R은 배열의 순서를 뒤집고, D는 첫번째 수를 버린다.

t=int(input())

for _ in range(t):
    p=input().rstrip()
    n=int(input())
    arr = input().rstrip()[1:-1].split(",")
    q=deque(arr)

    rev, front, back = 0, 0, len(q) - 1
    flag = 0

    if n == 0:
        q = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(q) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag==0:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")


