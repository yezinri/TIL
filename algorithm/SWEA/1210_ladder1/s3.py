import sys
sys.stdin = open('SWEA/1210_ladder1/input.txt', 'r')

for tc in range(1, 11):
    n = int(input())                                            # n : 문제 번호
    arr = [list(map(int, input().split())) for _ in range(100)] # arr : 사다리 배열
    
		# 시작점을 찾는 반복문
    for j in range(100):
        if arr[0][j] == 1:    # 시작점 j 찾기
            nj = j            # 좌우로 이동할 nj 변수에 시작점j 값을 할당
						
            # 행 이동을 하면서 좌우값을 살피는 반복문
            for i in range(100):                            
                if 0 <= nj-1 < 100 and arr[i][nj-1] == 1:   # 왼쪽에 1이 있으면 왼쪽으로 이동
                    nj -= 1
                    while i+1 < 100 and arr[i+1][nj] == 0:  # 다음 기둥이 나올 때까지 이동
                        nj -= 1
                elif 0 <= nj+1 < 100 and arr[i][nj+1] == 1: # 오른쪽에 1이 있으면 오른쪽으로 이동
                    nj += 1
                    while i+1 < 100 and arr[i+1][nj] == 0:  # 다음 기둥이 나올 때까지 이동
                        nj += 1
                elif i == 99:
                    if arr[i][nj] == 2:
                        print(f'#{tc} {j}')  # 도착점에 대응되는 출발점 j 반환
                        break