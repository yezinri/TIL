import sys
sys.stdin = open('SWEA/4836_색칠하기/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    red = []
    blue = []
    for square in arr:
        for i in range(square[0], square[2]+1):
            for j in range(square[1], square[3]+1):
                if square[4] == 1:
                    red.append((i, j))
                else:
                    blue.append((i, j))

    counts = 0
    for i in red:
        if i in blue:
            counts += 1

    print(f'#{tc} {counts}')
