from collections import deque


def supernova():
    visited = [[-1] * M for _ in range(N)]
    que = deque()
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                que.append([i, j])
                visited[i][j] = 0
    
    while que:
        qi, qj = que.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = qi + di
            nj = qj + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == -1:
                que.append([ni,nj])
                visited[ni][nj] = visited[qi][qj] + 1
                result += visited[ni][nj]
    return result




T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    ans = 0
    check = []
    print(supernova())
    

