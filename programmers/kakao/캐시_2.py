from collections import deque


def solution(cacheSize, cities):
    answer = 0
    order = deque()
    cache = {}

    if cacheSize == 0:
        answer = len(cities) * 5
        return answer

    for i in cities:
        i = i.upper()
        if len(cache) < cacheSize:
            # 이전에 캐시에 있었으면
            if i in cache:
                order.remove(i)
                order.append(i)
                answer += 1
            else:
                cache[i] = 1
                answer += 5
                order.append(i)
        else:
            if i in cache:
                order.remove(i)
                order.append(i)
                answer += 1
            else:
                key = order.popleft()
                del cache[key]
                cache[i] = 1
                order.append(i)
                answer += 5
    # print(answer)
    return answer

# solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"])


