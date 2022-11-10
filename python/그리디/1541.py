import sys

a=sys.stdin.readline()

res=0
if "-" in a:
    a=a.rstrip().split("-")
    for i in a:
        if "+" in i and res==0:
            num=i.split("+")
            res=sum(map(int,num))
        elif "+" in i:
            num=i.split("+")
            res-=sum(map(int,num))
        elif res==0:
            num=int(i)
            res=res+num
        else:
            num=int(i)
            res-=num
else:
    a=map(int, a.rstrip().split("+"))
    res=sum(a)
print(res)

