import sys
sys.stdin = open('SWEA/4839_이진탐색/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    P, PA, PB = map(int, input().split())
    book = list(range(1, P+1))
    AL = BL = 0
    AR = BR = P-1

    countA = 0
    while AL <= AR:
        AC = int((AL + AR)/2)
        if book[AC] == PA:
            countA += 1
            break
        elif book[AC] > PA:
            AR = AC
            countA += 1
        else:
            AL = AC
            countA += 1

    countB = 0
    while BL <= BR:
        BC = int((BL + BR)/2)
        if book[BC] == PB:
            countB += 1
            break
        elif book[BC] > PB:
            BR = BC
            countB += 1
        else:
            BL = BC
            countB += 1

    if countA < countB:
        result = 'A'
    elif countA > countB:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')
    