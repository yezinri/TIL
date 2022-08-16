import sys
sys.stdin = open('1206_view/input.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    nums = list(map(int, input().split()))

    result = 0 # 조망권 확보된 세대 수
    maxnum = 0 # 좌우 2칸 이내에 있는 빌딩 중 가장 높은 층
    for i in range(2, n-2):
        for j in [i-2, i-1, i+1, i+2]:
            if nums[j] > maxnum:
                maxnum = nums[j]
        if nums[i] - maxnum > 0: # 좌우 2칸 이내의 현재보다 높은 층의 빌딩이 없으면 조망권 확보가 가능함
            result += nums[i] - maxnum 
        maxnum = 0

    print(f'#{tc} {result}')
