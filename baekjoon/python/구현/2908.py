import sys

a,b=sys.stdin.readline().split()

a=a[::-1]   #역순 배치
b=b[::-1]

print(max(int(a),int(b)))
