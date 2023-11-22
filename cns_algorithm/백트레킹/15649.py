# 백트레킹
#15649

import sys
input=sys.stdin.readline

n,m=map(int, input().split())

ans=[]

def back():
    for i in range(1,n+1):
        if len(ans)==m:
            print(" ".join(map(str, ans)))
            return
        else:
            if i not in ans:
                ans.append(i)
                back()
                ans.pop()
back()
