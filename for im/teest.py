def dfs(V, start, end):        # s 시작 정점, V 정점개수 (1번부터인 정점의 마지막 정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []
    stack.append(start)         # 시작 정점 방문표시
    # 스택 생성
    visited[start] = 1
    while stack:
        cur = stack.pop()
        if cur == end:
            return 1
        for j in lst[cur]:
            if not visited[j]:
                stack.append(j)
                visited[j] = 1
    return 0
 
 
test_case = 10
for _ in range(1, test_case+1):
    start = 0
    end = 99
    tc, len_lst = map(int, input().split())
    lst = [[] for _ in range(101)]
    # print(lst)
 
    in_lst = list(map(int, input().split()))
    for i in range(len_lst):
        v1, v2 = in_lst[i*2], in_lst[i*2+1]
        lst[v1].append(v2)
 
    # print(lst)
    result = dfs(100, start, end)
    print(f'#{tc} {result}')