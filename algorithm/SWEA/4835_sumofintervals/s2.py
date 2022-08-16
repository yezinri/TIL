import sys
sys.stdin = open('4835_sumofintervals/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    minnum, maxnum = 100000000, 0

    add = 0
    for i in range(n-m+1):
        for j in range(m):
            add += nums[i+j]
        if add < minnum:
            minnum = add
        if add > maxnum:
            maxnum = add
        add = 0
    
    print(f'#{tc} {maxnum - minnum}')
