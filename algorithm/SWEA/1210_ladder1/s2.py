import sys
sys.stdin = open('SWEA/1210_ladder1/input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100): # 도착지점 
        if data[99][j] == 2:
            for i in range(n-1, -1):
                if 0 <= nj-1 < 100 and data[i][j-1] == 1:
                    k = -1
                    while True:
                        j += k
                        if data[i-1][j] == 1:
                            break
                elif 0 <= nj+1 < 100 and data[i][j+1] == 1:
                    k = 1
                    while True:
                        j += k
                        if data[i-1][j] == 1:
                            break
        print(f'#{tc} {j}')

                        
