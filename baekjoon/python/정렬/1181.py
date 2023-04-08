import sys

n=int(sys.stdin.readline())
lst=[]
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    if word not in lst:
        lst.append(word)
#정렬 순서를 주의해야 되는데, 상위 조건 A와 하위 조건 B가 있으면
#먼저 B로 정렬을 한 후에 A로 정렬을 해야 원하는 결과를 얻을 수 있다.
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
