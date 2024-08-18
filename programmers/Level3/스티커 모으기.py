# 15, 14 ,6, 20 와 같은 경우를 고려해야함
def solution(sticker):
    answer = 0
    n = len(sticker)

    # 길이가 1인 테스트 케이스
    if n == 1:
        return sticker[-1]

    # 첫번째 스티커를 떼는 경우
    dp_first = [0] * (n - 1)
    first = sticker[:n - 1]
    dp_first[0] = first[0]
    for i in range(1, n - 1):
        if i == 1:
            dp_first[i] = max(first[i], dp_first[i - 1])
        else:
            dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + first[i])

    # 두번째 스티커를 떼는 경우
    dp_sec = [0] * (n - 1)
    second = sticker[1:]
    dp_sec[0] = second[0]
    for i in range(1, n - 1):
        if i == 1:
            dp_sec[i] = max(second[i], dp_sec[i - 1])
        else:
            dp_sec[i] = max(dp_sec[i - 1], dp_sec[i - 2] + second[i])

    # print(dp_first)
    # print(dp_sec)
    answer = max(dp_first[-1], dp_sec[-1])
    return answer