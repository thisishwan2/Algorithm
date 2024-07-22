def solution(line):
    INF = float('inf')
    maxx, minx, maxy, miny = -INF, INF, -INF, INF
    coordinate = []
    l = len(line)

    for i in range(l):
        for j in range(i + 1, l):
            A, B, E, C, D, F = *line[i], *line[j]
            bunmo = A * D - B * C
            if bunmo == 0:
                continue
            x, y = (B * F - E * D) / bunmo, (E * C - A * F) / bunmo
            # 정수임을 판별
            if (float(int(x)) != x or float(int(y)) != y):
                continue

            x, y = int(x), int(y)
            maxx, minx, maxy, miny = max(maxx, x), min(minx, x), max(maxy, y), min(miny, y)
            coordinate.append((x, y))
    board = [["." for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for x, y in coordinate:
        board[maxy - y][x - minx] = "*"

    ans = []
    for i in range(maxy - miny + 1):
        line = ""
        for j in range(maxx - minx + 1):
            line += board[i][j]
        ans.append(line)
    return ans