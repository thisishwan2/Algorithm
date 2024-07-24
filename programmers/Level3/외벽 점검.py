from itertools import permutations

def solution(n, weak, dist):
    dist.sort(reverse = True) # 가장 멀리 갈 수 있는 인원부터 수행한다.
    len_weak = len(weak)

    # 반시계 방향을 신경쓰지 않기 위해 원형 배열을 선형으로 변경해주는 작업
    tmp = []
    for i in weak:
        tmp.append(i+n)
    weak = weak+tmp

    for i in range(1, len(dist)+1): # i는 몇명의 인원을 쓰는지 숫자
        # 가장 멀리 가는 인원 i명 뽑음
        for dis in permutations(dist[:i]):
            # 점검의 시작점을 설정하는 idx. 즉, idx부터 len_weak 만큼의 weak를 가지고 모든 취약점을 돌았는지 확인
            for idx in range(len_weak):
                people_dist = list(dis)
                new_weak = weak[idx:idx+len_weak]

                # 점검한다.(people_dist의 첫번째 인원이 점검할수 있는 칸을 다 점검하고, 그다음위치에 2번째 인원이 점검할수 있는 칸을 점검하는 것을 반복)
                while people_dist and new_weak:
                    # 점검을 하는 사람이 이동하는 거리 추출
                    d = people_dist.pop(0)
                    # 점검 위치 추출
                    p = new_weak.pop(0)
                    # 이동하는 사람이 점검한 후 위치
                    current = d+p

                    # w와 current 사이에 있는 지점은 d가 다 점검함
                    while new_weak and new_weak[0] <= current:
                        new_weak.pop(0)

                # 점검할 위치가 없으면 정답~
                if len(new_weak) == 0:
                    return i
    return -1

solution(5, [0, 1, 2, 3, 4], [7])