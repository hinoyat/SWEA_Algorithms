from collections import deque


def BFS():
    cnt = 0
    visited = [0] * (N+1)
    for i in range(1, N + 1):
        if graph[i] and not visited[i]:
            visited[i] = 1
            que = deque([i])
            # print(que)
            cnt += 1
            while que:
                v = que.popleft()
                # print(v)
                for s in graph[v]:
                    if visited[s] == 0:
                        visited[s] = 1
                        que.append(s)
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    lst = list(map(int, input().split()))
    check_set = set(lst)
    len_l = len(lst)
    graph = [[] for _ in range(N+1)]
    for i in range(0, len_l, 2):
        v1 = lst[i]
        v2 = lst[i+1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    group = N - len(check_set)
    result = BFS()
    print(f'#{tc} {group + result}')
