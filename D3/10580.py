T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        line = list(map(int, input().split()))
        lst.append(line)
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1
            elif lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]:
                cnt += 1
    print(f'#{tc} {cnt}')