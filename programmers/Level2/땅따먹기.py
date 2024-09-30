def solution(land):
    #     answer = 0

    #     dp = [[0 for _ in range(4)]for _ in range(len(land))]
    #     for _ in range(4):
    #         dp[0][_] = land[0][_]

    #     for i in range(1,len(land)):
    #         for j in range(4):
    #             for next in range(4):
    #                 if next!=j:
    #                     dp[i][next] = max(dp[i][next], dp[i-1][j]+land[i][next])

    #     return max(dp[-1])

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[len(land) - 1])
