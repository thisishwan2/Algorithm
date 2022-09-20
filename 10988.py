'''
w=input()
x=1
for i in range(len(w)//2):
    if w[i]!=w[-i-1]:
        print(0)
        x=0
        break
if x==1:
    print(x)'''

#더 직관적으로 풀어보자
'''
w=list(input())

if list(reversed(w))==w:
    print(1)
else:
    print(0)'''

w=input()
if w==w[::-1]:
    print(1)
else:
    print(0)