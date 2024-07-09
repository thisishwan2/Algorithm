# 이 문제는 그리디 문제
# 핵심은 라이언이 이기기로 마음먹은 점수라면 어피치가 쏜것보다 1발만 더 맞추고, 남은 화살은 0점에 몰빵하는게 중요하다
# 이렇게 하면 10~1점까지 라이언이 해당 점수에서 이길지 질지만(win=1, lose=0) 따지면 되기 때문에 2^10의 경우만 고려하면 된다.
# dfs를 이용하여 경우에 수를 전부 구하고, 해당 경우를 모두 for문으로 탐색한다.
# 탐색하면서 실제 라이언이 쏜 화살을 배열로 만들어놓는다.
# 이때 n발 이상 쏜 경우는 제외한다
# 그 후 각 점수에 대해 라이언이 이긴지, 어피치가 이긴지 확인하고 점수를 부여한다.
# 점수를 부여한 배열을 최종 결과 배열에 넣어둔다. 이때 점수차도 넣어준다.
# 이제 점수차가 큰 순서대로, 가장 작은 점수를 많이 맞춘 순서대로 정렬을 진행해준다.
# 가장 첫번째 요소를 확인하고 조건에 맞게 답을 반환한다.

candidate = []


# 10점부터 1점까지 win/lose에 대한 경우를 모두 구한다.
def dfs(tmp, index):
    if len(tmp) == 10:
        candidate.append(tmp[:])
        return

    for i in range(index, 10):
        for j in range(2):  # 0은 lose, 1은 win
            tmp.append(j)
            dfs(tmp, i + 1)
            tmp.pop()


def solution(n, info):
    answer = []
    dfs([], 0)

    result = []
    for lst in candidate:
        ryan_info = [0] * 11
        for index, val in enumerate(lst):
            if val == 1:  # 라이언이 이기는 점수라면
                ryan_info[index] = info[index] + 1  # 어피치보다 1발 더 쏜경우이다.

        if sum(ryan_info) > n:
            continue

        # 만약 화살이 남았으면 0점에 다 넣는다.
        if sum(ryan_info) < n:
            ryan_info[10] += (n - sum(ryan_info))

        # 점수차를 구한다.
        ryan_score = 0
        apeach_score = 0
        score = 10
        for ryan, apeach in zip(ryan_info, info):
            if ryan > apeach:
                ryan_score += score
            elif ryan == 0 and apeach == 0:
                pass
            else:
                apeach_score += score

            if score > 0:
                score -= 1
            else:
                continue

        # 마지막에 점수차 append
        ryan_info.append(ryan_score - apeach_score)

        result.append(ryan_info)

        result = sorted(result, key=lambda x: (
        -x[-1], -x[-2], -x[-3], -x[-4], -x[-5], -x[-6], -x[-7], -x[-8], -x[-9], -x[-10], -x[-11], -x[-12]))

    if result[0][-1] <= 0:
        return [-1]
    else:
        return result[0][:11]

    return answer