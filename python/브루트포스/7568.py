#자기보다 크고 무거운(둘 다 큰) 사람이 몇 명인지 쟤서 자기 등수만 정하면 된다. n명을 n-1번씩 전수 비교해보면 된다.
import sys

n=int(sys.stdin.readline())

lst=[]


for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    lst.append([x,y])

for i in lst:
    rank=1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1   #현재 본인이 몇등인지를 정할 수 있다.
    print(rank, end = " ")