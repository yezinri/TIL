import sys
sys.stdin = open('4861_회문/sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    text = [input() for _ in range(n)]

    # 행에서 회문 찾기
    for i in range(n):
        for j in range(n-m+1):
            for k in range(m//2):
                if text[i][j+k] != text[i][n-m-1-(j+k)]:
                    break
                elif k == (m//2)-1:
                    print(f'#{tc} {text[i][j:j+m]}')
                    break
    
    # 열에서 회문 찾기
    for i in range(n):
        for j in range(n-m+1):
            result = []
            for k in range(m//2):
                if text[j+k][i] != text[n-m-1-(j+k)][i]:
                    break
                else:
                    result.insert(len(result)//2, text[j+k][i])
                    result.insert(len(result)//2, text[n-m-1-(j+k)][i])
                    if k == (m//2)-1:
                        if m % 2 == 1:
                            result.insert(len(result)//2, text[j+k+1][i])
                        print(f'#{tc} {"".join(result)}')
                        break
