'''a1,b1=map(int, input().split())
a2,b2=map(int, input().split())
a3,b3=map(int, input().split())

if a1==a2:
    a4=a3
elif a1==a3:
    a4=a2
else:
    a4=a1

if b1==b2:
    b4=b3
elif b1==b3:
    b4=b2
else:
    b4=b1

print(a4,b4)'''

#리스트를 이용해 간략히 풀면

x_num=[]
y_num=[]
for _ in range(3):
    x,y=map(int,input().split())
    x_num.append(x)
    y_num.append(y)

for i in range(3):
    if x_num.count(x_num[i])==1:
        x4=x_num[i]
    if y_num.count(y_num[i])==1:
        y4=y_num[i]
print(x4,y4)