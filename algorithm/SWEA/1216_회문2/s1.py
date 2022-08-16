import sys
sys.stdin = open('1216_회문2/input.txt', 'r')

for tc in range(1, 11):
    tc = input()
    n = 100
    arr = [input() for _ in range(n)]
    
    maxlen = 0
    for i in range(n):
        for j in range(n):
            row = ''
            col = ''
            for k in range(n-j):
                row += arr[i][j+k]
                col += arr[j+k][i]
                if row == row[::-1] and len(row) > maxlen:
                    maxlen = len(row)
                if col == col[::-1] and len(col) > maxlen:
                    maxlen = len(col)

    print(f'#{tc} {maxlen}')