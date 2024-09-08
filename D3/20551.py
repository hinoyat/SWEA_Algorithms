def supernova(cnt, level, val):
    global ans
    if level == 0:
        ans = cnt
        return

    if lst[level] < 1:
        return


    if lst[level] <= lst[level - 1]:
        lst[level - 1] -= 1
        supernova(cnt + 1, level, val)
    else:
        supernova(cnt, level - 1, val)

T = int(input().strip())
for tc in range(1, T+1):
    ans = -1
    N = 3
    lst = list(map(int, input().split()))
    supernova(0, 2, 0)
    print(f'#{tc} {ans}')
