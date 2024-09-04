# from collections import deque
# import copy
#
#
# def BFS(i, arar):
#     visited = [[0] * H for _ in range(W)]
#     que = deque()
#     st_p = []
#     for s in range(len(arar[i])):
#         if arar[i][s] != 0:
#             st_p = (i, s)
#             break
#     if not st_p:
#         return arar
#
#     s1, e1 = st_p
#     que.append((s1, e1))
#     visited[s1][e1] = 1
#     while que:
#         qi, qj = que.popleft()
#         for d in range(1, arar[qi][qj]):
#             for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#                 ni = qi + di * d - 1
#                 nj = qj + dj * d - 1
#                 if 0<= ni < H and 0<= nj < W and visited[ni][nj] == 0:
#                     visited[ni][nj] = 1
#                     que.append((ni,nj))
#         arar[qi][qj] = 0
#     for i in arar:
#         i.sort()
#     # print(arar)
#     return arar
#
#
#
# def supernova(level, idx, arrr):
#     global max_z
#     if level == N:
#         result = 0
#         for i in arrr:
#             result += i.count(0)
#         max_z = max(max_z, result)
#         return
#
#     for i in range(W):
#         if arrr[i] == [0] * H: continue
#         n_ar = BFS(i, copy.deepcopy(arrr))
#         supernova(level + 1, i, n_ar)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, W, H = map(int, input().split())
#     arr = [list(map(int, input().split()))for _ in range(H)]
#     # 깨지는 최댓값 찾기
#     newarr = [list(row) for row in zip(*arr)]
#     max_z = 0
#     print(arr)
#     print(newarr)
#     supernova(0, 0, copy.deepcopy(newarr))
#     print((W*H) - max_z)





from collections import deque
import copy


def BFS(i, arar):
    visited = [[0] * realj for _ in range(reali)]
    que = deque()
    st_p = None
    for s in range(realj):
        if arar[i][s] != 0:
            st_p = (i, s)
            break
    if not st_p:
        return arar

    s1, e1 = st_p
    que.append((s1, e1))
    visited[s1][e1] = 1
    while que:
        qi, qj = que.popleft()

        for d in range(1, arar[qi][qj]):
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni = qi + di * d
                nj = qj + dj * d
                if 0 <= ni < reali and 0 <= nj < realj and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    que.append((ni, nj))
        arar[qi][qj] = 0

    # 벽돌 아래로 떨어뜨리기
    for c in range(reali):
        not_zero = [x for x in arar[c] if x != 0]
        arar[c] = [0] * (realj - len(not_zero)) + not_zero

    return arar


def supernova(level, idx, arrr):
    global max_z
    if level == N:
        result = 0
        for i in arrr:
            result += i.count(0)
        # print(result)
        max_z = max(max_z, result)
        return

    for i in range(W):
        n_ar = BFS(i, copy.deepcopy(arrr))
        supernova(level + 1, i, n_ar)


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    newarr = list(map(list, zip(*arr)))
    # print(newarr)
    reali = len(newarr)
    realj = len(newarr[0])
    max_z = 0
    supernova(0, 0, copy.deepcopy(newarr))
    print(f"#{tc} {W * H - max_z}")