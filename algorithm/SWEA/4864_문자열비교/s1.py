import sys
sys.stdin = open('4864_문자열비교/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1, str2 = input(), input()

    count = 0
    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            count += 1

    print(f'#{tc} {count}')
