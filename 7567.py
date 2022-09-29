'''
내가 처음 푼  풀이
a=input("")
sum=10

for i in range(1,len(a)):
    if a[i]== "(":
        if a[i-1]==a[i]:
            sum=sum+5
        else:
            sum=sum+10
    elif a[i]==")":
        if a[i]==a[i-1]:
            sum=sum+5
        else:
            sum=sum+10
print(sum)'''
#더 간결한 다른 풀이

a=list(input())
sum=0
for i in range(len(a)):
    if i==0:
        sum=sum+10
    elif a[i]==a[i-1]:
        sum=sum+5
    else:
        sum=sum+10
print(sum)

