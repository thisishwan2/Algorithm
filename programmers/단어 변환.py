# from collections import deque

# def solution(begin, target, words):
#     q=deque()
#     q.append([begin,0])
#     visited=[0]*len(words)

#     while q:
#         start, answer=q.popleft()
#         if(start==target):
#             return answer
#         compare=list(start)

#         for i in range(len(words)):
#             word_lst=list(words[i])
#             if visited[i]==0:
#                 cnt=0
#                 for j in range(len(compare)):
#                     if compare[j]!=word_lst[j]:
#                         cnt+=1
#                 if cnt==1:
#                     q.append([words[i],answer+1])
#                     visited[i]=1

#     return 0


from collections import deque


def get_adjacent(current, words):
    for word in words:

        count = 0
        for c, w in zip(current, word):  # zip으로 current, word 한 글자씩 뽑기 가능(zip을 쓸때는 둘의 길이를 고려)
            if c != w:
                count += 1

        if count == 1:
            yield word  # 일드를 이용함으로써 get_adjacent의 결과로 변환가능한 word만 리턴할 수 있음(전체 리스트를 반환 x)


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)