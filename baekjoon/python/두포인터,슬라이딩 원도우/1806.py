import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
answer = 1e9
total = arr[0] # 누적합 사용(본 문제의 핵심)(초기값을 배열의 첫 원소로)
break_flag = False
while break_flag == False:

    # 누적합이 s보다 크거나 같으면
    if total >= s:
        answer = min(answer, end - start+1)
        total -= arr[start]
        start += 1

    # 누적합이 s보다 작으면
    else:
        if end + 1 < n:
            end+=1
            total += arr[end]
        else:
            break_flag = True

if answer == 1e9:
    print(0)
else:
    print(answer)


