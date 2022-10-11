#꼭 다시풀어보기

import sys

n=int(sys.stdin.readline().rstrip())
group_word=0
for _ in range(n):
    word=sys.stdin.readline().rstrip()
    error=0
    for i in range(len(word)-1):
        if word[i]!=word[i+1]:          #연달은 문자가 다르다면
            new_word=word[i+1:]         #new_word 는 word[i]이후의 문자열이다. 'a'  'ba'
            if new_word.count(word[i])>0: #new_word에 word[i]의 글자가 있다면 EX) " 'a' ba"
                error+=1                
    if error==0:
        group_word+=1
print(group_word)
