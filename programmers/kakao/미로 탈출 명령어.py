import sys

sys.setrecursionlimit(5000)

# d,l,r,u 순
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
answer = ""


def get_dist(x1, y1, x2, y2):
    return abs(y1 - y2) + abs(x1 - x2)


def dfs(n, m, x, y, r, c, k, st):  # k: 남은 이동 가능 거리
    global visited
    global answer

    remain_dist = get_dist(x, y, r, c)

    # 남은 이동 거리가 0이고, 도착지에 도달한 경우
    if (x, y) == (r, c) and k == 0:
        answer = st
        return

    # 남은 이동 거리 - 도착지까지의 거리 가 의미하는 것은 현재위치를 도착지라고 가정하는 것과 같다.
    # 즉, 현재 도착지일때, 남은 이동거리가 짝수가 아니면, 다시 도착지로 못돌아온다는 의미
    # 또한, 남은 이동 거리 보다 도착지까지의 거리가 더 크면, 그건 도착지로 가지 못한다는 의미
    if (k - remain_dist) % 2 != 0 or (k - remain_dist) < 0:
        answer = "impossible"
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        remain_dist = get_dist(r, c, nx, ny)

        # 다음 위치가 범위안에 있고,
        # 다음위치로 이동했을때, 남은 이동 거리가 도착지까지의 거리보다 크고
        # 다음위치로 이동했을때, 남은 이동거리 - 도착지까지 거리가 짝수여야 도착지에 갈 수 있고,
        # 이전 알파벳이 해당 위치를 먼저 방문한적이 없는 경우
        if 0 <= nx < n and 0 <= ny < m and k - 1 >= remain_dist and (k - 1 - remain_dist) % 2 == 0 and \
                visited[k - 1][nx][ny] == 0:
            if i == 0:
                dfs(n, m, nx, ny, r, c, k - 1, st + "d")
                return
            elif i == 1:
                dfs(n, m, nx, ny, r, c, k - 1, st + "l")
                return
            elif i == 2:
                dfs(n, m, nx, ny, r, c, k - 1, st + "r")
                return
            elif i == 3:
                dfs(n, m, nx, ny, r, c, k - 1, st + "u")
                return


def solution(n, m, x, y, r, c, k):
    global visited
    x = x - 1
    y = y - 1
    r = r - 1
    c = c - 1
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
    dfs(n, m, x, y, r, c, k, "")
    print(answer)

    return answer
# solution(3,	4,	2,	3,	3,	1,	5)
# solution(2,	2,	1,	1,	2,	2,	2)
# solution(3,	3,	1,	2,	3,	3,	4)