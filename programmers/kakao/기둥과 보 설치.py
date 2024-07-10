# 이 문제의 중요한점은 설치하거나 삭제할때 모두 조건에 맞는지를 파악하면 쉽다.
# 그리고, 같은 x,y 좌표에 기둥과 보 하나만 올 수 있는줄 알았는데, 둘다 올 수도 있는것을 마지막 정렬 조건을 통해 알 수 있다.(함정)

def can_construct(x, y, a, structures):
    if a == 0:  # 기둥
        if y == 0:  # 바닥에 설치하는 경우
            return True
        if (x, y - 1, 0) in structures:  # 밑에 기둥이 있거나
            return True
        if (x - 1, y, 1) in structures:  # 기둥 왼쪽에 보가 있거나
            return True
        if (x, y, 1) in structures:  # 기둥 오른쪽에 보가 있거나
            return True

    else:  # 보
        if (x, y - 1, 0) in structures:  # 보의 왼쪽 끝 아래에 기둥이 있거나
            return True
        if (x + 1, y - 1, 0) in structures:  # 보의 오른쪽 아래에 기둥이 있거나
            return True
        if (x - 1, y, 1) in structures and (x + 1, y, 1) in structures:  # 보의 양쪽이 연결되어 있거나
            return True


def solution(n, build_frame):
    structures = set()

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            structures.add((x, y, a))
            if not can_construct(x, y, a, structures):
                structures.remove((x, y, a))
        else:  # 삭제
            structures.remove((x, y, a))

            # 위에서 구조물을 삭제한 경우에 for문에서 단 하나의 경우라도 False가 나오면 조건에 부합하기 때문에 다시 set에 해당 구조물을 넣어준다.
            if not all(can_construct(nx, ny, na, structures) for nx, ny, na in list(structures)):
                structures.add((x, y, a))

    answer = sorted(structures, key=lambda struct: (struct[0], struct[1], struct[2]))
    return answer