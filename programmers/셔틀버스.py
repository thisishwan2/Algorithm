# 9시부터 n번 t분 간격 역도착, m명이 최대 승객수
# 셔틀 도착한 시점에 줄슨 인원도 자리가 남으면 태우고감
# 콘이 셔틀타고 갈수있는 제일 늦은 시각 구하기
# 콘은 같은 시간에 도착한 사람이 여러명이면 제일 뒤에 슨다.
#모든 크루는 23:59에 집을 간다.-> 다음날 셔틀 탈일 없음
def solution(n, t, m, timetable): #n: 셔틀 운행수, t:셔틀 운행 간격, m:한셔틀 최대 크루수 timetable: 크루 도착시간
    
    #수치형으로 변경
    for i in range(len(timetable)):
        a,b = timetable[i].split(":")
        hour=int(a)*60
        timetable[i]= hour+int(b)
    timetable = sorted(timetable)
    print(timetable)
    
    # 첫차 시간
    first_bus = 540
    # {버스 시간: 탄 사람의 시간}
    bus={first_bus+t*i:[] for i in range(n)}
    print(bus)
    
    # 탑승여부 리스트
    ride=[0]*len(timetable) #0은 미탑승, 1은 탑승
    
    
    answer=0
    for i in bus:
        for j in range(len(timetable)):
            # 버스 도착시간보다 작거나 같아야 탑승
            # 탑승한 인원은 탑승 불가
            # 최대 탑승인원이상은 탑승 불가
            if i>=timetable[j] and ride[j]==0 and len(bus[i])<m:
                bus[i].append(timetable[j])
                ride[j]=1
    
    print(bus)
    
    # 막차 시간
    last_time = list(bus.keys())[-1]
    
    # 막차에 자리가 남아 있으면 막차시간에 정류장 도착
    if len(bus[last_time])<m:
        answer= last_time
    
    # 꽉 차있으면
    else:
        answer = bus[last_time][-1] -1
    
    hour = str(answer//60)
    min =  str(answer%60)
    
    if len(hour)==1:
        hour = "0"+hour
    
    if len(min)==1:
        min = "0"+min
        
    answer = hour+":"+min
    
    return answer