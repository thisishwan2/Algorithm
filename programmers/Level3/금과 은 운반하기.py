def solution(a, b, g, s, w, t):
    answer = -1

    # 최악의 경우
    # 광물의 최대무게 : 10**9 * 2(금,은)
    # 도시가 1개만 있고 소요시간이 최대(10**5), 옮길 수 있는 W가 1일때 : 10**5 * 2(왕복)
    start = 0
    end = (10 ** 9) * (10 ** 5) * 4

    while start <= end:
        mid = (start + end) // 2  # 시간
        gold = 0
        silver = 0
        total = 0

        for now_gold, now_silver, now_weight, now_time in zip(g, s, w, t):

            # 주어진 시간안에 이동할 수 있는 횟수
            move_cnt = mid // (now_time * 2)  # 왕복

            # 편도도 추가
            if mid % (now_time * 2) >= now_time:  # 편도 시간보다 나머지가 크면, 한번 더 이동할 수 있음(편도)
                move_cnt += 1

            # 주어진 시간 내 최대 적재 가능량 누적하기
            possible_weight = move_cnt * now_weight

            # gold 적재 가능량 확인
            if now_gold < possible_weight:
                gold += now_gold
            else:  # gold가 최대 적재 가능량보다 크면, 적재 가능량을 더하기
                gold += possible_weight

            # sliver 적재 가능량 확인
            if now_silver < possible_weight:
                silver += now_silver
            else:
                silver += possible_weight

            # 총합 적재 가능량 확인
            if (now_gold + now_silver) < possible_weight:
                total += now_gold + now_silver
            else:
                total += possible_weight

        # 만약 특정 시간동안 모든 도시를 고려해서 gold와 silver의 옮기는 양이 a+b보다 크고, gold가 a보다 크고, silver가 b보다 크면
        # 이미 과하게 옮기고 있는것이므로 시간을 줄여준다.
        if total >= a + b and gold >= a and silver >= b:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer
