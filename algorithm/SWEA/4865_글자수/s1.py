import sys
sys.stdin = open('4865_글자수/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1, str2 = input(), input()

    count = {}
    for i in str1:
        count[i] = 0
    
    for j in str2:
        if j in count:
            count[j] += 1

    maxV = 0
    for k in count.values():
        if k > maxV:
            maxV = k

    print(f'#{tc} {maxV}')