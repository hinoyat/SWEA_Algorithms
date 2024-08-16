t = int(input())

for tc in range(1, t+1):
    N = int(input())
    num = list(map(int, input().split()))
    # print(num)

    # max_c = 0
    # cur_num = 0
    # for i in range(N):
    #     cnt = 1
    #     cur_num = num[i]
    #     for j in range(N):
    #         if j > i:
    #             if num[j] > cur_num:
    #                 cnt += 1
    #                 cur_num = num[j]
    #     if cnt >= max_c:
    #         max_c = cnt
    #
    # print(f'#{tc} {max_c}')

    max_v = 1
    cnt = 1
    for i in range(N-1):
        if num[i] < num[i+1]:
            cnt += 1
            if cnt > max_v:
                max_v = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_v}')