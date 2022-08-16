import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    
    maxnum = 0 # 최대 낙차값 넣을 변수
    counts = 0 # 현재 위치의 박스보다 높이가 같거나 큰 박스 개수
    for i in range(n):
        for j in range(i, n): # 현재 위치의 박스 앞에
            if boxes[j] >= boxes[i]: # 높이가 같거나 더 큰 박스가 있다면 
                counts += 1
        if n-i-counts > maxnum:
            maxnum = n-i-counts
        counts = 0

    print(f'#{tc} {maxnum}')
