import sys
sys.stdin = open('5432_쇠막대기/sample_input.txt', 'r', encoding='UTF8')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    opens = 0
    close = 0
    result = 0

    for i in range(len(arr)-1):
        if arr[i] == '(' and arr[i+1] == ')': # 레이저를 만나면 왼쪽에 짝없는 열린 괄호를 카운트
            result += opens - close
        if arr[i] == ')' and arr[i+1] == ')': # 닫힌 가로가 쌍으로 있다면 잘려나간 막대기임으로 카운트
            result += 1
        if arr[i] == '(': # 현재까지의 열린 괄호 카운트
            opens += 1
        else: # 현재까지의 닫힌 괄호 카운트
            close += 1

    print(f'#{tc} {result}')
                