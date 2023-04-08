#시간초과 너무 어렵게 생각햇다
import sys

n=int(sys.stdin.readline())
i=2
routemin=2
routemax=7
while True:
    if routemax>=n and n>=routemin:
        print(i)
        break
    routemin+=6*i
    i+=1
    routemax+=6*i

#정답 (벌집의 개수가 6의 배수로 증가하기 때문)
import sys

n=int(sys.stdin.readline())

cnt=1
start=1 #벌집개수 1부터
while n>start:
    start+=cnt*6
    cnt+=1
print(cnt)
