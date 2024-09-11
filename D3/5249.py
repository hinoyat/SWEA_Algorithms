import heapq
def find_mama(p):
    if p != parent[p]:
        parent[p] = find_mama(parent[p])

    return parent[p]


def make_family(a, b):
    a = find_mama(a)
    b = find_mama(b)

    if a == b:
        return

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    parent = [i for i in range(N + 1)]
    graph = []
    for _ in range(E):
        v1, v2, value = map(int, input().split())
        graph.append((value, v1, v2))

    graph.sort()
    ans = 0

    for value, v1, v2 in graph:
        if find_mama(v1) != find_mama(v2):
            make_family(v1, v2)
            ans += value

    print(f'#{tc} {ans}')