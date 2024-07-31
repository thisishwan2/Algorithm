import heapq

def solution(n, paths, gates, summits): # n: 지점의 수, paths: 등산로 2차원 배열(i,j,time), gates: 출입구의 번호 배열, summits: 산봉우리 번호 배열
    # 인접리스트 생성
    arr = [[]for _ in range(n+1)]
    for i, j, k in paths:
        arr[i].append([j,k])
        arr[j].append([i,k])

    print(*arr,sep="\n")

    # 산봉우리 판별
    is_summit = [0]*(n+1)
    for i in summits:
        is_summit[i] = 1

    distance = [1e9]*(n+1)
    hq = []
    for gate in gates:
        distance[gate] = 0
        heapq.heappush(hq, [0,gate]) # intensity, 게이트 번호

    while hq:
        intensity, gate = heapq.heappop(hq)
        # 이전에 해당 노드가 더 작은 가중치를 갖는다면 넘어가고, 산봉우리면 continue
        if distance[gate] < intensity or is_summit[gate]==1:
            continue

        for num, dist in arr[gate]:
            dist = max(dist, intensity) # 이전까지 최대 가중치와 현재 가중치 비교
            if dist<distance[num]: # 다음 노드의 현재 가중치와 위에서 구한 비교 가중치중 비교 가중치가 더 작다면
                distance[num]=dist
                heapq.heappush(hq, [dist, num])

    result = [-1,1e9]
    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0]=summit
            result[1]=distance[summit]
    return result


solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[1, 3],	[5])