import sys

n=int(sys.stdin.readline())
res=[]

for i in str(n):
    res.append(int(i))

res.sort(reverse=True)
result=list(map(str, res))

print("".join(result))

#간단한 풀이
#숫자로 된 문자열을 역순 정렬
print("".join(sorted(input(), reverse=True)))