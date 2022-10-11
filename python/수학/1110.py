# 1번 풀이(1번 수행해서 next랑 new값을 만들어주고 while문 수행, n은 고정된 값이기때문)
n = input()
if len(n) == 1:     #길이가 1일때 n변수의 값을 0n으로 만드는 if문
    n = "0" + n
next = int(n[0]) + int(n[1])  # 2 + 6 = 8
new = n[-1] + str(next)[-1]  # 6 8 (맨 오른쪽 수를 가져오는)
cnt = 1
if n == new:
    print(cnt)
    exit(0)

while True:
    next = int(new[0]) + int(new[1])  # 6 + 8 = 14
    new = new[-1] + str(next)[-1]  # 8 4
    cnt += 1
    if new == n:
        break

print(cnt)

#2번 풀이(str)
n=input()
num=n
cnt=0
while True:
    if len(num)==1:
        num="0"+num
    plus = str(int(num[0])+int(num[1])) # 8(plus)= 2+6
    num= num[-1] + plus[-1] # 6 8
    cnt+=1
    if num==n:
        print(cnt)
        break

#3번 풀이(int)
n=int(input())      #68
num=n
cnt=0

while True:
    a=num//10       #6
    b=num%10        #8
    c=(a+b)%10      #14%10 -> 4
    num=(b*10)+c    # 80 + 4 =84

    cnt+=1
    if num==n:
        break
print(cnt)
