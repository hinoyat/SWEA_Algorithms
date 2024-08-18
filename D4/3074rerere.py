T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [int(input()) for _ in range(N)]
    # print(lst)
    start = 1
    end = max(lst) * M
    time = 0
    while start <= end:
        mid = (start + end)//2
        people = 0
        for i in lst:
            people += mid//i
        
            if people >= M:
                break

        if people >= M:
            time = mid
            end = mid-1
        else:
            start = mid+1
    print(f'#{tc} {time}')