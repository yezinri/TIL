import sys
sys.stdin = open('4861_회문/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    out = False
    for i in range(n):
        if out:
            break
        for j in range(n-m+1):
            row = ''
            col = ''
            for k in range(m):
                row += arr[i][j+k]
                col += arr[j+k][i]
            if row == row[::-1]:
                print(f'#{tc} {row}')
                out = True
            elif col == col[::-1]:
                print(f'#{tc} {col}')
                out = True

