import sys

n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    if word not in lst:
        lst.append(word)
lst.sort()  #먼저 사전순으로 정렬
lst.sort(key=lambda x: len(x))  #그후 글자수로 정렬

for i in lst:
    print(i)

#메모리 최소
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))