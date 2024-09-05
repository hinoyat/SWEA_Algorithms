# from pprint import pprint
# from collections import deque

# def BFS(start):
#     visited = [[-1]*N for _ in range(N)]
#     max_len = 0
#     r = 1
#     que = deque()
#     si, sj = start
#     cur_high = arr[si][sj]
#     que.append([si, sj])
#     visited[si][sj] = 1
#     while que:
#         qi, qj = que.pop()
#         max_way = 0
#         for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#             ni = qi + di
#             nj = qj + dj
#             if 0<= ni < N and 0<= nj < N and arr[ni][nj] <= arr[qi][qj] and visited[ni][nj] == -1:
#                 if arr[ni][nj] > max_way:
#                     max_way = arr[ni][nj]

#         for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#             ni = qi + di
#             nj = qj + dj
#             if 0<= ni < N and 0<= nj < N and arr[ni][nj] <= cur_high and visited[ni][nj] == -1 and arr[ni][nj] == max_way:
#                 if arr[ni][nj] == cur_high:
#                     cur_high -= 1
#                     visited[ni][nj] = visited[qi][qj] + 1
#                     que.append([ni, nj])
#                 else:
#                     cur_high = arr[ni][nj]
#                     visited[ni][nj] = visited[qi][qj] + 1
#                     que.append([ni, nj])
#                     if visited[ni][nj] > max_len:
#                         max_len = visited[ni][nj]
#                 r += 1

#     return visited




# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]

#     max_v = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > max_v:
#                 max_v = arr[i][j]

#     st_p = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == max_v:
#                 st_p.append([i,j])

#     result = []
#     for r in st_p:
#         result.append(BFS(r))

#     pprint(result)




# #######################
# def dfs(i, j, height, length, k_used):
#     global max_length
    
#     max_length = max(max_length, length)
    
#     for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
#         ni, nj = i + di, j + dj
#         if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited:
#             if arr[ni][nj] < height:
#                 visited.add((ni, nj))
#                 dfs(ni, nj, arr[ni][nj], length + 1, k_used)
#                 visited.remove((ni, nj))
#             elif not k_used and arr[ni][nj] - K < height:
#                 visited.add((ni, nj))
#                 dfs(ni, nj, height - 1, length + 1, True)
#                 visited.remove((ni, nj))

# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
    
#     max_height = max(max(row) for row in arr)
#     max_length = 0
    
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == max_height:
#                 visited = set([(i, j)])
#                 dfs(i, j, arr[i][j], 1, False)
    
#     print(f'#{tc} {max_length}')




# ######################
# def DFS(i, j, max_v, len, visit):
#     global max_len
#
#     if len > max_len:
#         max_len = len
#
#     for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#         ni = i + di
#         nj = j + dj
#
#     pass
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > max_v:
#                 max_v = arr[i][j]
#
#     max_len = 0
#
#     start_len = 1
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == max_v:
#                 visited = [[0] * N for _ in range(N)]
#                 DFS(i, j, max_v, start_len, 1)


# def DFS(i, j, cur_h, cur_len, visit):
#     global max_len
#
#     visited[i][j] = 1
#
#
#     if cur_len > max_len:
#         max_len = cur_len
#
#     for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#         ni = i + di
#         nj = j + dj
#
#         if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
#             if arr[ni][nj] < 0: continue
#             if arr[ni][nj] < cur_h:
#                 visited[ni][nj] = 1
#                 DFS(ni, nj, arr[ni][nj], cur_len + 1, visit)
#                 visited[ni][nj] = 0
#             elif arr[ni][nj] - K < cur_h and visit == 0:
#                 visited[ni][nj] = 1
#                 DFS(ni, nj, cur_h - 1, cur_len + 1, 1)
#                 visited[ni][nj] = 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > max_v:
#                 max_v = arr[i][j]
#
#     max_len = 0
#
#     start_len = 1
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == max_v:
#                 visited = [[0] * N for _ in range(N)]
#                 DFS(i, j, max_v, start_len, 0)
#
#     print(f'#{tc} {max_len}')


# si, sj - 현재 지점 cnt - 등산로 길이, cur 현재 높이, pos 깎은지 안 깎은지의 flag
def supernova(si, sj, cnt, cur, pos):
    global max_len

    max_len = max(cnt, max_len)

    for di, dj in ((0,1), (1, 0), (-1, 0), (0, -1)):
        ni = si + di
        nj = sj + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            if arr[ni][nj] < cur:
                visited[ni][nj] = 1
                supernova(ni, nj, cnt + 1, arr[ni][nj], pos)
                visited[ni][nj] = 0
            elif arr[ni][nj] - K < cur and pos == 0:
                visited[ni][nj] = 1
                supernova(ni, nj, cnt + 1, cur - 1, 1)
                visited[ni][nj] = 0




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] > max_v:
                max_v = arr[i][j]

    max_len = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_v:
                visited = [[0]*N for _ in range(N)]
                visited[i][j] = 1
                supernova(i, j, 1, max_v, 0)

    print(f'#{tc} {max_len}')
