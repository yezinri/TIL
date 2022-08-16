import sys
sys.stdin = open('SWEA/1213_string/test_input.txt', 'r', encoding='UTF8')

for tc in range(1, 11):
    n = input()
    p = input()
    t = input()
    pl = len(p)
    tl = len(t)

    cnt = 0
    for i in range(tl):
        if t[i:i+pl] == p:
            cnt += 1

    print(f'#{n} {cnt}')
