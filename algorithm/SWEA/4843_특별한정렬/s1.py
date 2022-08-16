import sys
sys.stdin = open('SWEA/4843_특별한정렬/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', end=" ")
    for i in range(5):
        print(f'{arr[-(i+1)]} {arr[i]}', end=" ")
    print()