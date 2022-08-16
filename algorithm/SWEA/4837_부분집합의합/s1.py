import sys
sys.stdin = open('SWEA/4837_부분집합의합/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(range(1, 13))
    ans = 0

    for i in range(1<<len(nums)):
        add = 0
        counts = n
        for j in range(len(nums)):
            if i & (1<<j):
                add += nums[j]
                counts -= 1
        if counts == 0 and add == k:
            ans += 1

    print(f'#{tc} {ans}')

    