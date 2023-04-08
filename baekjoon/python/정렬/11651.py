import sys

n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    xi,yi=map(int, sys.stdin.readline().split(" "))
    lst.append([yi,xi])

lst.sort()
for i in range(n):

    print(lst[i][1], lst[i][0])
#람다 이용
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[1], x[0])) #1번인덱스를 정렬하고 0번 인덱스 정렬
for i in so:
    print(i[0], i[1])