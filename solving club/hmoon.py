T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _  in range(100)]

    arr2 = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            arr2[j][100-1-i] = arr[i][j]
    
    max_len = 0
    for i in range(100):
        for j in range(100):
            check_j = 1
            while j + check_j<=100:
                if arr[i][j:j+check_j] == arr[i][j:j+check_j][::-1]:
                    if check_j > max_len:
                        max_len = check_j
                if arr2[i][j:j+check_j] == arr2[i][j:j+check_j][::-1]:
                    if check_j > max_len:
                        max_len = check_j

                check_j +=1



    
    print(f'#{tc} {max_len}')