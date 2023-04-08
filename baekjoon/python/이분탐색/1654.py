#1654

# 성원 n개의 랜선 필요, 영식 k개의 랜선 보유(길이 제각각)
# 성원은 n개 모두 같은 길이를 원함.
# 따라서 k개의 랜선을 잘라서 만들어야함. ex) 300cm ->140,140(20 버림)

import sys
input=sys.stdin.readline
# k: 갖고 있는 랜선 수, N: 필요한 랜선 수(target)
k,n=map(int, input().split())

lan=[]

for _ in range(k):
    lan.append(int(input()))

def bs(start, end):
    while start<=end:
        lan_cnt=0
        mid=(start+end)//2
        # 생성되는 랜선의 갯수 파악
        for i in lan:
            lan_cnt+=i//mid

        # 랜선 갯수가 타겟보다 많거나 같은 경우
        #참고로 같은경우는 더 긴 길이중에 랜선갯수와 타겟수가 맞는 경우도 있을수 있으므로, start=mid+1 해줘도 된다.
        if lan_cnt>=n:
            ans.append(mid)
            start=mid+1 #갯수를 줄이기 위해 길이를 늘린다.
        # 랜선 갯수가 타겟보다 적은 경우
        else:
            end=mid-1 # 길이를 줄인다.

cnt=0
ans=[]
bs(1, max(lan))

print(max(ans))

