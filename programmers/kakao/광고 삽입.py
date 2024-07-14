# 중요한점으로 시청자 시청 종료 시간은 포함되지 않는다.
def time_to_sec(time):
    h, m, s = map(int, time.split(':'))
    return h * 60 * 60 + m * 60 + s


def sec_to_time(sec):
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f'{h:02}:{m:02}:{s:02}'


def solution(play_time, adv_time, logs):  # 동영상 재생시간, 광고 재생 가능 시간, 사용자 시청 시간

    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    arr = [0] * (play_time_sec + 1)

    # 누적합으로 풀기 위해 시청 시작 시점과 시청 종료 시점을 표시한다.(인원 표시)
    for log in logs:
        start, end = log.split("-")
        start = time_to_sec(start)
        end = time_to_sec(end)
        arr[start] += 1
        arr[end] -= 1

    # 누적합을 구한다.
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]

    # 누적합 구간중 가장 큰 곳을 찾는다.
    max_val = sum(arr[0:adv_time_sec])  # 0초부터 adv_time_sec까지의 누적합 구간의 값. 초기 값 세팅을 해줘야 이후 구간을 비교할 수 있다.
    max_time = 0
    val = max_val
    for i in range(1, len(arr) - adv_time_sec):
        val = val - arr[i - 1] + arr[i + adv_time_sec - 1]
        if val > max_val:
            max_val = val
            max_time = i
    return sec_to_time(max_time)

''' 틀린 풀이 '''
# 본 풀이는 시간초과가 발생한다. 그 이유는 최대 300000 개의 log가 주어지고, 모든 구간 0~play_time(최대 99시간 59분 59초)에 +1을 한다고 가정하면
# log(300000*play_time)이기 때문에 초과가 난다.
# 또한, 유의해야할 점은 시청 시간을 수직선 상으로 나타내면 이해가 쉬운데, 시작 시점은 포함하고, 종료 시점은 포함하면 안된다.(종료 시점 즉, 그 이전까지만 시청한다는 의미)

def solution(play_time, adv_time, logs):  # 동영상 재생시간, 광고 재생 가능 시간, 사용자 시청 시간

    h = int(play_time[0:2]) * 60 * 60
    m = int(play_time[3:5]) * 60
    s = int(play_time[6:])

    play_time_sec = h + m + s

    # max_time = 99*3600+59*60+59
    arr = [0] * (play_time_sec + 1)
    new_logs = [[0, play_time_sec]]
    for log in logs:
        start, end = log.split("-")

        h = int(start[0:2]) * 60 * 60
        m = int(start[3:5]) * 60
        s = int(start[6:])

        start_sec = h + m + s

        h = int(end[0:2]) * 60 * 60
        m = int(end[3:5]) * 60
        s = int(end[6:])

        end_sec = h + m + s

        new_logs.append([start_sec, end_sec])

        for sec in range(start_sec, end_sec + 1):
            arr[sec] += 1

    # print(arr)

    h = int(adv_time[0:2]) * 60 * 60
    m = int(adv_time[3:5]) * 60
    s = int(adv_time[6:])

    adv_time_sec = h + m + s
    max_time = 0
    max_start_time = 0
    for start, end in new_logs:
        print(arr[start:start+adv_time_sec + 1])
        if sum(arr[start:start+adv_time_sec + 1]) > max_time:
            max_time = sum(arr[start:start+adv_time_sec + 1])
            max_start_time = start

    # 되돌리기
    hour = max_start_time // 3600
    mini = (max_start_time % 3600) // 60
    sec = max_start_time % 60

    print(str(hour) + ":" + str(mini) + ":" + str(sec))




solution(	"02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"])