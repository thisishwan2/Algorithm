line = list(input())

ans = 0
s=[]
for idx, val in enumerate(line):
    if val == "(":
        s.append("(")
    else:
        if line[idx-1] == "(": # 레이저면
            s.pop()
            ans+=len(s)
        else: # 선이 끝나는 위치면
            s.pop()
            ans+=1
print(ans)