def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    start = 1
    end = distance

    while start <= end:
        mid = (start + end)//2 # 각 바위 지점 사이의 거리의 최솟값 중 최대값이라고 가정(추후 이것을 답으로 사용)

        previous = 0
        count = 0
        for rock in rocks:
            if rock - previous < mid: # 이전 바위와의 거리 차이를 보고, mid 보다 작은 경우에는 그 바위 지점을 제거 한다고 생각(더 작은 거리가 있으면 안됨.)
                count += 1
                if count > n: break
            else: # 이전 바위보다 거리가 크면, 이전 바위를 업데이트
                previous = rock

        # 바위 사이의 거리의 최솟값을 줄인다.
        if count > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer