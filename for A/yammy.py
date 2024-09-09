# def direction(i, j, direct):
#     if direct == 0:
#         ni = i - 1
#         nj = j + 1
#         return ni, nj, direct + 1
#
#     if direct == 1:
#         ni = i + 1
#         nj = j + 1
#         return ni, nj, direct + 1
#     if direct == 2:
#         ni = i + 1
#         nj = j - 1
#         return ni, nj, direct + 1
#
#     if direct == 3:
#         ni = i - 1
#         nj = j - 1
#         return ni, nj, direct
#
#
#
# def armageddon(i, j, cnt, direct, si, sj):
#     global ans
#
#     if i > N-1 or i < 0 or j > N-1 or j < 0:
#         return
#
#     if i == si and j == sj and cnt > 0 :
#         ans = max(ans, cnt )
#         return
#
#     if arr[i][j] in check:
#         return
#
#
#     dr = {0:(-1, 1), 1:(1, 1), 2:(1, -1), 3:(-1, -1)}
#     ni = i + dr[direct][0]
#     nj = j + dr[direct][1]
#     check.add(arr[i][j])
#     if 0<=ni<N and 0<= nj < N and arr[ni][nj] not in check:
#         armageddon(ni, nj, cnt + 1, direct, si, sj)
#
#     ni, nj, new_direct = direction(i, j, direct)
#     if 0<=ni<N and 0<= nj < N and arr[ni][nj] not in check:
#         armageddon(ni, nj, cnt + 1, new_direct, si, sj)
#     check.remove(arr[i][j])
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     check = set()
#     ans = -1
#     memo = {}
#
#
#     for i in range(1, N):
#         for j in range(0, N - 1):
#             check = set()
#             armageddon(i, j, 0, 0, i, j)
#     print(f'#{tc} {ans}')


def direction(i, j, direct):
    if direct == 0:
        ni = i - 1
        nj = j + 1
        return ni, nj, direct + 1

    if direct == 1:
        ni = i + 1
        nj = j + 1
        return ni, nj, direct + 1
    if direct == 2:
        ni = i + 1
        nj = j - 1
        return ni, nj, direct + 1

    if direct == 3:
        ni = i - 1
        nj = j - 1
        return ni, nj, direct


def armageddon(i, j, cnt, direct, si, sj):
    global ans

    if i > N - 1 or i < 0 or j > N - 1 or j < 0:
        return

    if i == si and j == sj and cnt > 0:
        ans = max(ans, cnt)
        return

    if direct == 2:
        if cnt * 2 <= ans:
            return

    if arr[i][j] in check:
        return

    dr = {0: (-1, 1), 1: (1, 1), 2: (1, -1), 3: (-1, -1)}
    ni = i + dr[direct][0]
    nj = j + dr[direct][1]
    check.add(arr[i][j])
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in check:
        armageddon(ni, nj, cnt + 1, direct, si, sj)

    ni, nj, new_direct = direction(i, j, direct)
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in check:
        armageddon(ni, nj, cnt + 1, new_direct, si, sj)
    if ni == si and nj == sj:
        armageddon(ni, nj, cnt + 1, new_direct, si, sj)
    check.remove(arr[i][j])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = set()
    ans = -1
    memo = {}

    for i in range(1, N):
        for j in range(0, N - 1):
            check = set()
            armageddon(i, j, 0, 0, i, j)
    print(f'#{tc} {ans}')