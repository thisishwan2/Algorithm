#다음번에는 로직을 정리하고 짜도록하자. 결국 아래의 풀이랑 같은 의미이지만 풀이가 두서없다.
t=int(input())

for i in range(t):
    h,w,n=map(int, input().split())

    if n%h==0:
        x=n//h
        y=str(h)
    else:
        x=(n//h)+1
        y=str(n%h)

    if x<10:
        x="0"+str(x)
    else:
        x=str(x)
    

    print(y+x)

#다른 풀이
#층수는 N에서 건물 층수를 나눈 나머지가 되고, 
# 호수는 N에서 건물 층수를 나눈 몫 +1 이 된다. 
# 만일 N이 건물 층수의 배수인 경우에는 층수는 입력받은 층수 그대로 되고,
# 호수는 N에서 건물 층수는 나눈 몫이 된다.

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(f'{floor*100+num}')   #층에 100을 곱함으로 3자리 수를 만들어준다.