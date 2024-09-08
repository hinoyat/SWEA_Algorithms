def back(si, sj, distance, cnt):
    global ans

    if distance >= ans:
        return

    if cnt == N:
        distance += abs(hi - si) + abs(hj - sj)
        ans = min(distance, ans)
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            back(dct[i][0], dct[i][1], distance + abs(si - dct[i][0]) + abs(sj - dct[i][1]), cnt + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    ci = lst.pop(0)
    cj = lst.pop(0)

    hi = lst.pop(0)
    hj = lst.pop(0)

    dct = {}

    idx = 1
    for i in range(0, len(lst), 2):
        dct[idx] = (lst[i], lst[i+1])
        idx += 1

    # print(dct)
    # print(lst)
    visited = [0] * (N + 1)
    ans = 100000
    back(ci, cj , 0, 0)
    print(f'#{tc} {ans}')
