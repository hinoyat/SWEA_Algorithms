import pprint
from collections import deque

def supernova(info):

    que = deque(info)
    visited = [[0] * len(arr[0]) for _ in range(len(arr))]
    for i, j, v in que:
        visited[i][j] = 1
    # print(que)
    # print(arr)
    # print(visited)

    while que:
        qi, qj, v = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < len(arr) and 0<= nj <len(arr[0]) and visited[ni][nj] == 0 and visited[ni][nj] == visited[qi][qj] + 1:
                visited[ni][nj] = visited[qi][qj] + 1



T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * (N + (K * 2)) for _ in range(K)] + [[0] * K +  list(map(int, input().split())) + [0] * K for _ in range(N)] + [[0] * (N + K * 2) for _ in range(K)]
    # pprint.pprint(arr)

    start_info = []

    for i in range(K, len(arr) - K):
        for j in range(K , len(arr) - K):
            if arr[i][j] != 0:
                start_info.append([i, j, arr[i][j]])
    # print(start_info)
    supernova(start_info)
