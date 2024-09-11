import heapq
def supernova(start, end):

    visited = [0xffffff] * (N + 1)
    visited[start] = 0
    que = [(0, 0)]

    while que:
        v, q = heapq.heappop(que)
        # print(info[q])
        for nv, nq in info[q]:
            new_v = v + nv
            if visited[nq] > new_v:
                visited[nq] = new_v
                heapq.heappush(que, (new_v, nq))
    return visited[-1]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    info = [[] for _ in range(N + 1)]
    for _ in range(E):
        v1, v2, val = map(int, input().split())
        info[v1].append([val, v2])

    print(f'#{tc} {supernova(0, N)}')
