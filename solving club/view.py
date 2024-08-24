T = 10
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    sun = 0
    for i in range(2, n-2):
        max_val = 0
        sec_val = 0
        for j in lst[i-2:i+3]:
            if j > max_val:
                max_val = j
        for s in lst[i-2:i+3]:
            if s <= max_val and s >sec_val:
                sec_val = s

        if lst[i] == max_val:
            sun += max_val - sec_val

    print(f'#{tc} {sun}')