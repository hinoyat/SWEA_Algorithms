# def check(arr):
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     for i in range(N):
#         for j in range(M):
#             for d in range(4):
#                 newi = i + di[d]
#                 newj = j + dj[d]
#                 if 0<=newi<N and 0<=newj<M:
#                     if arr[newi][newj] == arr[i][j]:
#                         return 'impossible'
#     return 'possible'

# 격자판 칠하기

# import copy
# def color():
#     ar1 = copy.deepcopy(arr)
#     c_lst = ['#','.']
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     # 첫행 칠하기
#     if ar1[0][0] != '?':
#         if M > 1:
#             for j in range(1, M):
#                 if ar1[0][j] == '?':
#                     if ar1[0][j-1] == '.':
#                         ar1[0][j] = '#'
#                     else:
#                         ar1[0][j] = '.'
#         # 나머지 칠하면서 확인하기 위에랑 다르게 색칠
#         if N >1:
#             for i in range(1, N):
#                 for j in range(M):
#                     if ar1[i][j] == '?':
#                         if ar1[i-1][j] == '.':
#                             ar1[i][j] = '#'
#                         else:
#                             ar1[i][j] = '.'
#         for i in range(N):
#             for j in range(M):
#                 for d in range(4):
#                     newi = i + di[d]
#                     newj = j + dj[d]
#                     if 0<=newi<N and 0<=newj<M:
#                         if ar1[newi][newj] == ar1[i][j]:
#                             return 'impossible'
#         return 'possible'
    

#     # 여기는 첫 칸이 ?일때
#     else:
#         flag = False
#         for c in c_lst:
#             ar1 = copy.deepcopy(arr)
#             ar1[0][0] = c
#             flag = True
#             if M > 1:
#                 for j in range(1, M):
#                     if ar1[0][j] == '?':
#                         if ar1[0][j-1] == '.':
#                             ar1[0][j] = '#'
#                         else:
#                             ar1[0][j] = '.'
#             # 나머지 칠하면서 확인하기 위에랑 다르게 색칠
#             if N >1:
#                 for i in range(1, N):
#                     for j in range(M):
#                         if ar1[i][j] == '?':
#                             if ar1[i-1][j] == '.':
#                                 ar1[i][j] = '#'
#                             else:
#                                 ar1[i][j] = '.'
            
#             for i in range(N):
#                 for j in range(M):
#                     for d in range(4):
#                         newi = i + di[d]
#                         newj = j + dj[d]
#                         if 0<=newi<N and 0<=newj<M:
#                             if ar1[newi][newj] == ar1[i][j]:
#                                 flag = False
#                                 break
#                     if flag == False:
#                         break
#                 if flag == False:
#                     break

#             if flag == True:
#                 return 'possible'

#         return 'impossible'
#             # 확인하기

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     print(f'#{tc} {color()}')

#     # 왼 오 위 아래 탐지하며 같지 않은 값을 대입



# 격자판 ver2
import copy
def color():
    ar1 = copy.deepcopy(arr)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 첫행 칠하기
    if ar1[0][0] != '?':
        if M > 1:
            for j in range(1, M):
                if ar1[0][j] == '?':
                    if ar1[0][j-1] == '.':
                        ar1[0][j] = '#'
                    else:
                        ar1[0][j] = '.'
        # 나머지 위에 보면서 다른 색으로 칠하기
        if N >1:
            for i in range(1, N):
                for j in range(M):
                    if ar1[i][j] == '?':
                        if ar1[i-1][j] == '.':
                            ar1[i][j] = '#'
                        else:
                            ar1[i][j] = '.'
        # 확인하기
        for i in range(N):
            for j in range(M):
                for d in range(4):
                    newi = i + di[d]
                    newj = j + dj[d]
                    if 0<=newi<N and 0<=newj<M:
                        if ar1[newi][newj] == ar1[i][j]:
                            return 'impossible'
        return 'possible'


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    c_lst = ['#','.']
    # 첫 칸이 물음표가 아닐 때
    if arr[0][0] != '?':
        print(f'#{tc} {color()}')
    else:
        # 물음표일 때 하나씩 채워보면서 확인하기
        result = []
        for c in c_lst:
            arr[0][0] = c
            r = color()
            result.append(r)
        if 'possible' in result:
            print(f'#{tc} possible')
        else:
            print(f'#{tc} impossible')


                    