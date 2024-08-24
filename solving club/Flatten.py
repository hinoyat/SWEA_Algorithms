T = 10
for tc in range(1, T+1):
    dump = int(input())
    lst = list(map(int, input().split()))

    for d in range(dump):

        max_box = -21
        min_box = 21e8

        max_idx = 0
        min_idx = 0
        for i in range(len(lst)):
            if lst[i] > max_box:
                max_box = lst[i]
                max_idx = i
            if lst[i] < min_box:
                min_box = lst[i]
                min_idx = i
        lst[max_idx] -= 1
        lst[min_idx] += 1
    print(f'#{tc} {max(lst) - min(lst)}')