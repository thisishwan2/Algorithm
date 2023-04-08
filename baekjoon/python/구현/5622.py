import sys
word=list(map(str, sys.stdin.readline().rstrip()))

time=0
for i in word:
    if i=="A" or i=="B" or i=="C":
        time+=3
    elif i=="D" or i=="E" or i=="F":
        time+=4
    elif i=="G" or i=="H" or i=="I":
        time+=5
    elif i=="J" or i=="K" or i=="L":
        time+=6
    elif i=="M" or i=="N" or i=="O":
        time+=7
    elif i=="P" or i=="Q" or i=="R" or i=="S":
        time+=8
    elif i=="T" or i=="U" or i=="V":
        time+=9
    elif i=="W" or i=="X" or i=="Y" or i=="Z":
        time+=10
print(time)

'''
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
time = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:               a의 각자리 문자열이 dial 문자열에 있으면 (in 메서드 문자포함여부 확인)
            time += dial.index(i)+3 인덱스의 3만큼 더해야 각 다이열의 최소시간
print(ret)
'''
