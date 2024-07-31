# 시전시간 t초 동안 붕대를 감으면서 1초마다 x만큼 체력이 회복되고, 시전시간 전체동안 붕대 감기 성공 = y만큼 추가 회복
# 붕대 감는중 공격당하면 붕대 감기 취소, 붕대 감기 취소 당하거나, 기술이 끝나면 다시 붕대감기를 0초부터 시작
# 공격 받으면 피해량 만큼 체력 감소, 0이하시 -1 리턴
# 남은 체력을 리턴

def solution(bandage, health, attacks):
    time = 0  # 시간
    sequence = 0  # 연속 성공 횟수
    real_heart = health  # 실제 현재 체력
    # real_heart += health

    for i in attacks:
        attack_time = i[0]  # 공격 시간
        attack_damage = i[1]  # 공격 피해량
        print(real_heart)
        if real_heart <= 0:
            return -1

        while True:
            time += 1

            # 공격이면
            if time == attack_time:
                sequence = 0
                real_heart -= attack_damage
                break

            # 공격 아닌 경우
            else:
                sequence += 1
                # 연속 성공이 최대인 경우
                if sequence == bandage[0]:
                    sequence = 0  # 연속 성공 초기화
                    # 회복량 회복하고 추가 회복량도 회복할건데, 최대 체력을 넘지 않는 선에서 회복할것이다.
                    real_heart = min(health, real_heart + bandage[1] + bandage[2])


                # 연속 성공이 최대가 아닌 경우
                elif sequence != bandage[0]:
                    # 회복량 회복할건데, 최대 체력을 넘지 않는 선에서 회복할것이다.
                    real_heart = min(health, real_heart + bandage[1])

    if real_heart <= 0:
        return -1
    return real_heart


solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])


# 다른 풀이
# 붕대감기: t초동안 붕대를 감고, 1초마다 x만큼 회복한다.
# t초 연속 붕대감기에 성공시, y만큼의 체력을 추가회복
# 최대 체력 이상이 되는 것은 불가능

# 붕대감기 기술 사용중 공격당하면, 기술이 취소된다.
# 공격을 당하는 순간에는 체력을 회복할 수 없다.
# 공격으로 취소당하면, 다시 붕대감기를 하고 연속 성공시간이 0으로 초기화된다
# 공격받으면 피해량만큼 체력이 줄고, 0이하가 되면 죽는다.


# bandage: 붕대담기 시전 시간, 1초당 회복량, 추가 회복량/ health: 최대 체력/ attacks: 몬스터 공격 시간, 피해량
def solution(bandage, health, attacks):
    # 붕대감기 연속 시전 시간, 초당 회복량, 추가 회복량
    heal_time, heal_amount, add_heal_amount = bandage[0], bandage[1], bandage[2]
    # 최대 체력
    max_heart = health

    # 공격 종료시간
    end_time = attacks[-1][0]

    # 배열[공격 시간] = 피해량 형태로 변경
    attack_list = [0] * (1001)
    for t, d in attacks:
        attack_list[t] = d

    time = 0  # 시간
    seq_success = 0  # 연속 성공
    while time < end_time:
        time += 1

        if attack_list[time] == 0:  # 몬스터 공격이 없는 경우
            # 연속 성공 한 경우에는 기존에 초당회복량+추가 회복량을 해준다.
            if seq_success + 1 == heal_time:
                health = health + heal_amount + add_heal_amount

                if health > max_heart:
                    health = max_heart
                seq_success = 0
            # 연속 성공은 아닌경우
            else:
                seq_success += 1
                health = health + heal_amount

                if health > max_heart:
                    health = max_heart

        else:  # 공격이 있는 경우
            # 공격당해서 체력인 0이하가 되는 경우
            if health - attack_list[time] <= 0:
                return -1
            else:
                health -= attack_list[time]
                seq_success = 0

        # print(health)

    return health

# solution([3, 2, 7],	20,	[[1, 15], [5, 16], [8, 6]])