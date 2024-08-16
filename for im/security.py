from pprint import pprint
test = int(input())
for tc in range(test):
    N = int(input())
    city = []
    for _ in range(N):
        user_input = input()
        city.append([item for item in user_input])

    check = [[0]*N for _ in range(N)]
    direc = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    cnt = 0
    home_cnt = 0
    for i in range(N):
        for j in range(N):
            # city[i][j] 도착
            check[i][j] = 1
            pprint(city)
            pprint(check)
            print(cnt)
            if city[i][j] == 'A':
                for dx, dy in direc:
                    move_r = i + dx
                    move_c = j + dy
                    if 0 <= move_r < N and 0 <= move_c < N and check[move_r][move_c] == 0:
                        check[move_r][move_c] = 1
                        if city[move_r][move_c] == 'H':
                            cnt += 1
            elif city[i][j] == 'B':
                for dx, dy in direc:
                    for l in range(1, 3):
                        move_r = i + dx*l
                        move_c = j + dy*l
                        if 0 <= move_r < N and 0 <= move_c < N and check[move_r][move_c] == 0:
                            check[move_r][move_c] = 1
                            if city[move_r][move_c] == 'H':
                                cnt += 1
            elif city[i][j] == 'C':
                for dx, dy in direc:
                    for l in range(1, 4):
                        move_r = i + dx*l
                        move_c = j + dy*l
                        if 0 <= move_r < N and 0 <= move_c < N and check[move_r][move_c] == 0:
                            check[move_r][move_c] = 1
                            if city[move_r][move_c] == 'H':
                                cnt += 1
            elif city[i][j] == 'H':
                home_cnt += 1
    print(home_cnt)
    print(cnt)
    # print(f'#{tc+1} {home_cnt - cnt}')