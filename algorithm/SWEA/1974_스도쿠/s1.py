import sys
sys.stdin = open('1974_스도쿠/input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    
    result = 1
    for i in range(9):
        row = []
        col = []
        if i == 0 or i == 3 or i == 6:
            square = [[], [], []]
        for j in range(9):
            
            if arr[i][j] in row:                # 행
                result = 0
            else:
                row.append(arr[i][j])
            
            if arr[j][i] in col:                # 열
                result = 0
            else:
                col.append(arr[j][i])
            
            if j < 3:                           # 3X3
                if arr[i][j] in square[0]:
                    result = 0
                else:
                    square[0].append(arr[i][j])
            elif j < 6:
                if arr[i][j] in square[1]:
                    result = 0
                else:
                    square[1].append(arr[i][j])
            else:
                if arr[i][j] in square[2]:
                    result = 0
                else:
                    square[2].append(arr[i][j])

        if result == 0:
            print(f'#{tc} {result}')
            break
       
    else:
        print(f'#{tc} {result}')
