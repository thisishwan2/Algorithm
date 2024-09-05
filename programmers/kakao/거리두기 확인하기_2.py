from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(places):
    answer = []

    for place in places:
        # 특정 응시자를 기준으로 맨하튼 거리가 2이내의 모든 지점을 확인.(3칸)
        # 단 이때, 둘 사이에 파티션을 고려한다.
        # 파티션을 두 좌표가 평행하면 사이에 있는지 확인하고,
        # 대각선상이면 각 대각선에 파티션이 있는지 확인한다.

        flag = True  # 모두 거리두기를 잘 지킨다는 플레그
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    q = deque()
                    q.append([i, j, 1])
                    visited = [[0 for _ in range(5)] for _ in range(5)]
                    visited[i][j] = 1

                    while q:
                        x, y, cnt = q.popleft()

                        if cnt == 3:
                            if place[x][y] == "P":
                                # 만약 x,y의 좌표도 P라면, 사이에 파티션으로 놓였는지 확인
                                # 평행한 경우라면
                                if i == x:
                                    if place[i][(j + y) // 2] != "X":
                                        flag = False
                                        break
                                elif j == y:
                                    if place[(i + x) // 2][y] != "X":
                                        flag = False
                                        break

                                # 대각선의 경우라면
                                else:
                                    if place[i][y] != "X" or place[x][j] != "X":
                                        flag = False
                                        break
                            continue
                        # 바로 옆칸이 사람이면, 무조건 탈락
                        elif cnt == 2 and place[x][y] == "P":
                            flag = False
                            break

                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]

                            if 0 <= nx < 5 and 0 <= ny < 5:
                                if visited[nx][ny] == 0 and cnt<3:
                                    q.append([nx, ny, cnt + 1])
                                    visited[nx][ny] = 1
                    if flag == False:
                        break
                if flag == False:
                    break
            if flag == False:
                break
        if flag == False:
            answer.append(0)
        else:
            answer.append(1)
    print(answer)


solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])