#나는 중복되는 요소. 즉, 같은 카드가 3개 뽑히는 경우를 배제해야 된다고 생각했다.
import sys

n, m = map(int,sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
big=0

#따라서 아래의 3중 for 문에 if 문을 달아서 중복을 제외했다.
for i in card:
    fir=i
    for j in card[1:]:
        if i==j:
            continue

        sec=j
        for k in card[2:]:
            if i==k or j==k:
                continue

            thr = k    
            res=fir+sec+thr
            if (res<=m):
                big=max(big,res)
print(big)
#하지만 이렇게 풀었을 경우 시간이 오래나왔다. 따라서 좀더 효율적인 코드를 생각해봤다.

#아래의 코드의 for문을 잘 보자. range의 범위를 잘보면, 중복이 될 것을 방지하여 범위를 설정했다.
# i와 j가 변하는 값에 대해 범위를 조정해줌으로써 중복을 피했다.
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
nlst = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            three =  lst[i] + lst[j] + lst[k]
            if three > M:
                continue
            else:
                nlst.append(three)
print(max(nlst))