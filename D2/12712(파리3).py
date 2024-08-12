from pprint import pprint


# 돌 뒤집기
# 


# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     pprint(arr)

#     # 가로 세로
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     max_fly = 0
#     for i in range(N):
#         for j in range(N):
#             sum_rc = 0
#             sum_rc += arr[i][j]
#             for s in range(1, M):
#                 for d in range(4):
#                     new_i = i + di[d] * s
#                     new_j = j + dj[d] * s
#                     if new_j < 0 or new_i < 0 or new_j >= N or new_i >= N:
#                         pass
#                     else:
#                         sum_rc += arr[new_i][new_j]

#             if max_fly < sum_rc:
#                 max_fly = sum_rc


#     di2 = [1, -1, 1, -1]
#     dj2 = [1, -1, -1, 1]
#     for i in range(N):
#         for j in range(N):
#             sum_rc = 0
#             sum_rc += arr[i][j]
#             for s in range(1, M):
#                 for d in range(4):
#                     new_i = i + di2[d] * s
#                     new_j = j + dj2[d] * s
#                     if new_j < 0 or new_i < 0 or new_j >= N or new_i >= N:
#                         pass
#                     else:
#                         sum_rc += arr[new_i][new_j]

#             if max_fly < sum_rc:
#                 max_fly = sum_rc
    


#     print(max_fly)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint( arr)

    # 가로 세로
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_fly = 0
    for i in range(N):
        for j in range(N):
            sum_rc = 0
            sum_rc += arr[i][j]
            for s in range(1, M):
                for d in range(4):
                    new_i = i + di[d] * s
                    new_j = j + dj[d] * s
                    if new_j < 0 or new_i < 0 or new_j >= N or new_i >= N:
                        pass
                    else:
                        sum_rc += arr[new_i][new_j]

            if max_fly < sum_rc:
                max_fly = sum_rc


    di2 = [1, -1, 1, -1]
    dj2 = [1, -1, -1, 1]
    for i in range(N):
        for j in range(N):
            sum_rc = 0
            sum_rc += arr[i][j]
            for s in range(1, M):
                for d in range(4):
                    new_i = i + di2[d] * s
                    new_j = j + dj2[d] * s
                    if new_j < 0 or new_i < 0 or new_j >= N or new_i >= N:
                        pass
                    else:
                        sum_rc += arr[new_i][new_j]

            if max_fly < sum_rc:
                max_fly = sum_rc
    


    print(f'#{tc} {max_fly}')
