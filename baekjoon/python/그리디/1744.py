from collections import deque
n = int(input())

positive = []
negative = []
zero_cnt = 0
one_cnt = 0

for _ in range(n):
    num = int(input())
    if num>1:
        positive.append(num)
    elif num<0:
        negative.append(num)
    elif num == 1:
        one_cnt+=1
    else:
        zero_cnt+=1

answer = 0

positive.sort(reverse=True)
negative.sort()

# 양수는 곱한다.
positive = deque(positive)
while positive:
    if len(positive)>=2:
        num1 = positive.popleft()
        num2 = positive.popleft()
        answer += num1*num2
    else:
        num1 = positive.popleft()
        answer += num1

negative = deque(negative)
# 음수끼리도 곱한다.
while len(negative)>=2:
    num1 = negative.popleft()
    num2 = negative.popleft()
    answer+= num1*num2

# 만약 음수가 한개 남았다면, 0이 있는 경우에는 둘이 곱하고, 아닌경우에는 그냥 더한다.
if negative:
    if zero_cnt == 0:
        answer+=negative.popleft()

# 1은 그냥 더한다.
answer+=one_cnt
print(answer)