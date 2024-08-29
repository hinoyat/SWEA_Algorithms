from collections import deque

def BFS(start):
    visited = [[-1]*N for _ in range(N)]
    max_len = 0
    r = 1
    que = deque()
    si, sj = start
    cur_high = arr[si][sj]
    que.append([si, sj])
    visited[si][sj] = 1
    while que:
        qi, qj = que.pop()
        max_way = 0
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = qi + di
            nj = qj + dj
            if 0<= ni < N and 0<= nj < N and arr[ni][nj] <= cur_high and visited[ni][nj] == -1:
                if arr[ni][nj] > max_way:
                    max_way = arr[ni][nj]

        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = qi + di
            nj = qj + dj
            if 0<= ni < N and 0<= nj < N and arr[ni][nj] <= cur_high and visited[ni][nj] == -1 and arr[ni][nj] == max_way:
                if arr[ni][nj] == cur_high:
                    cur_high -= 1
                    visited[ni][nj] = visited[qi][qj] + 1
                    que.append([ni, nj])
                else:
                    cur_high = arr[ni][nj]
                    visited[ni][nj] = visited[qi][qj] + 1
                    que.append([ni, nj])
                    if visited[ni][nj] > max_len:
                        max_len = visited[ni][nj]
                r += 1

    return max_len




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_v:
                max_v = arr[i][j]

    st_p = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_v:
                st_p.append([i,j])

    result = []
    for r in st_p:
        result.append(BFS(r))

    print(max(result))