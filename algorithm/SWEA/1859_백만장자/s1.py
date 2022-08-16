import sys
sys.stdin = open('1859_백만장자/input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))
    maxp = 0
    profit = 0

    for i in range(n-1, -1, -1):
        if maxp - price[i] > 0:
            profit += maxp - price[i]
        else:
            maxp = price[i]

    print(f'#{tc} {profit}')