from collections import defaultdict
from pprint import pprint


# 방향 델타

def change_val(i, j, lst):

    max_v = 0
    v = 0
    d = 0
    cnt = 0
    for nv, nd in lst:
        max_v = max(max_v, nv)
        v += nv
        if nv >= max_v:
            d = nd
        cnt += 1

    if cnt == 1:
        return i, j, v, d
    else:
        return i, j, v, d


def moving(i, j, lst):
    i += direction[lst[1]][0]
    j += direction[lst[1]][1]

    v = lst[0]
    d = lst[1]
    if arr[i][j] == -1:
        d = direction[lst[1]][2]
        v//=2

    return i, j, v, d


T = int(input())
for tc in range(1, T+1):
    direction = {
        1:(-1, 0, 2),
        2:(1, 0, 1),
        3:(0, -1, 4),
        4:(0, 1, 3)
    }
    # 배열, 시간, 미생물
    N, M, K = map(int, input().split())

    arr = [[-1] * N for _ in range(N)]

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            arr[i][j] = 0


    misaeng = defaultdict(list)
    for _ in range(K):
        i, j, v, d = map(int,input().split())
        misaeng[(i, j)].append((v, d))



    # 이동 시키는 횟수
    for _ in range(M):
        new_misaeng = defaultdict(list)
        for mi, mj in misaeng:
            ni, nj, nv, nd = moving(mi, mj, *misaeng[(mi, mj)])
            new_misaeng[(ni, nj)].append((nv, nd))
        # print(new_misaeng)
        # print(misaeng)
        for ci, cj in new_misaeng:
            ni, nj, nv, nd = change_val(ci, cj, new_misaeng[(ci, cj)])
            new_misaeng[(ni, nj)] = [(nv, nd)]
        misaeng = new_misaeng
    ans = 0
    # print(misaeng)

    for v in misaeng:
        ans += misaeng[v][0][0]

    print(f'#{tc} {ans}')

