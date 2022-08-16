import sys
sys.stdin = open('4408_자기방/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    move = [tuple(map(int, input().split())) for _ in range(n)]
    counts = 1

    startb = 0
    endb = 0
    for i in range(n):
        starta = (move[i][0]//2)-1 if move[i][0] % 2 == 0 else move[i][0]//2
        enda = (move[i][1]//2)-1 if move[i][1] % 2 == 0 else move[i][1]//2
        if starta > enda:
            starta, enda = enda, starta
        if set(range(startb, endb)) & set(range(starta, enda)):
            counts += 1
        startb, endb = starta, enda

    print(f'#{tc} {counts}')


        
        