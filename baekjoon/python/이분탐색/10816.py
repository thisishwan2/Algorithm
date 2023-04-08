import sys
input=sys.stdin.readline

#딕셔너리를 이용한 풀이
n=int(input())
cards=sorted(list(map(int,input().split())))
m=int(input())
target=list(map(int,input().split()))

#각 숫자의 카운트 값을 넣는 딕셔너리
dic={}
for card in cards:
    if card in dic:
        dic[card]+=1
    else:
        dic[card]=1

# 이분 탐색
def bs(start,end,cards,target):
    while start<=end:
        mid=(start+end)//2

        if cards[mid]==target:
            return dic.get(target)
        elif cards[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

for i in target:
    print(bs(0,n-1,cards,i), end=" ")


# upper bound & lower bound
#lower는 해당 수가 처음 나오는 위치이고, upper는 해당수 다음 수가 처음 나오는 위치이다.
n=int(input())
card=list(map(int,input().split()))
m=int(input())
target=list(map(int,input().split()))

card.sort()

#lower bound 찾기
def lower(start,end,target,card):
    while start<end:
        mid=(start+end)//2

        # 타켓 값이 카드의 값보다 큰 경우에는 start는 mid에 1을 더한 값이다.
        if target>card[mid]:
            start=mid+1
        # 타겟 값이 카드의 값보다 작거나 같은 경우에는 end는 mid 값과 같다.
        else:
            end=mid
    return end

def upper(start,end,target,card):
    while start<end:
        mid=(start+end)//2

        # 타겟 값이 카드의 값보다 같거나 큰 경우에는 start는 mid+1이다.
        if target>=card[mid]:
            start=mid+1
        else:
            end=mid
    return end

ans=[]
for i in target:
    low=lower(0,n,i,card)
    up=upper(0,n,i,card)
    ans.append(up-low)
print(*ans)