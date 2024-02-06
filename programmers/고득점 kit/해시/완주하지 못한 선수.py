participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# Counter 객체는 뺄셈이 가능함
# def solution(participant, completion):
#     part = Counter(participant)
#     comp = Counter(completion)
#
#     part.subtract(comp)
#
#     return ''.join(list(part.elements()))

# 같은 part는 같은 hash 값을 가진다. 따라서 sumhash에서 comp에 대한 해시값을 빼면 마지막 남은 사람만 남음
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    for comp in completion:
        sumHash -= hash(comp)

    print(hashDict[sumHash])
    return hashDict[sumHash]

solution(participant, completion)