def solution(command):
    sx, sy = 0, 0
    dir = 0
    forward = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    backward = {0: [0, -1], 1: [-1, 0], 2: [0, 1], 3: [1, 0]}

    # 방향: 상우하좌

    for i in command:
        if i == "R":
            dir = (dir + 1) % 4
        elif i == "L":
            if (dir - 1) < 0:
                dir = 3
            else:
                dir = dir - 1
        elif i == "G":
            sx = sx + forward[dir][0]
            sy = sy + forward[dir][1]
        elif i == "B":
            sx = sx + backward[dir][0]
            sy = sy + backward[dir][1]
    answer = [sx, sy]

    return answer