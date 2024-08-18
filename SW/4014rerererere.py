T = int(input())
for tc in range(1, T+1):
    N, X = map(int,input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    print(arr)

    # 행 탐색
    pos = 0
    for i in range(N):
        hang_lst = [0] * 7
        for j in range(N):
            s = arr[i][j]
            hang_lst[s] += 1
        print(hang_lst)