def solution(triangle):
    # dp 배열을 삼각형의 크기로 초기화
    dp = [[0] * len(row) for row in triangle]

    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):  # 행
        for j in range(len(triangle[i])):
            if j == 0:  # 맨 왼쪽 원소
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:  # 맨 오른쪽 원소
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:  # 중간에 있는 원소
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    # 마지막 행에서 최댓값 반환
    return max(dp[-1])
