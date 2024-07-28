def solution(n):
    answer = 0
    dp = [0] * 5001
    n//=2
    dp[1] = 3
    dp[2] = 11

    for i in range(3, n+1):
        dp[i] = (dp[i-1]*4-dp[i-2])

    return dp[n] % 1000000007
print(solution(8))
print(solution(10))