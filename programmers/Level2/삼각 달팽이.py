def solution(n):
    num = 1
    plus = 2
    for i in range(1, n):
        num += plus
        plus += 1

    arr = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    dir = {0: [1, 0], 1: [0, 1], 2: [-1, -1]}  # 하, 우, 좌측 대각
    direction = 0
    for i in range(1, num + 1):
        arr[x][y] = i

        nx = x + dir[direction][0]
        ny = y + dir[direction][1]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            direction = (direction + 1) % 3
            nx = x + dir[direction][0]
            ny = y + dir[direction][1]
            x = nx
            y = ny

    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
    return answer