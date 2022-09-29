n=int(input())
ans=0
for i in range(n):
    a,b,c=map(int, input().split())
    if a==b==c:
        ans=max(ans,10000+1000*a)
    elif a==b or b==c:
        ans=max(ans,1000+100*b)
    elif a==c:
        ans=max(ans,1000+100*a)
    else:
        ans=max(ans,max(a,b,c)*100)
print(ans)