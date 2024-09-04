def back(idx, val, cnt):
    global ans

    if val > ans:
        return

    if 0 not in visited_col:
        ans = min(ans, val)

    for i in range(N):
        if visited_col[i] == 0:
            visited_col[i] = 1
            back(idx + 1 ,val + arr[idx][i], cnt + 1)
            visited_col[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    ans = 0xffffff
    visited_col = [0] * N

    back(0, 0, 0)

    print(f'#{tc} {ans}')
