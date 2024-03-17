def solution(cacheSize, cities):
    answer = 0

    cache = []

    for i in cities:
        i = i.upper()
        idx = 0

        if i in cache:
            answer += 1
            idx = cache.index(i)
        else:
            answer += 5

        if len(cache) == cacheSize:
            cache.append(i)
            cache.pop(idx) # 이부분을 그냥 pop(0)을 하면 안됨. 왜냐면 LRU 알고리즘을 사용하기 때문에 캐시 히트 한 이전 도시를 최신화 시켜야하기 때문
        else:
            cache.append(i)

    return answer