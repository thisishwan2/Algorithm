def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        position = i - 1
        for j in range(len(board)):
            if board[j][position] != 0:
                stack.append(board[j][position])
                board[j][position] = 0
                break

        # print("==")
        # print(stack)
        # print("==")

        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer