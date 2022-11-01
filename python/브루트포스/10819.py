#순열 풀이
from itertools import permutations

n = int(input())
arr = list(map(int ,input().split()))
#튜플형태로 리스트에 저장됨.
permu = list(permutations(arr, n))


res=0
#i에 튜플 째로 들어감.
for i in permu:
    sum=0
    for j in range(n-1):
        sum+=abs(i[j]-i[j+1])
    res=max(res,sum)

print(res)

#백트래킹 향후 서술할 예정