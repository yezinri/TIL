import sys
sys.stdin = open('SWEA/1209_sum/input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = 0

    for i in range(100): # 각 행의 합
        add = 0
        for j in range(100):
            add += arr[i][j]
        if add > maxV:
            maxV = add

    for i in range(100): # 각 열의 합
        add = 0
        for j in range(100):
            add += arr[j][i]
        if add > maxV:
            maxV = add

    add = 0
    for i in range(100): # 우하향 대각선의 합
        add += arr[i][i]
    if add > maxV:
        maxV = add

    add = 0
    for i in range(100): # 좌하향 대각선의 합
        add += arr[i][n-1-i]
    if add > maxV:
        maxV = add     

    print(f'#{n} {maxV}')

    