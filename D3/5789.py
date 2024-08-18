T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lst = [0 for _ in range(N+1)]
    for i in range(1, Q+1):
        s, e = map(int, input().split())
        for j in range(s, e+1):
            lst[j] = i

    lst.pop(0)
    print(f'#{tc}', end=' ')
    print(*lst)