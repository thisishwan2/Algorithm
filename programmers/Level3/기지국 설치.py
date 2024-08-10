# 그리디로 풀기
def solution(n, stations, w):
    lst = []

    start = 1
    for i in stations:
        lst.append(i - w + -start)
        start = i + w + 1

    if start <= n:
        lst.append(n - start + 1)

    answer = 0
    for i in lst:
        if i % (2 * w + 1) == 0:
            answer += i // (2 * w + 1)
        else:
            answer += i // (2 * w + 1) + 1

    return answer


def solution(n, stations, w):
    answer = 0
    std = w * 2 + 1
    start = 1
    for s in stations:
        if s - w - start > 0:
            answer += (s - w - start) // std
            if (s - w - start) % std: answer += 1
        start = s + w + 1
    if n - start + 1 > 0:
        answer += (n - start + 1) // std
        if (n - start + 1) % std: answer += 1
    return answer