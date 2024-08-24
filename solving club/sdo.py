def fact_check(arr):
    for i in range(9):
        hang = set()
        yolo = set()
        for j in range(9):
            hang.add(arr[i][j])
            yolo.add(arr[j][i])
        
        if len(hang) != 9:
            return 0
        
        if len(yolo) != 9:
            return 0
    
    kang_i = [0, 0, 0, 1, 1, 1, -1 -1, -1]
    kang_j = [0, -1, 1, 0, -1, 1, 0, -1, 1]
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            kang = set()
            for d in range(9):
                ni = i + kang_i[d]
                nj = j + kang_j[d]
                kang.add(arr[ni][nj])
            if len(kang) != 9:
                return 0
            
    return 1




T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _  in range(9)]
    a = fact_check(arr)
    print(f'#{tc} {a}')