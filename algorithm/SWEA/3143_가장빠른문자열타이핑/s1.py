import sys
sys.stdin = open('3143_가장빠른문자열타이핑/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    typing = 0

    i = 0
    while i < len(a):
        if a[i:i+len(b)] == b:
            typing +=1
            i += len(b)
        else:
            typing += 1
            i += 1

    print(f'#{tc} {typing}')