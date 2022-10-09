n=int(input())

x1=n//3
x2=n//5
list=[]

for j in range(0,(x1+1)):
    x1=j
    for i in range(0,(x2+1)):
        x2=i
        if 3*x1+5*x2==n:
            sum=x1+x2
            list.append(sum)
if list==[]:
    print(-1)
else:
    print(min(list))

#다른풀이 5로 나누어 질때 까지 3을 빼다 보면 된다. while-else문 사용
num = int(input())
count = 0

while num >= 0:
  if num % 5 == 0:
    count += num // 5
    print(count)
    break
  
  num -= 3
  count += 1
  
else:
  print(-1)