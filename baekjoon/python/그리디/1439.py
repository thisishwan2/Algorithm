#1439

s=input()

cnt=0


if s==str(1)*len(s) or s==str(0)*len(s):
    print(cnt)

else:
    fir=s[0]
    for i in range(len(s)-1):
        if s[i+1]!=fir and s[i]!=s[i+1]:
            cnt+=1
    print(cnt)

#다른 풀이
change = 0
prev = '?'
string = input()
for i in string:
    if i != prev: change += 1
    prev = i
print(change//2)