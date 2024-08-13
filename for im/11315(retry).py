# # 오목 판정
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     word = [list(input()) for _ in range(N)]

#     possible = False

#     i = 0
#     j = 0
#     hang_cnt = 0
#     while i < N:
#         if word[i][j] == 'o':
#             hang_cnt +=1
#             if hang_cnt >= 5:
#                 possible = True
#                 break
#         else:
#             hang_cnt = 0
#         j += 1
#         if j >= N:
#             j = 0
#             i +=1


#     i = 0
#     j = 0
#     yeol_cnt = 0
#     while j < N:
#         if word[i][j] == 'o':
#             yeol_cnt +=1
#             if yeol_cnt >= 5:
#                 possible = True
#                 break
#         else:
#             yeol_cnt = 0
#         i += 1
#         if i >= N:
#             i = 0
#             j +=1



#     i = 0
#     j = 0
#     cnt = 0
#     while i < N and j < N:
#         if word[i][j] == 'o':
#             cnt += 1
#             di = i + 1
#             dj = j + 1
#             while di < N and dj < N:
#                 if word[di][dj] == 'o':
#                     cnt += 1
#                 else:
#                     cnt = 0
#                     break
#                 di += 1
#                 dj += 1
#             if cnt >= 5:
#                 possible = True
#                 break
#             cnt = 0
#         j += 1
#         if j >= N:
#             j = 0
#             i +=1 
            
#     i = 0
#     j = 0
#     cnt = 0
#     while i < N and j < N:
#         if word[i][j] == 'o':
#             cnt += 1
#             di = i + 1
#             dj = j - 1
#             while di < N and dj >= 0:
#                 if word[di][dj] == 'o':
#                     cnt += 1
#                 else:
#                     cnt = 0
#                     break
#                 di += 1
#                 dj -= 1
#             if cnt >= 5:
#                 possible = True
#                 break
#             cnt = 0
#         j += 1
#         if j >= N:
#             j = 0
#             i +=1 
            
        
#     print(f'#{tc}', end= ' ')
#     if possible == True:
#         print('YES')
#     else:
#         print('NO')


# # 오목 판정
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     word = [list(input()) for _ in range(N)]

#     possible = False

#     for i in range(N):
#         hang_cnt = 0
#         for j in range(N):
#             if word[i][j] == 'o':
#                 hang_cnt += 1
#                 if hang_cnt >= 5:
#                     possible = True
#                     break
#             else:
#                 hang_cnt = 0
#         if possible:
#             break

#     # 세로 검사
#     if not possible:
#         for j in range(N):
#             yeol_cnt = 0
#             for i in range(N):
#                 if word[i][j] == 'o':
#                     yeol_cnt += 1
#                     if yeol_cnt >= 5:
#                         possible = True
#                         break
#                 else:
#                     yeol_cnt = 0
#             if possible:
#                 break
#     if not possible:
#         for i in range(N):
#             for j in range(N):
#                 cnt = 0
#                 di, dj = i, j
#                 while di < N and dj < N:
#                     if word[di][dj] == 'o':
#                         cnt += 1
#                         if cnt >= 5:
#                             possible = True
#                             break
#                     else:
#                         cnt = 0
#                     di += 1
#                     dj += 1
#                 if possible:
#                     break
#             if possible:
#                 break

#     # 대각선 검사 (좌하향)
#     if not possible:
#         for i in range(N):
#             for j in range(N):
#                 cnt = 0
#                 di, dj = i, j
#                 while di < N and dj >= 0:
#                     if word[di][dj] == 'o':
#                         cnt += 1
#                         if cnt >= 5:
#                             possible = True
#                             break
#                     else:
#                         cnt = 0
#                     di += 1
#                     dj -= 1
#                 if possible:
#                     break
#             if possible:
#                 break
            
        
#     print(f'#{tc}', end= ' ')
#     if possible == True:
#         print('YES')
#     else:
#         print('NO')

# # 오목
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word = [list(input()) for _ in range(N)]

    possible = False

    # 가로 검사
    i = 0
    while i < N and not possible:
        j = 0
        hang_cnt = 0
        while j < N:
            if word[i][j] == 'o':
                hang_cnt += 1
                if hang_cnt >= 5:
                    possible = True
                    break
            else:
                hang_cnt = 0
            j += 1
        i += 1

    # 세로 검사
    j = 0
    while j < N and not possible:
        i = 0
        yeol_cnt = 0
        while i < N:
            if word[i][j] == 'o':
                yeol_cnt += 1
                if yeol_cnt >= 5:
                    possible = True
                    break
            else:
                yeol_cnt = 0
            i += 1
        j += 1

    # 대각선 검사 (우하향)
    i = 0
    while i < N and not possible:
        j = 0
        while j < N and not possible:
            di, dj = i, j
            cnt = 0
            while di < N and dj < N:
                if word[di][dj] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        possible = True
                        break
                else:
                    cnt = 0
                di += 1
                dj += 1
            j += 1
        i += 1

    # 대각선 검사 (좌하향)
    i = 0
    while i < N and not possible:
        j = 0
        while j < N and not possible:
            di, dj = i, j
            cnt = 0
            while di < N and dj >= 0:
                if word[di][dj] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        possible = True
                        break
                else:
                    cnt = 0
                di += 1
                dj -= 1
            j += 1
        i += 1

    print(f'#{tc}', end=' ')
    if possible:
        print('YES')
    else:
        print('NO')