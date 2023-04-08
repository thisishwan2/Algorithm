#1535(재귀를 이용한 풀이 시간 648ms)

def knapsack(capacity, n):
    if capacity==0 or n==0:
        return 0
    if damage_hp[n-1]>capacity:
        return knapsack(capacity, n-1)
    else:
        return max(happy[n-1]+knapsack(capacity-damage_hp[n-1], n-1), knapsack(capacity, n-1))


import sys
n=int(sys.stdin.readline())

damage_hp=list(map(int, sys.stdin.readline().rstrip().split()))
happy=list(map(int, sys.stdin.readline().rstrip().split()))


print(knapsack(99, len(damage_hp)))


#dp를 이용한 풀이(Bottom-Up)(68ms)(이중리스트를 엄청 큰 크기로 만들어서 오래걸릴줄 알았는데 아니었다.)
#문제에서 체력이 0이되면 안된다고 했으니, 최대 허용 체력은 99이다.
def knapsack(W, wt, val, n): #W: 체력 한도, wt: 각 체력 사용량, val:기쁨, n:기쁨의 수
    #2차원 리스트 생성
    #최대 체력은 99이므로 range (100)=0~99
    k=[[0 for _ in range(100)] for _ in range(n+1)]

    #위의 이중 for문가 같은 크기의 for문
    for i in range(n+1):
        for w in range(W+1):
            #0번째 행 ,열 은 0이 들어가야한다.
            if i==0 or w==0:
                k[i][w]=0
            #wt의 0번째 인덱스가 0~99 크기보다 작으 경우에만
            elif wt[i-1]<=w:
                #더 큰값을 선택
                k[i][w]=max(val[i-1]+k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                #i번째의 체력을 뺀 것들로 최적값을 구함.
                k[i][w]=k[i-1][w]
    return k[n][W]

n=int(input())
wt=list(map(int, input().split()))
val=list(map(int, input().split()))

print(knapsack(99, wt, val, n))

#조금더 간력한 DP풀이
import sys

n = int(sys.stdin.readline())
#미리 행과 열에 0을 넣어준다.
stamina_consum = [0] + list(map(int, sys.stdin.readline().split()))
get_pleasure = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * 100 for _ in range(n + 1)]
#1부터 진행해서 행과 열의 0번째는 다 0으로 되어 있다.
for i in range(1, n + 1):#n까지
    for j in range(1, 100):#99까지
        
        if stamina_consum[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - stamina_consum[i]] + get_pleasure[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])