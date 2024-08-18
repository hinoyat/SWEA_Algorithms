from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # first_cnt = 0
    
    # first_cnt += M - arr[0].count('W')
    
    # first_cnt += M - arr[N-1].count('R')
    # print(first_cnt)

    finishWB = False

    count = [[0]*3 for _ in range(N)]
    for i in range(N):
        count[i][0] = arr[i].count('W')
        count[i][1] = arr[i].count('B')
        count[i][2] = arr[i].count('R')
    
    com = [i for i in range(1, N)]
    # print(count)
    # print(com)
    ls = list(combinations(com, 2))
    # print(ls)
    min_v = 21e8
    for c in ls:
        l1, l2 = c
        # print(l1, l2)
        w = 0
        b = 0
        r = 0
        for i in range(0, l1):
            w += arr[i].count('R') + arr[i].count('B')
        for j in range(l1, l2):
            b += arr[j].count('R') + arr[j].count('W')
        for k in range(l2, N):
            r += arr[k].count('W') + arr[k].count('B')
        re = w + b + r
        if re < min_v:
            min_v = re
    print(f'#{tc} {min_v}')
