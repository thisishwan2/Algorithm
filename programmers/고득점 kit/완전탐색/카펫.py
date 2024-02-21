# 본 문제의 핵심은 주어진 타일의 개수를 통해 사각형의 넓이를 구할떄 필요한 가로,세로 의 경우의 수를 구해서
# 해당 경우의 수를 하나씩 돌아가면서 brown, yellow 에 수에 맞는 답을 찾는 방식
def solution(brown, yellow):
    answer = []

    total = brown + yellow
    mid = int(total ** (1 / 2))

    tmp = []

    for i in range(3, mid + 1):
        if (total % i == 0):
            tmp.append([total // i, i])

    for i in tmp:
        garo = i[0]
        sero = i[1]

        if ((sero - 2) * (garo - 2) == yellow):
            answer.append(garo)
            answer.append(sero)

    return answer