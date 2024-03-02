# 최대 8!의 경우가 존재 (약 4만개)
candidate = []


def back(tmp, n, dungeons, visited):
    if len(tmp) == n:
        copy_tmp = tmp[:]  # 백트래킹에서 함수에 정의된 리스트를 복사하기 위한 스킬, 이렇게 안하면 참조값이 같아서 빈 리스트가 들어감
        candidate.append(copy_tmp)
        return
    else:
        for i in range(len(dungeons)):
            if visited[i] == 0:
                visited[i] = 1
                tmp.append(dungeons[i])
                back(tmp, n, dungeons, visited)
                visited[i] = 0
                tmp.pop()


def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [0] * n
    back([], n, dungeons, visited)

    for i in candidate:
        cnt = 0
        heart = k
        for j in i:
            if heart >= j[0] and heart - j[1] > 0:
                cnt += 1
                heart -= j[1]
        answer = max(answer, cnt)

    return answer