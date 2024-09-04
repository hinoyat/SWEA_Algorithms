def supernova(gas, cnt, cur):
    global ans

    if cnt > ans:
        return
    # print(gas, cnt, cur)
    if gas < 0:
        return

    if arr[cur] == -1:
        ans = min(ans, cnt)
        return

    supernova(gas - 1, cnt, cur + 1)
    supernova(arr[cur] - 1, cnt + 1, cur + 1)


T = int(input())
for tc in range(1, T+1):

    arr = list(map(int, input().split())) + [-1]
    # print(arr)
    end_p = len(arr)
    start_gas = arr[1]

    ans = 0xffffff

    supernova(start_gas, 0, 1)

    print(f'#{tc} {ans}')

