def solution(sizes):
    tmp = []

    for i in sizes:
        first = i[0]
        second = i[1]
        if second > first:
            tmp.append([second, first])
        else:
            tmp.append([first, second])

    first_max = 0
    second_max = 0

    for i in tmp:
        if i[0] > first_max:
            first_max = i[0]
        if i[1] > second_max:
            second_max = i[1]

    answer = first_max * second_max

    return answer

# []에서 앞을 큰수 뒤를 작은수로 정렬
# 1. [[60,50],[70,30],[60,30],[80,40]] => 80*50
# 2. [[10,7],[12,3],[15,8],[14,7],[15,5]] => 15*8
# 3. [[14,4], [19,6],[16,6],[18,7],[11,7]] => 19*7

# 더 쉬운 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
# 즉, 해당 for문을 보면 [60,50] 중에 max는 왼쪽, min은 오른쪽, [70,30] 중 70은 왼쪽, 30은 오른쪽
# 이와 같은 방법으로 2값중 max 인 리스트가 왼쪽에 min인 리스트가 오른쪽에 위치되고, 그 리스트중 최대값을 구해서 곱하는 것이다.
