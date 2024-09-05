def supernova(si, sj, result):

    if len(result) == 7:
        check.add(result)
        return

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = si + di
        nj = sj + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # visited[ni][nj] = 1
            supernova(ni, nj, result + arr[ni][nj])
            # visited[ni][nj] = 0

T = int(input().strip())
for tc in range(1, T+1):
    N = 4
    arr = [list(input().split()) for _ in range(N)]
    check = set()
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            supernova(i, j, arr[i][j])
    print(f'#{tc} {len(check)}')
