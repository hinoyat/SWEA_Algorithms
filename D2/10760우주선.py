from pprint import pprint
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint(arr)


    di = [0, 1, 1,  1,  0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1,  0,  1]

    can = 0
    for i in range(N):
        for j in range(M):
            start_p = arr[i][j]
            cnt = 0
            for d in range(8):
                new_i = i + di[d]
                new_j = j + dj[d]
                if new_i < 0 or new_i >= N or new_j < 0 or new_j >= M:
                    pass
                else:
                    if arr[new_i][new_j] < start_p:
                        cnt += 1
            if cnt >= 4:
                can += 1

    print(f'#{tc} {can}')