import copy


# 90도 회전
def turn_90(key):
    n = len(key)
    new_arr = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            new_arr[y][n - 1 - x] = key[x][y]

    return new_arr


def solution(key, lock):
    m = len(key)
    n = len(lock)

    unlock_cnt = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                unlock_cnt += 1
    print(unlock_cnt)
    # lock 주위를 0으로 확장
    extend_size = n + 2 * (m - 1)
    extended_lock = [[0] * extend_size for _ in range(extend_size)]

    # 원래의 lock 데이터를 중앙에 배치
    for i in range(n):
        for j in range(n):
            extended_lock[i + m - 1][j + m - 1] = lock[i][j]

    for _ in range(4):
        key = turn_90(key)
        # 모든 위치에서 시도
        for x in range(extend_size - m + 1):
            for y in range(extend_size - m + 1):

                tmp = copy.deepcopy(extended_lock)

                # key를 적용해보기
                valid = True # valid는 key의 돌기와 lock의 돌기가 만나면 안되기 때문에 만들어둔 변수
                for i in range(m):
                    for j in range(m):
                        nx, ny = x + i, y + j
                        if key[i][j] == 1 and tmp[nx][ny] == 1: # 돌기가 겹치는 경우
                            valid = False
                        if key[i][j] == 1 and tmp[nx][ny] == 0: # 키의 돌기와 락의 홈이 겹치는 경우
                            tmp[nx][ny] = 1

                # 확장함 배열에서 lock부분에 빈 흠이 없는지 확인
                cnt=0
                for i in range(m-1, m + n - 1):
                    for j in range(m-1, m + n - 1):
                        if tmp[i][j] == 1:
                            cnt+=1

                if cnt == n*n and valid:
                    return True

    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])


