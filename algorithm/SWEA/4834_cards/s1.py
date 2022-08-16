import sys
sys.stdin = open('4834_cards/sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = input()

    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1

    maxnum = [0, 0]
    for i in count:
        if count.get(i) > maxnum[1]:
            maxnum = [i, count.get(i)]
        elif count.get(i) == maxnum[1]:
            if i > maxnum[0]:
                maxnum = [i, count.get(i)]

    print(f'#{tc} {maxnum[0]} {maxnum[1]}')