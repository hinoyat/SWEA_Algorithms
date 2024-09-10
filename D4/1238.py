'''
24 2
2 7 11 6 6 2 2 15 15 4 4 2 4 10 7 1 1 7 1 8 1 17 3 22
'''

from collections import deque
def supernova(start):
    global ans
    que = deque()
    que.append(start)
    visited[start] = 1
    meet = []

    while que:
        q = que.popleft()
        meet.append(q)
        for p in graph[q]:
            if not visited[p]:
                visited[p] = visited[q] + 1
                que.append(p)

    return


T = 10
for tc in range(1, T+1):
    # 동시 전달, visited, 없는 사람 있다
    Data_len, start_point = map(int, input().split())

    max_people = 100

    info = list(map(int, input().split()))

    visited = [0] * (max_people + 1)

    graph = [[]for _ in range(max_people + 1)]

    for v in range(0, Data_len, 2):
        v1, v2 = info[v], info[v+1]
        graph[v1].append(v2)

    ans = 0
    
    r = supernova(start_point)

    check_val = max(visited)

    for i in range(100, -1, -1):
        if visited[i] == check_val:
            ans = i
            break
    print(f'#{tc} {i}')