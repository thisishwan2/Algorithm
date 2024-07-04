# 풀이법 - 조합가능한 컬럼의 인덱스를 뽑은 다음, 유일성을 만족하는 지 확인한다.
# 그 후 유일성을 만족하는 것들을 길이순으로  sort 한뒤 for문을 돌리면서 set으로 변환해서 최소성을 확인한다.
# 이때 a.issubset(b) 메서드를 활용한다.
# 중요한 점은 set과 딕셔너리 키로는 리스트를 쓸 수 없다.(immutable만 가능하기 때문)

def dfs(tmp, num, visited, n, start):
    global index_candidate

    if len(tmp) == num:
        index_candidate.add(tuple(tmp))
        return

    for i in range(start, n):
        if visited[i] == 0:
            tmp.append(i)
            visited[i] = 1
            dfs(tmp, num, visited, n, i)
            tmp.pop()
            visited[i] = 0


def solution(relation):
    global index_candidate
    answer = 0

    n = len(relation[0])
    index_candidate = set()
    # 컬럼의 길이를 가지고, 만들수 있는 인덱스 조합을 만든다.
    for i in range(1, n + 1):
        visited = [0 for _ in range(n)]
        dfs([], i, visited, n, 0)

    # print(index_candidate)
    # print(len(index_candidate))

    result = set()
    # 해당 인덱스 조합을 for문으로 돌리면서, relation을 순회한다. 이때 딕셔너리를 이용해서 중복여부를 파악하면서 key를 만든다.
    for index_list in index_candidate:
        tmp = {}

        unique = True
        for row in relation:
            # key = [] 딕셔너리 키에는 리스트 사용 불가
            key = ""
            for num in index_list:
                key += row[num]

            # 중복이 존재하지 않으면, 딕셔너리에 추가
            if tmp.get(key) == None:
                tmp[key] = ""
                continue
            # 중복이 존재하면 break
            else:
                unique = False
                break
                # 유일한 경우
        if unique:
            result.add(index_list)
    # print(result)
    # 가능한 인덱스 조합을 result 에 넣고, 해당 result에서 최소성을 만족하는 지만 확인한다.

    result = sorted(result, key=lambda x: len(x))
    # print(result)

    unique_list = []
    for i in result:
        unique = True
        for j in unique_list:
            if j.issubset(set(i)): # set을 이용해서 부분집합 포함 여부를 파악
                unique = False
                break

        if unique:
            answer += 1
            unique_list.append(set(i))
        else:
            continue

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])