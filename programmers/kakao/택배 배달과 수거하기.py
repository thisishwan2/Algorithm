# 다시 풀어보기
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    answer = 0
    delivery_cnt = 0
    pickup_cnt = 0

    for i in range(n):
        delivery_cnt += deliveries[i]
        pickup_cnt += pickups[i]

        # 만약 둘 중 하나가 양수라면, 아직 i번째 지점을 방문해야 한다.
        while delivery_cnt > 0 or pickup_cnt > 0:
            # 여기서 cap만큼 빼주는데, 추후에 해당 부분의 음수값만큼 다른 지점을 들려서 배달 혹은 수거할 수 있음.
            delivery_cnt -= cap
            pickup_cnt -= cap
            answer += (n - i) * 2

    return answer