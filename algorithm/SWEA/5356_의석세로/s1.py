import sys
sys.stdin = open('5356_의석세로/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    text = [input() for _ in range(5)]
    result = ''

    for j in range(15):
        for i in range(5):
            if len(text[i]) > j:
                result += text[i][j]

    print(f'#{tc} {result}')