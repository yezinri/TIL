import sys
sys.stdin = open('4828_min_max/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(n-1, 0, -1): # 정렬할 범위의 끝 위치 지정 / 버블 정렬 range범위 설정이 헷갈림
        for j in range(0, i): # 한 단계가 끝나면 가장 큰 원소가 마지막 자리에 정렬
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] 
    
    print(f'#{tc} {nums[-1] - nums[0]}')