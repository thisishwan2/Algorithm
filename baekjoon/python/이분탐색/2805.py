n,m=map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

# upper bound
while start<=end:
    mid = (start+end)//2
    total = 0

    for i in tree:
        if i>mid:
            total+=(i-mid)

    # 벌목 높이를 이분탐색

    # 자른 위치에서 잘려나간 길이의 합이 타겟 값보다 크거나 같다면(=> 바꿔말하면 중간값이 타겟값보다 작거나 같으면)
    if total >= m:
        start = mid + 1

    # 자른 위치에서 잘려나간 길이의 합이 타겟 값보다 작으면(=> 중간값이 타겟값보다 크다)
    else:
        end = mid-1
print(end)