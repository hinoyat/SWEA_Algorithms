T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    center = [N//2, N//2]

    sum_v = 0
    for i in range(N):
        for j in range(N):
            if abs(center[0] - i) + abs(center[0]-j) < N//2:
                sum_v += arr[i][j]
    print(f'#{tc} {sum_v}')