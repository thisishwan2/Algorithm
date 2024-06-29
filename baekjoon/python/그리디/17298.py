#
n =int(input())
lst = list(map(int, input().split()))

answer = [-1]*n
tmp = []
for i,val in enumerate(lst):
    while tmp and tmp[-1][1] < val:
        answer[tmp[-1][0]] = val
        tmp.pop()
    tmp.append([i,val])
print(*answer)