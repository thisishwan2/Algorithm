#1931

#시간초과
import sys

n=int(sys.stdin.readline())

times=[]

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append([start,end])

times.sort(key=lambda x: (x[0]))

lst=[]
while True:

    for i in range(n):
        cnt=1
        for j in range(n):
            if times[i][1]<=times[j][0]:
                i=j
                cnt+=1
        lst.append(cnt)
    break

print(max(lst))

#sol

import sys

n=int(sys.stdin.readline())

times=[]

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    times.append([start,end])

#빨리 끝나는 회의 순서대로 정렬. 빨리 회의가 끝나야 그 뒤의 많은 경우를 고려해볼 수 있다.
times.sort(key=lambda x: (x[1], x[0]))

#가장 빨리 끝나는 회의는 선택하는 것이므로 cnt=1 부터 시작한다.
cnt=1
end_time=times[0][1]

for i in range(1,n):
    #i번째 시작시간이 end_time보다 크거나 같으면(회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.)
    if times[i][0]>=end_time:
        #+1
        cnt+=1
        #그 시각의 끝나는 시간을 end_time에 저장
        end_time=times[i][1]

print(cnt)