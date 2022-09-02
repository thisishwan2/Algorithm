hour, min=map(int, input().split())
take_time=int(input())

hour=hour+take_time//60         #소요 분이 60이 넘어가면 몫을 받아 시간에 더해준다
min=min+take_time%60            #소요 분의 나머지를 받아 분에 더해준다

if min >=60:                    #분이 60을 넘어가면
    min=min-60                  #0분부터 시작하고
    hour=hour+1                 #한시간 더해준다.
if hour >=24:                   #시간이 24시간과 같거나 넘어가면 문제 조건에 맞게
    hour=hour-24                #0시부터 시작하도록 한다.    

print(hour,min)

