import heapq


def solution(program):
    answer = [0] * 11
    heap = []  # heapq의 경우 리스트를 사용해야 함
    cur = 0  # 현재 시각
    program.sort(key=lambda x: (x[1], x[0]))  # 호출 시각, 우선 순위 순으로 정렬

    # cur 시간보다 작거나 같은 program 시간들을 heap에 담는다.
    def call_program():
        while len(program) > 0 and program[0][1] <= cur:
            heapq.heappush(heap, program.pop(0))  # 힙에서는 우선순위를 고려하여 넣는다.

    # 힙이 비어있지 않거나, 남은 프로그램이 있는 경우
    while len(program) > 0 or not len(heap) == 0:
        if len(heap) == 0:  # 힙이 비어있다면,
            cur = program[0][1]  # 프로그램 배열의 가장 앞의 값의 시각을 현재 시각으로 설정
            call_program()  # cur 시간보다 작거나 같은 program 시간들을 heap에 담는다.

        execute = heapq.heappop(heap)  # 실행할 프로그램을 꺼낸다.
        answer[execute[0]] += (cur - execute[1])  # 현재시간에서 - 프로그램 호출 시간을 빼서 대기시간을 넣는다.
        cur += execute[2]  # 현재시각을 갱신한다.(즉, 프로그램이 끝난 시간이 된다.)
        call_program()  # 갱신한 현재 시각을 바탕으로 이전에 호출된 프로그램을 힙에 담는다.
    answer[0] += cur

    return answer