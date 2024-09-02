
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work = [list(map(int, input().split()))for _ in range(N)]
    # print(work)
    work.sort(key=lambda x : x[1])
    # print(work)
    start = work[0][0]
    ans = 1
    for i in range(N-1):
        if work[i+1][0] < start:continue
        start = work[i+1][1]
        ans += 1
    print(f'#{tc} {ans}')
