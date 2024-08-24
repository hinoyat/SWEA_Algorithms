T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _  in range(100)]
    
    max_val = 0


    for i in range(100):
        sum_row = 0
        sum_col = 0
        for j in range(100):
            sum_row += arr[i][j]
            sum_col += arr[j][i]
        if sum_row > max_val:
            max_val = sum_row
        if sum_col > max_val:
            max_val = sum_col

    sum_rd = 0
    sum_ld = 0

    for i in range(100):
        for j in range(100):
            if i == j:
                sum_rd += arr[i][j]
            if 100-i-1 == j:
                sum_ld += arr[i][j]
    
    if sum_rd > max_val:
        max_val = sum_rd
    if sum_ld > max_val:
        max_val = sum_ld

    print(f'#{tc} {max_val}')