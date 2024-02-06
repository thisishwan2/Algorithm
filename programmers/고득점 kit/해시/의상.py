def solution(clothes):
    cloth_dict = {}

    for cloth, type in clothes:
        if type in cloth_dict:
            cloth_dict[type] += 1
        else:
            cloth_dict[type] = 1

    print(cloth_dict)

    # 수식은 x+a 와 같은 수식을 곱하는거로 생각하면 됨
    # 종류 1일때 a개
    # 종류 2일때 (x+a)*(x+b) = x^2+abx+ab(1대입후 계산 후 -1)
    # 이런 방식으로 쭉..

    ans = 1

    for val in cloth_dict.values():
        ans *= (1 + val)
    print(ans - 1)

    return ans - 1


def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2  # 그 옷을 고른다 안고른다 2가지 경우
        else:
            clothes_type[t] += 1  # 그 이후에는 같은 종류의 옷 개수가 늘어나서 1더함(즉, 고를 기회가 하나더 늘어남)
            # ex: ["yellow_hat", "headgear"] 일땐 경우 2개, ["yellow_hat", "headgear"], ["green_turban", "headgear"] 일때는 각각 고르는 경우+안고르는 경우 = 3

    cnt = 1
    for num in clothes_type.values():
        # 모든 경우를 계산
        cnt *= num

    return cnt - 1  # 모두 선택 안하는 경우를 제외