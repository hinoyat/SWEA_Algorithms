T = int(input())
for _ in range(T):
    tc = int(input())
    g_lst = list(map(int, input().split()))
    g_n_lst = [0]*101
    for i in g_lst:
        g_n_lst[i] += 1
    v = max(g_n_lst)
    for j in range(len(g_n_lst)-1, -1, -1):
        if g_n_lst[j] == v:
            print(f'#{tc} {j}')
            break