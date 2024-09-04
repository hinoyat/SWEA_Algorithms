def direction(info, order, direct):
    if direct == 0:
        pass
    if direct == 1:
        pass
    if direct == 2:
        pass
    if direct == 3:
        pass


def armageddon(info, cnt, order, direct):
    global ans


    if (i, j) in ((0, N-1), (N-1, 0), (0, 0), (N-1, N-1)):
        return 0
    armageddon(info, cnt + 1, 0)
    armageddon(direction(info, order, direct), cnt + 1, 1)






T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    check = set()
    ans = 0
    visited = [[0] * N for _ in range(N)]

