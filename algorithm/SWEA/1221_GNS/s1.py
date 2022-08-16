import sys
sys.stdin = open('SWEA/1221_GNS/GNS_test_input.txt', 'r', encoding='UTF8')

T = int(input())

for tc in range(1, T+1):
    n = int(input().split()[1])
    arr = input().split()

    order = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    print(f'#{tc}')
    for i in order:
        for j in range(n):
            if arr[j] == i:
                print(i, end=' ')
    print()

