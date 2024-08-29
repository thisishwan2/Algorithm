def solution(n, k, cmd):
    cur = k  # 현재 위치를 나타내는 커서
    table = {i: [i - 1, i + 1] for i in range(n)}  # 더블 링크드 리스트를 딕셔너리로 표현
    answer = ['O'] * n
    # 양 끝단은 None으로 초기화
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    stack = []  # 삭제 정보를 담을 스택

    for c in cmd:

        # 삭제
        if c == "C":
            answer[cur] = 'X'
            prev, next = table[cur]
            stack.append([prev, cur, next])

            # 삭제에 따른 cur 위치 조정
            if next == None:
                cur = table[cur][0]
            else:
                cur = table[cur][1]

            # 맨 앞 행을 지우는 거면
            if prev == None:
                # 지우는 행  = 다음 행의 이전 행 => None으로 처리
                table[next][0] = None

            # 맨 마지막 행을 지우는 거면
            elif next == None:
                # 지우는 행 = 이전 행의 다음 행 => None 처리
                table[prev][1] = None

            # 중간에 있는 것을 지우면
            else:
                # 중간 노드를 지우고 연결
                table[prev][1] = next
                table[next][0] = prev

        # 복구
        elif c == "Z":
            prev, now, next = stack.pop()
            answer[now] = 'O'

            if prev == None:
                table[next][0] = now
            elif next == None:
                table[prev][1] = now
            else:
                table[next][0] = now
                table[prev][1] = now

        # 이동
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)

            # 표의 범위를 벗어나지는 않는다.
            if c1 == 'D':
                for _ in range(c2):
                    cur = table[cur][1]
            else:
                for _ in range(c2):
                    cur = table[cur][0]

    return ''.join(answer)