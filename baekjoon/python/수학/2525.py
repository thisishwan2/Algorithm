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

'''
더 쉬운 풀이
h,m=map(int, input().split())
t=int(input())

m=m+t       분에 소요분도 더해준다
h=h+m//60   그 분의 60으로 나눈 몫을 시간에 더한다
m=m%60      분은 60이면 안되므로 60의 나머지를 구한다
h=h%24      시간도 24이면 안되므로 24의 나머지를 구한다

print(h,m)
'''
