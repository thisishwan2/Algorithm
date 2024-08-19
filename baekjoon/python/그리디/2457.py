n=int(input())

days = []
for _ in range(n):
    days.append(list(map(int, input().split())))

days.sort()
latest_end=(3,1)
i=0
answer = 0

while i<n:
    max_end= latest_end

    flag = False
    # 중요한 스킬. 튜플을 이용하면, 날짜 비교가 용이하다.
    # 그리고 정렬을 하면, latest_end보다도 먼저 끝나는 애들이 있는데, 이런 애들 까지 고려를 해서 while문을 짜야 한다.
    while i<n and ((days[i][0], days[i][1]) <= latest_end < (days[i][2], days[i][3]) or ((days[i][2], days[i][3])<=latest_end)):
        if ((days[i][0], days[i][1]) <= latest_end < (days[i][2], days[i][3])) and max_end<(days[i][2], days[i][3]):
            max_end=(days[i][2], days[i][3])
        i+=1
        flag = True

    # 만약 이전에 심어진 날보다 이전에 끝난다면, 굳이 처리할 필요 없음
    if not flag:
        i += 1
        continue
    else:
        # 후보군들을 전부다 보고 난뒤에는 꽃이 심어진 날짜를 변경한다.
        latest_end = max_end
        answer += 1

        if latest_end>(11,30):
            print(answer)
            exit(0)
print(0)
