def supernova(level, value):
    global max_ans, min_ans
    if level == N :
        max_ans = max(max_ans, value)
        min_ans = min(min_ans, value)
        return

    for idx in range(order_len):
        if order[idx] > 0:
            order[idx] -= 1
            if idx == 0:
                supernova(level + 1, value + num[level])
            if idx == 1:
                supernova(level + 1, value - num[level])
            if idx == 2:
                supernova(level + 1, value * num[level])
            if idx == 3:
                supernova(level + 1, int(value / num[level]))
            order[idx] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order = list(map(int, input().split()))
    num = list(map(int, input().split()))
    order_len = 4
    max_ans = -0xffffff
    min_ans = 0xffffff
    supernova(1, num[0])
    print(f'#{tc} {max_ans - min_ans}')