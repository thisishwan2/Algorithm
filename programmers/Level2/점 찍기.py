import math


def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        # 피타고라스 정리 이용
        # x값이 i일때, y값의 최대값을 구한뒤, y값을 k로 나누면 x일때 찍을 수 있는 갯수가 나온다.
        max_y = int(math.sqrt(d ** 2 - i ** 2))
        # print(max_y, i) # 4,0/2,0/0,0  # 2,2/0,2 # 0,4
        answer += (max_y // k) + 1  # +1은 y가 0인 경우를 더해준다.

    return answer