import sys

cro_alpha=["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = sys.stdin.readline().rstrip()

for i in cro_alpha:
    if i in word:
        word=word.replace(i, "a")   #크로아티아 문자열은 아무 문자열(여기선 a)로 바꿔준다

print(len(word))