import sys
a,b,v=map(int,sys.stdin.readline().split())
'''
while 문으로 문제를 풀게되면 시간초과가 발생한다.

day=2
point=a-b
if a-b>=v:
    print(day)
while True:
    point=point+a
    if (point>=v):
        print(day)
        break
    else:
        point=point-b
        day+=1'''
#노션의 풀이를 참고하자

if (v-b) % (a-b) == 0 :
    print((v-b) // (a-b))
else :
    print(((v-b) // (a-b)) +1)