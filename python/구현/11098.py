n=int(input())
for _ in range(n):
    p=int(input())
    list_price=[]
    list_name=[]
    for _ in range(p):
        c,name=input().split()
        c=int(c)
        list_price.append(c)
        list_name.append(name)
    a=list_price.index(max(list_price))    
    print(list_name[a])
