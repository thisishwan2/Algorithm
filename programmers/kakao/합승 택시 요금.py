def solution(n, s, a, b, fares):  # 지점 개수, 출발지점, A 도착지점, B 도착지점, 금액 배열

    fee = [[1e9 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in fares:
        c = i[0]
        d = i[1]
        f = i[2]
        fee[c][c] = 0
        fee[d][d] = 0
        fee[c][d] = f
        fee[d][c] = f
    print(b)
    # 모든 지점을 하차 지점이라 생각하고, min 값을 찾는다.(플로위드 와샬)
    for i in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                fee[x][y] = min(fee[x][y], fee[x][i] + fee[i][y])

    # print(*fee, sep="\n")

    total = 1e9
    # 모든 지점이 환승 구역일때,
    for i in range(1, n + 1):
        # 시작점 부터 i 까지는 같이 가고, i부터 a,b 까지의 거리만 계산
        total = min(total, fee[s][i] + fee[i][a] + fee[i][b])

    # print(total)

    return total
# solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])