def supernova(idx, level, val):
    global min_val
    global max_val


    # if tuple(lst) in check:
    #     return

    if level == N-1:
        min_val = min(val, min_val)
        max_val = max(val, max_val)
        return

    for i in range(4):
        if order[i] != 0:
            order[i] -= 1
            if i == 0:
                supernova(idx + 1, level + 1, val + num_lst[idx])
            if i == 1:
                supernova(idx + 1, level + 1, val - num_lst[idx])
            if i == 2:
                supernova(idx + 1, level + 1, val * num_lst[idx])
            if i == 3:
                supernova(idx + 1, level + 1, int(val / num_lst[idx]))
            order[i] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))

    dct = {0:'+', 1:'-', 2:'*', 3:'/'}

    max_val = -21e8
    min_val = 21e8

    visited = [0] * (N-1)

    supernova(1, 0, num_lst[0])
    print(f'#{tc} {max_val - min_val}')
