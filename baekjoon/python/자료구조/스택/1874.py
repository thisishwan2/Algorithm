n=int(input())
num=0
s=[]
ans=[]
for _ in range(n):

    cmd = int(input())

    if num<cmd:
        for i in range(num+1, cmd+1):
            s.append(num+1)
            ans.append("+")
            num+=1
        ans.append("-")
        s.pop()
    elif s[-1] == cmd:
        s.pop()
        ans.append("-")
    elif s[-1] != cmd:
        print("NO")
        exit(0)

for i in range(len(ans)):
    print(ans[i])