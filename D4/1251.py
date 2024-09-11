def find_mama(c):
    if c != parent[c]:
        parent[c] = find_mama(parent[c])
    return parent[c]


def family(a, b):
    a = find_mama(a)
    b = find_mama(b)

    if a == b:
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

import heapq, math

# def bbbung(start_node):
#     visited = [float('inf')] * N
#     que = [(0, start_node)]
#     visited[start_node] = 0
#
#     ans =
#
#     while que:
#         qval, q = heapq.heappop(que)
#         for nv in graph[q]:
#             if not visited[nv]:
#                 new_val = int(E * ((abs(x_info[q] - x_info[nv])**2) + (abs(x_info[q] - x_info[nv])**2)))
#                 if new_val <


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_info = list(map(int, input().split()))
    y_info = list(map(int, input().split()))
    graph = [[i for i in range(N)]for _ in range(N)]
    E = float(input())

    parent = [i for i in range(N)]

    info = []

    for i in range(N-1):
        for j in range(i + 1, N):
            new_val = E * ((abs(x_info[i] - x_info[j])**2) + (abs(y_info[i] - y_info[j])**2))
            info.append((new_val, i, j))
    #
    # print(x_info)
    # print(y_info)
    # print(info)

    info.sort()

    ans = 0
    for value, v1, v2 in info:
        if find_mama(v1) != find_mama(v2):
            family(v1, v2)
            ans += value
    real_ans = round(ans, 0)
    print(f'#{tc} {int(real_ans)}')
