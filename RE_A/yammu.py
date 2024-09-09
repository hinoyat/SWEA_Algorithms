def supernova(check, cnt, di, si, sj, end_point):
    global ans
    if si < 0 or sj < 0 or si >=N or sj >= N :
        return

    if di == 3 and cnt * 2 <= ans:
        return


    if (si, sj) == end_point and di == 4:
        ans = max(ans, cnt)
        return

    if arr[si][sj] in check:
        return



    # 방향 바꿀래 안 바꾸래
    check.add(arr[si][sj])
    ni, nj = si + direction[di][0], sj + direction[di][1]

    supernova(check, cnt + 1, di, ni, nj, end_point)
    if di < 4:
        supernova(check, cnt + 1, di + 1, ni, nj, end_point)
    check.remove(arr[si][sj])



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = -1
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = {
        1: (-1, 1),
        2: (1, 1),
        3: (1, -1),
        4: (-1, -1)
        }
    for i in range(N - 1):
        for j in range(0, N - 1):
            supernova(set(), 0, 1, i, j, (i, j))

    print(f'#{tc} {ans}')
