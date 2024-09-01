import sys
from collections import defaultdict
sys.setrecursionlimit(10**6) # 재귀 깊이를 설정한다.
def find_room(room_dict, room):
    if room_dict[room] == 0: # room이 비었다면
        room_dict[room] = room + 1 # 딕셔너리에 해당 룸의 다음 방을 넣는다.
        return room
    else: # room이 찼다면,
        # room의 val을 가지고 다시 찾는다.
        room_dict[room] = find_room(room_dict, room_dict[room])
        return room_dict[room] # 이 과정에서 이전에 존재하는 방들다음의 빈방 위치를 지정하게 된다.


# 원하는 방번호에 배정하거나, 원하는 방번호보다 크지만 젤 작은 값에 배정
def solution(k, room_number):
    answer = []
    room_dict = defaultdict(int)

    for room in room_number:
        answer.append(find_room(room_dict, room))
    return answer

# solution(10, [1,3,4,1,3,1]	)