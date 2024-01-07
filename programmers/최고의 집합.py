def solution(n, s):
    ans = []
    if s // n < 1:
        return [-1]
    elif s % n == 0:
        for i in range(n):
            ans.append(s // n)
        return ans
    else:
        for _ in range(n):
            ans.append(s // n)
            s = s - s // n
            n = n - 1

    return sorted(ans)