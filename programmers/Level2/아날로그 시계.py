# 초침이 시침과 겹치거나, 초침이 분침과 겹칠떼 알람이 울림

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작과 끝 시간을 초로 변경
    start_sec = h1 * 3600 + m1 * 60 + s1
    end_sec = h2 * 3600 + m2 * 60 + s2

    # 시작시간 이후부터 검사를 진행하기 때문에 시작점이 00:00:00 이거나, 12:00:00 이면 1을 더해주고 시작한다.
    if (h1 == 0 and m1 == 0 and s1 == 0) or (h1 == 12 and m1 == 0 and s1 == 0):
        answer += 1

    # 시작시간부터 끝시간까지 1초씩 증가시키면서 검사한다.
    while start_sec < end_sec:

        # 360도 중 시침은 1시간 동안 30도 -> 1초에 30/3600 = 1/120도 이동
        # 360도 중 분침은 1분동안 6도 -> 1초에 6/60 = 1/10도 이동
        # 360도 중 시침은 1초동안 6도 -> 1초에 6도 이동
        h_cur_ang = (start_sec / 120) % 360
        m_cur_ang = (start_sec / 10) % 360
        s_cur_ang = (start_sec * 6) % 360

        # 다음 위치(초침에 +1한 경우)가 마지막 각도 즉 360도 일때, 0으로 되지 않도록 한다.
        h_next_ang = 360 if (start_sec + 1) / 120 % 360 == 0 else (start_sec + 1) / 120 % 360
        m_next_ang = 360 if (start_sec + 1) / 10 % 360 == 0 else (start_sec + 1) / 10 % 360
        s_next_ang = 360 if (start_sec + 1) * 6 % 360 == 0 else (start_sec + 1) * 6 % 360

        # 초침이 분침보다 뒤에있었는데, +1한 뒤에는 앞서있다면? 한번 겹침
        if s_cur_ang < m_cur_ang and s_next_ang >= m_next_ang:
            answer += 1
        # 초침이 시침보다 뒤에있었는데, +1한 뒤에는 앞서있다면? 한번 겹침
        if s_cur_ang < h_cur_ang and s_next_ang >= h_next_ang:
            answer += 1
        # 만약 시침 초침 분침이 모두 겹친다면, 한번 겹친걸 빼준다.
        if s_next_ang == m_next_ang and s_next_ang == h_next_ang:
            answer -= 1

        start_sec += 1

    return answer