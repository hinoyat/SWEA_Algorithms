# from pprint import pprint
# G = {'A':1, 'B':2, 'C':3}
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     arr = [list(input()) for _ in range(n)]
#     # pprint(arr)

#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]

#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] in G:
#                 for s in range(1, G[arr[i][j]]+1):
#                     for d in range(4):
#                         newi = i + di[d] * s
#                         newj = j + dj[d] * s
#                         if 0<=newi<n and 0<=newj<n and arr[newi][newj] == 'H':
#                             arr[newi][newj] = 'O'
#     # pprint(arr)
#     cnt  = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 'H':
#                 cnt += 1
#     print(f'#{tc} {cnt}')

## 메모리 줄이기

G = {'A':1, 'B':2, 'C':3}
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] in G:
                for s in range(1, G[arr[i][j]]+1):
                    for d in range(4):
                        newi = i + di[d] * s
                        newj = j + dj[d] * s
                        if 0<=newi<n and 0<=newj<n and arr[newi][newj] == 'H':
                            arr[newi][newj] = 'O'
    cnt  = 0
    for i in arr:
        cnt += i.count('H')
    print(f'#{tc} {cnt}')