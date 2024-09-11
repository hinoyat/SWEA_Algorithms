import heapq
def supernova():

    que = [(0, 0, 0)]
    visited = [[0xffffff] * N for _ in range(N)]
    visited[0][0] = arr[0][0]
    min_v = 0xffffff

    while que:
        val, qi, qj = heapq.heappop(que)
        if qi == N - 1 and qj == N - 1:
            min_v = min(min_v, val)
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < N and 0<= nj < N:
                if arr[qi][qj] < arr[ni][nj]:
                    newval = val + (arr[ni][nj] - arr[qi][qj]) + 1
                else:
                    newval = val + 1

                if newval < visited[ni][nj]:
                    visited[ni][nj] = newval
                    heapq.heappush(que, (newval, ni, nj))

    return min_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {supernova()}')
