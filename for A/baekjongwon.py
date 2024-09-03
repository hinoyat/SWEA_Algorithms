def supernova(idx, cnt):
    global ans

    if cnt == menu:
        # print(visited)
        result1 = 0
        result2 = 0
        lst = []
        lst2 = []
        for i in range(N):
            if visited[i] == 1:
                lst.append(i)
            else:
                lst2.append(i)

        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                result1 += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]

        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                result2 += arr[lst2[i]][lst2[j]] + arr[lst2[j]][lst2[i]]

        ans = min(ans, abs(result1 - result2))

        return

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            supernova(i + 1, cnt + 1)
            visited[i] = 0


T = int(input().strip())
for tc in range(1, T+1):
    ans = 21e8
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    menu = N//2
    visited = [0] * N
    visited[0] = 1
    supernova(1, 1)
    print(f'#{tc} {ans}')
