T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [map(int, input().split()) for _ in range(N)]

    di = [0, 0, 1, -1,   1, 1, -1, -1]
    dj = [1, -1, 0, 0,   1, -1, -1, 1]

    max_v = 0

    for i in range(N):
        sum_v1 = 0
        sum_v2 = 0
        for j in range(N):
            sum_v1 += arr[i][j]
            sum_v2 += arr[i][j]

            for k in range(1, M+1):
                for d in range(4):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    if 0<=ni<N and 0<=nj<N:
                        sum_v1 +=arr[ni][nj]
            if sum_v1 > max_v:
                max_v = sum_v1

            for k in range(1, M+1):
                for d in range(4, 8):
                    ni = i + di[d] * k
                    nj = j + dj[d] * k
                    if 0<=ni<N and 0<=nj<N:
                        sum_v2 +=arr[ni][nj]
            if sum_v2 > max_v:
                max_v = sum_v2

        print(f'#{tc} {max_v}')