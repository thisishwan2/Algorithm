# 대기실은 5개 (5*5 크기)
# 응시자들은 맨허튼 거리로 2이하로 앉으면 안됨
# 응시자 자리 사이가 파티션으로 막히면 ㄱㅊ

# p는 응시자가 앉은 자리, o는 빈 테이블, x는 파티션

# 응시자가 앉은 자리간의 맨허튼 거리가 1 이면 항상 거리두기 조건 불 충족
# 만약 맨허튼 거리가 2이면 파티션의 여부를 파악해야함

def solution(places):
    answer = []

    for place in places:
        sit_place = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    sit_place.append([i, j])

        flag = False

        for i in range(len(sit_place)):
            for j in range(i + 1, len(sit_place)):
                p1 = sit_place[i]
                p2 = sit_place[j]

                # 두 사람 사이의 거리가 1이라면 거리두기를 지키지 않은 것이다.
                if (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) == 1:
                    flag = True
                    break

                # 두 사람 사이의 거리가 2이라면 파티션의 여부를 파악한다.
                elif (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) == 2:

                    # 두사람이 직선상에 위치한다면, 중간에 파티션이 있으면 ok
                    if p1[0] == p2[0]:
                        if place[p1[0]][(p1[1] + p2[1])//2] == "X":
                            continue
                    elif p1[1] == p2[1]:
                        if place[(p1[0] + p2[0])//2][p1[1]] == "X":
                            continue

                    # 두사람이 대각선 상에 존재한다면, 양 옆에 위치한 부분에 파티션이 존재하면 ok
                    elif place[p1[0]][p2[1]] == "X" and place[p2[0]][p1[1]] == "X":
                            continue

                    # 만약 ok가 아니면 거리두기를 지키지 않은것
                    flag = True
                    break

                # 두사람이 거리가 2이상이면 ok
                elif (abs(p1[0] - p2[0]) + abs(p2[0] - p2[1])) > 2:
                    continue

            if flag == True:
                break

        if flag == True:
            answer.append(0)
        else:
            answer.append(1)

    return answer
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


'''
이런 풀이도 가능

from collections import deque

def check(place, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x, y, 0])
    visited = set()
    visited.add(tuple([x, y]))
    while queue:
        a, b, c = queue.popleft()
        if c == 2:
            continue
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx <= len(place)-1 and ny >= 0 and ny <= len(place[0])-1:
                if tuple([nx, ny]) not in visited:
                    visited.add(tuple([nx, ny]))
                    if place[nx][ny] == 'P':
                        return False
                    if place[nx][ny] == 'X':
                        continue
                    queue.append([nx, ny, c+1])

    return True


def solution(places):
    answer = []

    for place in places:
        people = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P':
                    people.append([i, j])

        flag = True
        for x, y in people:
            if not check(place, x, y):
                flag = False
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)


    return answer



'''