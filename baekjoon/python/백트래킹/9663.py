#9663

import sys
input=sys.stdin.readline

n=int(input())

#row[i]=j 가 의미하는것은 [i,j]에 체스가 있다는 의미

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i])==abs(x-i): # 같은 열에 있거나, 대각선에 있는 경우 제외
            return False
    
    return True

def backtracking(x):
    global ans

    if x==n:
        ans+=1
        return

    else:
        for i in range(n):
            row[x]=i
            if is_promising(x): # 통과하면 뎁스가 하나 증가하고 다시 0부터 하나씩 가능성을 확인
                backtracking(x+1)

ans=0
row=[0]*n
backtracking(0)
print(ans)