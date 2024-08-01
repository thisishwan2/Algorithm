from collections import deque

# 상상, 상하, 상좌, 상우, 하상, 하하, 하좌, 하우, 좌상, 좌하, 좌좌, 좌우, 우상, 우하, 우좌, 우우
move = [[-1, 0, -1, 0], [-1, 0, 1, 0], [-1, 0, 0, -1], [-1, 0, 0, 1], [1, 0, -1, 0], [1, 0, 1, 0], [1, 0, 0, -1],
        [1, 0, 0, 1], [0, -1, -1, 0], [0, -1, 1, 0], [0, -1, 0, -1], [0, -1, 0, 1], [0, 1, -1, 0], [0, 1, 1, 0],
        [0, 1, 0, -1], [0, 1, 0, 1]]


def solution(maze):
    answer = 0

    n, m = len(maze), len(maze[0])
    r_sx, r_sy, r_tx, r_ty = 0, 0, 0, 0  # 빨간 수레 시작 칸, 도착 칸
    b_sx, b_sy, b_tx, b_ty = 0, 0, 0, 0  # 파란 수레 시작 칸, 도착 칸

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                r_sx = i
                r_sy = j
            elif maze[i][j] == 2:
                b_sx = i
                b_sy = j
            elif maze[i][j] == 3:
                r_tx = i
                r_ty = j
            elif maze[i][j] == 4:
                b_tx = i
                b_ty = j

    # print(r_sx, r_sy, r_tx, r_ty,b_sx, b_sy, b_tx, b_ty)

    q = deque()
    q.append([r_sx, r_sy, b_sx, b_sy, 0, set(), set()])

    while q:
        rx, ry, bx, by, cnt, visited_r, visited_b = q.popleft()
        print(rx, ry, bx, by, cnt, visited_r, visited_b)

        # 먼저 add 한 뒤 copy하면 add 한게 반영이 된다
        n_visited_r = visited_r.copy()
        n_visited_b = visited_b.copy()
        n_visited_r.add((rx, ry))
        n_visited_b.add((bx, by))

        if (rx, ry) == (r_tx, r_ty) and (bx, by) == (b_tx, b_ty):
            print(cnt)
            return cnt

        r_flag = False
        b_flag = False

        for drx, dry, dbx, dby in move:
            # 도착지에 도착한 수례를 파악해서 위치를 조정해야함
            if (rx, ry) == (r_tx, r_ty) and (bx, by) != (b_tx, b_ty):
                r_flag = True
                nrx = rx
                nry = ry
                nbx = bx + dbx
                nby = by + dby
            elif (rx, ry) != (r_tx, r_ty) and (bx, by) == (b_tx, b_ty):
                b_flag = True
                nrx = rx + drx
                nry = ry + dry
                nbx = bx
                nby = by
            elif (rx, ry) != (r_tx, r_ty) and (bx, by) != (b_tx, b_ty):
                nrx = rx + drx
                nry = ry + dry
                nbx = bx + dbx
                nby = by + dby

            # 범위 안이고, 벽이 아니어야 한다.
            if (0 <= nrx < n and 0 <= nry < m and 0 <= nbx < n and 0 <= nby < m) and (
                    maze[nrx][nry] != 5 and maze[nbx][nby] != 5):
                # 이미 한 수례가 도착지에 방문하면 방문 조건에서 걸리기 때문에, flag를 이용해서 or 연산을 하고, 만약 방문하지 않았다면 다음 조건을 확인
                if (r_flag or (nrx, nry) not in n_visited_r) and (b_flag or (nbx, nby) not in n_visited_b):
                    # 같은 칸을 방문하지 않아야한다. 수례의 위치는 서로 바꿀 수 없다.
                    if (nrx, nry) != (nbx, nby) and not ((rx, ry) == (nbx, nby) and (bx, by) == (nrx, nry)):
                        # q.append([nrx,nry,nbx,nby,cnt+1,visited_r.add((nrx, nry)),visited_b.add((nbx, nby))])
                        q.append([nrx, nry, nbx, nby, cnt + 1, n_visited_r, n_visited_b])
        # print("=================")
        # print(q)
        # print("=================")

    return 0


solution([[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]])