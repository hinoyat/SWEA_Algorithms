# import pprint
# from collections import deque
#
# def supernova(info):
#
#     que = deque(info)
#     visited = [[-1] * len(arr[0]) for _ in range(len(arr))]
#
#     for i, j, v, val in que:
#         visited[i][j] = 1
#
#     while que:
#         qi, qj, v, val = que.popleft()
#         arr[qi][qj] -= 1
#         if arr[qi][qj] > 0:
#             que.append([qi, qj, v, val])
#         elif arr[qi][qj] == 0:
#             for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#                 ni, nj = qi + di, qj + dj
#                 if 0<= ni < len(arr) and 0<= nj <len(arr[0]):
#                     if visited[ni][nj] == visited[qi][qj] + 1:
#                         if arr[ni][nj] < val and arr[ni][nj] != 0:
#                             arr[ni][nj] = val
#                         # que.append([ni, nj, v, val])
#                     elif visited[ni][nj] == -1:
#                         visited[ni][nj] = visited[qi][qj] + 1
#                         arr[ni][nj] = val
#                         que.append([ni, nj, v, val])
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#     arr = [[0] * (N + (K * 2)) for _ in range(K)] + [[0] * K + list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (N + K * 2) for _ in range(K)]
#     start_info = []
#
#     for i in range(K, len(arr) - K):
#         for j in range(K , len(arr) - K):
#             if arr[i][j] != 0:
#                 start_info.append([i, j, arr[i][j], arr[i][j]])
#     # print(start_info)
#     supernova(start_info)
#     ans = 0
#     pprint.pprint(arr)
#     for i in arr:
#         ans += sum(i)
#
#     print(ans)




import pprint
from collections import deque

def supernova(arr, info):
    que = deque(info)
    visited = [[-1] * len(arr[0]) for _ in range(len(arr))]

    for i, j, v, val in que:
        visited[i][j] = 0  # 시작점은 0으로 설정

    while que:
        # pprint.pprint(arr)
        qi, qj, v, val = que.popleft()
        arr[qi][qj] -= 1
        if arr[qi][qj] > 0:
            que.append([qi, qj, arr[qi][qj], val])
        elif arr[qi][qj] == 0:
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = qi + di, qj + dj
                if 0 <= ni < len(arr) and 0 <= nj < len(arr[0]):
                    if visited[ni][nj] == -1:
                        visited[ni][nj] = visited[qi][qj] + 1
                        arr[ni][nj] = val
                        que.append([ni, nj, arr[ni][nj], val])

                    elif visited[ni][nj] == visited[qi][qj] + 1:
                        if arr[ni][nj] > 0 and arr[ni][nj] < val:
                            arr[ni][nj] = val

                    if visited[ni][nj] > K:
                        return



T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * (N + (K * 2)) for _ in range(K)] + \
          [[0] * K + list(map(int, input().split())) + [0] * K for _ in range(N)] + \
          [[0] * (N + K * 2) for _ in range(K)]
    start_info = []

    for i in range(K, len(arr) - K):
        for j in range(K, len(arr[0]) - K):
            if arr[i][j] != 0:
                start_info.append([i, j, arr[i][j], arr[i][j]])

    supernova(arr, start_info)
    ans = sum(sum(row) for row in arr)

    print(f"#{tc} {ans}")