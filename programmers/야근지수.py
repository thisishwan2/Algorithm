def solution(n, works):
    answer = 0

    # 일이 야근하는 시간보다 적은 경우엔 일을 다 마치므로 피로도가 없음
    if sum(works) <= n:
        return 0

    dics = {}
    for work in works:
        if work in dics:
            dics[work] += 1
        else:
            dics[work] = 1

    while n > 0:
        max_val = max(dics.keys())
        if dics[max_val] <= n:
            if max_val - 1 in dics:
                dics[max_val - 1] += dics[max_val]
            else:
                dics[max_val - 1] = dics[max_val]

            n = n - dics[max_val]
            dics.pop(max_val, None)  # None 이 없으면 dics에 정보가 없을시 에러발생
        else:
            if max_val - 1 in dics:
                dics[max_val - 1] += n
            else:
                dics[max_val - 1] = n

            dics[max_val] = dics[max_val] - n
            n = 0

    for key in dics.keys():
        answer += key * key * dics[key]

    return answer