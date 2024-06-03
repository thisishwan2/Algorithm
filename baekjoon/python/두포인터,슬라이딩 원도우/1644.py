n = int(input())

arr=[]
tmp = [False, False] + [True]*(n-1)
# 연속된 소수를 배열에 담는다.
# 에라토스 테네스의 체
for i in range(2,n+1):

    # 소수 판별
    if tmp[i]:
        arr.append(i)
        for j in range(2*i,n+1,i):
            tmp[j]=False


# 경우의수 찾기
start=0
end=0

cnt=0
total=0

for i in range(len(arr)):

    total+=arr[i]

    if total == n:
        cnt+=1
    elif total>n:
        for j in range(start,i):
            total -= arr[j]
            if total==n:
                cnt+=1
                start = j+1
                break
            elif total<n:
                start = j+1
                break

'''
answer = 0
start = 0
end = 0
while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])
    if temp_sum == N:
        answer += 1
        end += 1
    elif temp_sum < N:
        end += 1
    else:
        start += 1

'''

print(cnt)