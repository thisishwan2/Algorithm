# 3초 제한에 nlogn 복잡도 인데, 초과나는것이 이해가 안가지만
# 최소한의 시간을 쓸 수 있도록 하자
# 
import sys
input=sys.stdin.readline
w,n = map(int, input().split())

jewel=[list(map(int, input().split()))for _ in range(n)]
jewel=sorted(jewel, key = lambda x:x[1], reverse=True)
price=0

for mj,pi in jewel:
    if w>mj:
        price+=mj*pi
        w-=mj
    else:
        price+=w*pi
        break
print(price)