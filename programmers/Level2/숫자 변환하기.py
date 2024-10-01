from collections import deque


def solution(x, y, n):
    q = deque()
    q.append([x, 0])
    visited = [0] * (y + 1)
    visited[x] = 1

    while q:
        num, cnt = q.popleft()

        if num == y:
            return cnt

        for i in range(3):  # in (num + n, num * 2, num * 3): 이렇게 풀어도 됨(in 스킬)
            if i == 0:
                n_num = num + n
            elif i == 1:
                n_num = num * 2
            elif i == 2:
                n_num = num * 3

            if n_num <= y and visited[n_num] == 0:
                q.append([n_num, cnt + 1])
                visited[n_num] = 1

    return -1