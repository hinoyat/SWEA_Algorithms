def ladder2(i, j):
    dis = 0
    while i < 99:
        i += 1
        dis += 1
        if j == 0:
            if arr[i][j+1] == 1:
                while arr[i][j+1] ==1:
                    dis += 1
                    j +=1
                    if j == 99:
                        break
        elif j == 99:
            if arr[i][j-1] == 1:
                while arr[i][j-1] ==1:
                    dis += 1
                    j -=1
                    if j == 0:
                        break
        else:
            if arr[i][j-1] == 1:
                while arr[i][j-1] ==1:
                    dis += 1
                    j -=1
                    if j == 0:
                        break
            elif arr[i][j+1] == 1: 
                while arr[i][j+1] ==1:
                    dis += 1
                    j +=1
                    if j == 99:
                        break

    return dis


T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _  in range(100)]

    start_p = []
    for i in range(100):
        if arr[0][i] == 1:
            start_p.append([0,i])
    
    min_idx = 0
    min_dis = 21e8
    
    for pi, pj in start_p:
        r = ladder2(pi, pj)
        if r < min_dis:
            min_dis = r
            min_idx = pj

    print(f'#{tc} {min_idx}')