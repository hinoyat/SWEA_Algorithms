def supernova(idx, connected, line , remain):
    global ans, max_connect

    if idx == core_cnt:
        if max_connect < connected:
            max_connect = max(max_connect, connected)
            ans = line

        elif max_connect == connected:
            ans = min(ans, line)
        return

    if connected + remain < max_connect:
        return

    supernova(idx + 1, connected , line, remain - 1)

    ci, cj = core_lst[idx]
    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        save_idx = []
        while 0<= ni < N and 0<= nj < N and arr[ni][nj] == 0:
            save_idx.append([ni, nj])
            ni, nj = ni + di, nj + dj

        if ni >= N or nj >= N or ni < 0 or nj < 0:
            for i, j in save_idx:
                arr[i][j] = -2
            supernova(idx + 1, connected + 1, line + len(save_idx), remain - 1)
            for i, j in save_idx:
                arr[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 직선으로만 연결 가능

    # 벽에 붙은 건 연결로 친다

    # 최대로 연결할 수 있는 전선의 방향을 찾아야 함

    # 전선 길이의 최솟값
    ans = 21e8
    # 연결 길이의 최댓값
    max_connect = 0

    core_lst = []

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if arr[i][j] == 1:
                core_lst.append([i, j])

    core_cnt = len(core_lst)

    supernova(0, 0, 0, core_cnt)

    print(f'#{tc} {ans}')
