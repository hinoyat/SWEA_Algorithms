import heapq

def supernova(graph, start, end):
    que = [(0, end)]
    visited = [123456789] * (N + 1)
    visited[end] = 0
    while que:
        qval, qv = heapq.heappop(que)
        if qval > visited[qv]:
            continue
        for nval, nv in graph[qv]:
            newval = qval + nval
            if newval > visited[nv]: continue

            visited[nv] = newval
            heapq.heappush(que, (newval, nv))
    return visited[1:]




T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    go_graph = [[]for _ in range(N + 1)]
    back_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        v1, v2, val = map(int, input().split())
        go_graph[v1].append((val, v2))
        back_graph[v2].append((val, v1))

    go_result = supernova(go_graph, N, X)
    back_result = supernova(back_graph, N, X)

    print(go_graph)
    print(go_result)
    print(back_graph)
    print(back_result)

    ans = 0
    for i in range(N):
        hino = go_result[i] + back_result[i]
        ans = max(ans, hino)
    print(f'#{tc} {ans}')