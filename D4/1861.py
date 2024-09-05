def supernova(start_point, si, sj, cnt):
    global max_v
    global start_p

    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni = si + di
        nj = sj + dj
        # 갈 수 있는 곳 찾기
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == arr[si][sj] + 1 and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            supernova(start_point, ni, nj, cnt + 1)
            visited[ni][nj] = 0
        else:
            # 먼저 최댓값 갱신
            max_v = max(cnt, max_v)
            # 이 조건이 없이 하게 되면 원래 딕셔너리에 있던 값보다 작은 값이 덮어씌워짐
            if cnt >= max_v:
                result[start_point] = cnt




T = int(input().strip())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = {}
    max_v = -1
    start_p = 21e8
    # 모든 지점에서 함수 돌리기
    for i in range(N):
        for j in range(N):
            supernova(arr[i][j], i, j, 1)

    # 딕셔너리의 키를 정렬해줘서 작으면서 max 값인 key 찾기
    check = list(result.keys())
    check.sort()
    # print(result)
    # 찾으면 멈추기
    for i in check:
        if result[i] == max_v:
            start_p = i
            break

    print(f'#{tc} {start_p} {max_v}')
