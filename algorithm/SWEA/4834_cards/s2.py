import sys
sys.stdin = open('4834_cards/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input()))

    # 카운팅 정렬
    counts = [0] * 10 
    for i in range(n):
        counts[nums[i]] += 1
    
    maxnum = [0, 0] # 가장 많은 카드의 숫자와 장수 담을 리스트
    for j in range(10):
        if counts[j] >= maxnum[1]: # maxnum의 장수와 같거나 같으면
            maxnum = [j, counts[j]] # 해당 인덱스 값으로 바꿔줌

    print(f'#{tc} {maxnum[0]} {maxnum[1]}')