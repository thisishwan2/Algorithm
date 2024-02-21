def solution(n, lost, reserve):
    tmp = []

    lost = sorted(lost)
    reserve = sorted(reserve)

    for i in lost:
        if i in reserve:
            reserve.remove(i)
            tmp.append(i)

    for i in tmp:
        lost.remove(i)

    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)

    answer = n - len(lost)

    return answer

solution(5,[4,5],[3,5])