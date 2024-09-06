def supernova(idx, val, kcal_val, remaintaste):
    global ans
    if kcal_val > K:
        return

    if idx == N:
        ans = max(val, ans)
        return

    if val + remaintaste < ans:
        return

    supernova(idx + 1, val + info[idx][0], kcal_val + info[idx][1], remaintaste - info[idx][0])
    supernova(idx + 1, val, kcal_val, remaintaste - info[idx][0])



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    info = []
    total_taste = 0

    ans = 0

    for i in range(N):
        taste, kcal =map(int,input().split())
        info.append([taste, kcal])
        total_taste += taste

    supernova(0, 0, 0, total_taste)
    print(f'#{tc} {ans}')
