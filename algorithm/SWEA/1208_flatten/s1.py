import sys
sys.stdin = open('1208_flatten/input.txt', 'r')

for tc in range(1, 12):
    n = int(input())
    nums = list(map(int, input().split()))

    while n > 0:
        maxnum = minnum = nums[0]
        maxidx = minidx = 0 
        for i in range(100):
            if nums[i] >= maxnum:
                maxidx, maxnum = i, nums[i]
            elif nums[i] <= minnum:
                minidx, minnum = i, nums[i]
        if nums[maxidx] - nums[minidx] <= 1:
            break
        else:
            nums[maxidx] -= 1
            nums[minidx] += 1
        n -= 1

    maxnum = minnum = nums[0] # 최대값, 최소값 초기화 필요
    for i in range(100):
        if nums[i] >= maxnum:
            maxnum = nums[i]
        elif nums[i] <= minnum:
            minnum = nums[i]

    print(f'#{tc} {maxnum-minnum}')
