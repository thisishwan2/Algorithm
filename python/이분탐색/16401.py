import sys
input = sys.stdin.readline
M, N = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()
st = 1
ed = snack[-1]
while st <= ed:
    mid = (st+ed)//2
    cnt = 0
    for i in snack:
        cnt += i//mid
    if cnt >= M:
        st = mid+1
    else:
        ed = mid-1
print(ed)

#16401

import sys
input=sys.stdin.readline

m,n=map(int,input().split())

snack=list(map(int, input().split()))

def bs(start, end):
    while start<=end:
        cnt=0
        mid=(start+end)//2

        for i in snack:
            cnt+=(i//mid)

        if cnt<m:
            end=mid-1
        
        elif cnt>=m:
            start=mid+1

    return end

print(bs(1,max(snack)))