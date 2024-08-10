# 2일땐 2가지 (1+1)
# 3일땐 3가지
# 4일땐 5가지
# 5일땐 8가지
# 6일땐 12가지
# 7일땐 15가지

def solution(n):
    answer = 0

    dp = [0] * 60001

    dp[2] = 2
    dp[3] = 3

    num = 4
    while num <= n:
        dp[num] = (dp[num - 1] + dp[num - 2]) % 1000000007
        num += 1

    answer = dp[n]

    return answer