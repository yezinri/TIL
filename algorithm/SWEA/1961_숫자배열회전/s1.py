import sys
sys.stdin = open('1961_숫자배열회전/input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr[-j-1][i], end='')
        print(end=' ')
        for j in range(n):
            print(arr[-i-1][-j-1], end='')
        print(end=' ')
        for j in range(n):
            print(arr[j][-i-1], end='')
        print()