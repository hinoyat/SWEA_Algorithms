T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]

    lst = [[] for _ in range(n)]
    # print(lst)
    # print(arr)
    for i in range(n):
        for j in range(n):
            if arr[j][i] != 0:
                lst[i].append(arr[j][i])
    # print(lst)

    cnt = 0
    for d in lst:
        for s in range(len(d) - 1):
            if d[s] == 1 and d[s+1] == 2:
                cnt +=1

    print(f'#{tc} {cnt}')
