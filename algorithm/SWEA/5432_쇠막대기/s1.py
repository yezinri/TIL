import sys
sys.stdin = open('SWEA/5432_쇠막대기/sample_input.txt', 'r', encoding='UTF8')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    cnt = 0
    result = 0

    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] != ')':
            for j in range(i+1, len(arr)):
                if arr[j] == '(':
                    cnt += 1
                elif arr[j] == ')' and cnt != 0:
                    cnt -= 1
                else:
                    lazer = 0
                    for k in range(i+1, j):
                        if arr[k] == '(' and arr[k+1] == ')':
                            lazer += 1
                    result += lazer + 1
                    break
    
    print(f'#{tc} {result}') # 런타임 에러
