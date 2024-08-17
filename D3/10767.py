T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0 for _ in range(N)]for _ in range(N)]

    # 기본 돌 배치해주기
    arr[N//2-1][N//2-1] = 2
    arr[N//2][N//2] = 2
    arr[N//2-1][N//2] = 1
    arr[N//2][N//2-1] = 1
    # print(arr)

    di = [0, 1, 1,  1,  0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1,  0,  1]
    for game in range(M):
        #돌 위치, 색
        gi, gj, rock = map(int, input().split())
        # 문제가 돌 위치를 인덱스보다 1씩 크게 줍니다
        gi -= 1
        gj -= 1
        # 내 돌 놓기
        arr[gi][gj] = rock
        # 바꿀 인덱스를 담아줄 바구니
        change = []
        for d in range(8):
            # 바꾸기 전에 임시로 담아둘 바구니
            change_can = []
            # 내 돌이 끝에 있는지 확인할
            my_cnt = 0
            # 상대 돌이 있는지;
            other_cnt = 0
            for j in range(1, N):
                newi = gi + di[d] * j
                newj = gj + dj[d] * j
                if 0 <= newi < N and 0<= newj < N:
                    # 이거 0인 칸도 내 돌로 만들어서 자꾸 틀렸어요
                    # 확실하게 설계 안 하고 들어간 잘못
                    # 0 보이면 브레이크
                    if arr[newi][newj] == 0:
                        break
                    # 일단 상대 돌 보이면 무작정 담기
                    if arr[newi][newj] != rock:
                        other_cnt +=1
                        change_can.append([newi, newj])
                    # 내 돌을 만나면 내 돌이 있다 체크하고 컷
                    if arr[newi][newj] == rock:
                        if other_cnt > 0:
                            my_cnt += 1
                            break
                        else:
                            break

            # 바뀌는지 확인해보기
            # 둘다 1 이상이면 진짜 바꿀 돌의 위치를 담기
            if my_cnt > 0 and other_cnt > 0:
                for c in change_can:
                    change.append(c)

        for i, j in change:
            arr[i][j] = rock
        # pprint(arr)
    black = 0
    white = 0
    for s in arr:
        black += s.count(1)
        white += s.count(2)
    
    print(f'#{tc} {black} {white}')