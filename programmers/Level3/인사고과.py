def solution(scores):
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b

    # 인센티브를 받지 못하는 사원을 찾아서 없앤다.
    # 첫번째 요소를 내림차순, 두번째 요소를 오름차순으로 정렬한 경우 i의 두번째 요소보다 i+1의 두번째 요소가 작다면 그 사원은 인센티브를 받지 못한다.
    # 따라서 max_b를 정하고, 그 max_b보다 작은 b가 존재하면 그 사원은 인센티브를 받지 못한다.
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxb = 0

    for a, b in scores:
        if target_a < a and target_b < b:
            return -1

        # 따라서 max_b보다 크거나 같은 b에 대해서 총 점수가 원호보다 크면 rank가 높은것.
        if b >= maxb:
            maxb = b
            if a + b > target_score:
                answer += 1

    return answer + 1