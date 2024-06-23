import math

def solution(w, h):
    # 최대 공약수
    gcd = math.gcd(w, h)

    # 최대 공약수로 나눈만큼이 하나의 작은 규칙 크기임
    w_small = w / gcd
    h_small = h / gcd

    small_cnt = w_small + h_small - 1

    return w * h - small_cnt * gcd