#11052

n=int(input())
cardpack=[0]+list(map(int, input().split()))
dp=[0]*(n+1)

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i], dp[i-j]+cardpack[j]) #dp[i-j]: i-j개의 카드를 구매할때 최대 가격, cardpack[j]: j개 카드 가격 (i-j)+(j)=i
print(dp)