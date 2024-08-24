def solution(picks, minerals):
    # minerals를 5개씩 나눈다.
    mineral_list = []
    for i in range(0, len(minerals), 5):
        mineral_list.append(minerals[i:i + 5])
    # print(mineral_list)

    # picks의 개수를 고려하여, 몇번째 광물 리스트 까지 마인 작업을 할 수 있는지 확인하고 mineral_list를 재설정한다.
    pick_cnt = sum(picks)
    if len(mineral_list) > pick_cnt:  # 곡괭이가 광물보다 적다면,
        mineral_list = mineral_list[0:pick_cnt]

    # print(mineral_list)

    # 광물 리스트에서 각각 어떤 곡괭이를 부여할지를 찾는다.
    mineral_cnt = []
    for i in range(len(mineral_list)):
        mineral_tmp = [0, 0, 0]
        for j in mineral_list[i]:
            if j == "diamond":
                mineral_tmp[0] += 1
            elif j == "iron":
                mineral_tmp[1] += 1
            else:
                mineral_tmp[2] += 1
        mineral_tmp.append(i)  # 인덱스 추가
        mineral_cnt.append(mineral_tmp)

    # 정렬 다이아, 철, 돌 순으로
    mineral_cnt = sorted(mineral_cnt, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    # print(mineral_cnt)

    answer = 0
    # 정렬한 리스트에서 인덱스를 얻어서 picks에서 값을 줄여가면서 피로도를 계산한다.
    for i in mineral_cnt:
        idx = i[3]
        picks_num = 0
        if picks[0] > 0:  # 다이아가 있다면
            picks_num = 0
            picks[0] -= 1
        elif picks[1] > 0:
            picks_num = 1
            picks[1] -= 1
        elif picks[2] > 0:
            picks_num = 2
            picks[2] -= 1

        # print(answer)
        for j in mineral_list[idx]:
            if picks_num == 0:
                answer += 1

            elif picks_num == 1:
                if j == 'diamond':
                    answer += 5
                else:
                    answer += 1
            else:
                if j == 'diamond':
                    answer += 25
                elif j == 'iron':
                    answer += 5
                else:
                    answer += 1
    return answer


'''

def solution(picks, minerals):
    answer = 0

    minerals = minerals[:sum(picks)*5]
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)]

    costs = []
    for mineral in minerals:
        cost = [0, 0, 0] # dia, iron, ston
        for mine in mineral:
            if mine == 'diamond':
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mine == 'iron':
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)

    costs = sorted(costs, key=lambda x: (-x[0], -x[1], -x[2]))

    for cost in costs:
        if picks[0] > 0:
            picks[0] -= 1
            answer += cost[0]
            continue
        elif picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
            continue
        elif picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
            continue

    return answer

'''