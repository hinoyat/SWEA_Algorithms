def arr_maker(arr):
    arr2 = [[0] * col for _ in range(row)]
    for i in range(col):
        for j in range(row):
            arr2[j][col-1-i] = arr[i][j]
    return arr2



T = int(input())
for tc in range(1, T+1):
    col, row = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(col)]
    arr2 = arr_maker(arr)

    max_l = 0
    for i in range(col):
        cnt = 0
        for j in range(row):
            if arr[i][j] == 1:
                cnt +=1
                if cnt > max_l:
                    max_l = cnt
            else:
                cnt = 0

    for i in range(row):
        cnt = 0
        for j in range(col):
            