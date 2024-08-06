import heapq


def solution(jobs):
    hq = []
    jobs = sorted(jobs)
    cur = 0
    ans = 0
    n = len(jobs)

    while len(jobs) != 0 or len(hq) != 0:
        if len(hq) == 0:
            start, time = jobs.pop(0)
            cur = start + time
            ans += cur - start
        else:
            time, start = heapq.heappop(hq)
            cur = cur + time
            ans += cur - start
        while len(jobs) != 0 and cur > jobs[0][0]:  # 요청시간이 현재 시간보다 작으면
            start, time = jobs.pop(0)
            heapq.heappush(hq, (time, start))

    print(ans // n)
    return ans // n


solution([[0, 3], [1, 9], [2, 6]])