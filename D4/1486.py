def supernova(val, level, max_v):
    global min_v

    if level == N:
        if val < B:
            return
        min_v = min(val, min_v)
        return

    # 가지치기 1 - 남은 것을 다 더해도 B를 넘지 못할 때
    if val + max_v < B:
        return

    # 더하거나 더하지 않거나
    supernova(val + lst[level], level + 1, max_v - lst[level])
    supernova(val, level + 1, max_v - lst[level])



T = int(input().strip())
for tc in range(1, T+1):
    # N 점원의 수 # B 넘겨야 하는 탑의 높이
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    min_v = 0xffffff
    max_v = sum(lst)

    supernova(0, 0, max_v)

    result = min_v - B
    print(f'#{tc} {result}')