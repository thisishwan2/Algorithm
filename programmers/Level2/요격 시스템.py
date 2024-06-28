# 미사일 최소 사용
# s,e 좌표의 미사일은 요격안됨(테두리는 요격안됨)
def solution(targets):
    answer = 0
    targets = sorted(targets, key=lambda x: x[1])

    check = -1  # 끝점 좌표
    for i in range(len(targets)):
        if check <= targets[i][0]:  # 끝점 좌표와 i의 앞쪽 좌표를 비교(앞쪽 좌표가 더 크거나 같으면 둘은 한번에 요격되지 않음)
            check = targets[i][1]  # 끝점 업데이트
            answer += 1

    return answer