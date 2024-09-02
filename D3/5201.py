T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    ans = 0
    take = [0] * N
    take2 = [0] * M
    container.sort(reverse=True)
    truck.sort(reverse=True)
    cnt = 0

    for i in range(M):
        for j in range(N):
            if take[j] == 0 and take2[i] == 0 and truck[i] >= container[j]:
                take[j] = 1
                take2[i] = 1
                cnt += 1
                ans += container[j]
            if cnt == min(M, N):
                break
        if cnt == min(M, N):
            break

    print(f'#{tc} {ans}')
