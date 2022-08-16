import sys
sys.stdin = open('SWEA/1210_ladder1/input.txt', 'r')

for tc in range(1, 11):
    t = int(input())
    n = 100
    data = [list(map(int, input().split())) for _ in range(n)]
    dj = [-1, 1]

    start = [] # 시작점
    for i in range(n):
        if data[0][i] == 1: 
            start.append(i)

    for j in start: # 열 좌표
        nj = j
        for i in range(n): # 행 좌표
            for k in dj:
                while True:
                    if 0 <= nj+k < n and data[i][nj+k] == 1:
                        nj += k
                        if i < n-1 and data[i+1][nj] == 1:
                            break
        if data[99][nj] == 2:
            print(f'#{tc} {j}')
