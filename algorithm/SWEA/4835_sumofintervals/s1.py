import sys
sys.stdin = open('SWEA/4835_sumofintervals/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    result = []
    add = 0
    for i in range(n-m+1):
        for j in range(m):
            add += nums[i+j]
        result.append(add)
        add = 0

    print(f'#{tc} {max(result)-min(result)}')