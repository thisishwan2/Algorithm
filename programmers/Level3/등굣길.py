def solution(m, n, puddles):
    answer = 0

    dp = [[0 for _ in range(m + 1)] for _ in range(n)]

    dp = [[0] * (m + 1)] + dp
    dp[1][1] = 1

    for x, y in puddles:
        dp[y][x] = -1
    # print(dp)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue

            if dp[i][j] != -1:
                if dp[i - 1][j] != -1 and dp[i][j - 1] != -1:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
                elif dp[i - 1][j] == -1:
                    dp[i][j] = dp[i][j - 1]
                elif dp[i][j - 1] == -1:
                    dp[i][j] = dp[i - 1][j]

    # print(dp)
    return dp[n][m]