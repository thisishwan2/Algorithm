#2512

import sys
input=sys.stdin.readline

n=int(input())
money=list(map(int,input().split()))
m=int(input())

def bs(start, end, moeny):
    while start<=end:
        mid=(start+end)//2

        total = 0
        for i in moeny:
            #만약 mid값보다 크면, mid를 더함
            if i>=mid:
                total+=mid
            # 그외 money 자체값을 더함
            else:
                total+=i

        # total이 예산보다 크면
        if total>m:
            end=mid-1
        # total이 예산보다 작거나 같으면
        else:
            start=mid+1
    return end


if sum(money)<=m:
    print(max(money))
else:
    ans=bs(1,max(money),money)
    print(ans)

