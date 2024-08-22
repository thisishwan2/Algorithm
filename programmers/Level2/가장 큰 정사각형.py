def solution(board):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = [[0 for _ in range(m)] for _ in range(n)]

    if (n, m) == (1, 1) and board[0][0] == 1:
        answer = 1

    # 첫행, 첫열 설정
    for i in range(m):
        dp[0][i] = board[0][i]

    for i in range(n):
        dp[i][0] = board[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
            answer = max(answer, dp[i][j])

    return answer * answer