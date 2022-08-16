import sys
sys.stdin = open('4408_자기방/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    move = [tuple(map(int, input().split())) for _ in range(n)]
    room = [0] * 200

    for i in range(n):
        start = (move[i][0]//2)-1 if move[i][0] % 2 == 0 else move[i][0]//2
        end = (move[i][1]//2)-1 if move[i][1] % 2 == 0 else move[i][1]//2
        if start <= end:
            for j in range(start, end+1):
                room[j] += 1
        else:
            for j in range(start, end-1, -1):
                room[j] += 1

    maxV = 0
    for count in room:
        if count > maxV:
            maxV = count

    print(f'#{tc} {maxV}')