n = int(input())
lst = []
for _ in range(n):
    x,y = map(int, input().split()) # x가 출발점, y가 도착점
    lst.append([x,y])

lst = sorted(lst)

start = -100000000
end = -100000000
ans = 0
for i in lst:
    # 처음 시작은 좌표 설정
    if start == -100000000 and end ==-100000000:
        start = i[0]
        end = i[1]
        ans+= end-start

    # 만약 이전 종료점이 현재 종료점보다 크거나 같다면, continue
    elif end>=i[1]:
        continue

    # 이전 종료지점이 현재 시작점 보다 크다 -> 중복으로 걸쳐있는 것.
    elif end>=i[0]:
        ans+=i[1]-end
        start = i[0]
        end = i[1]

    # 이전 종료지점보다 현재 시작점이 더 크면
    elif end<i[0]:
        start = i[0]
        end = i[1]
        ans+=end-start

print(ans)