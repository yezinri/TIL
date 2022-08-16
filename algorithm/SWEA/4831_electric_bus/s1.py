import sys
sys.stdin = open('4831_electric_bus/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split()) # k: 최대 이동 거리 / n: 종점까지 정류장 / m: 설치된 충전기 개수
    charge = list(map(int, input().split()))
    now = 0 # 현재 정류장 위치
    count = 0 # 충전 횟수

    for i in range(m):
        if charge[i] - now > k: # 바로 앞 충전소와의 거리가 k보다 크면 연료 부족
            count = 0
            break
        elif charge[i] - now == k: # 바로 앞 충전소와의 거리가 k 라면 다른 선택지 고려하지 않고 이동
            now = charge[i]
            count += 1
        else: # 바로 앞 충전소와의 거리가 k 보다 작다면 충전 횟수를 최소화하기 위해 그 다음 충전소와의 거리도 고려
            if i != m-1 and charge[i+1] - now <= k: # 그 다음 충전소와의 거리가 k이하라면 다음 충전소로 이동
                    pass 
            elif n - now <= k: # 마지막 충전소에 있을 시 종점까지의 거리가 k이하라면 pass
                    pass 
            else: # 그것도 아니면 바로 앞 충전소로 이동해서 충전
                now = charge[i]
                count += 1

    print(f'#{tc} {count}')
            
