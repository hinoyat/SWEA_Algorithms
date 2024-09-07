# # 방향전환
# def meetblock(i, j, dir, block):
#     if block == 1:
#         return wall1[dir][2]
#     if block == 2:
#         return wall2[dir][2]
#     if block == 3:
#         return wall3[dir][2]
#     if block == 4:
#         return wall4[dir][2]
#     if block == 5:
#         return wall5[dir][2]
#
# # 웜홀 처리
# def worm(i, j, d, num):
#     for si, sj in wormhole[num]:
#         if si != i or sj != j:
#             return (si, sj, d)
#
# # 움직이기
# # 종료 조건은 시작 지점과 끝 지점이 같아질 때 or blackhole 만났을 때
# def movingball(ssi, ssj, snd, starti, startj):
#     cnt = 0
#     si, sj, nd = ssi, ssj, snd
#     while True:
#         si = si + direc[nd][0]
#         sj = sj + direc[nd][1]
#
#         if 1<= arr[si][sj] <=5:
#             nd = meetblock(si, sj, nd, arr[si][sj])
#             cnt += 1
#             # print(nd)
#         elif arr[si][sj] > 5:
#             si, sj, nd = worm(si, sj, nd, arr[si][sj])
#             continue
#         if si == starti and sj==startj:
#             return cnt
#         if arr[si][sj] == -1:
#             return cnt
#
#         # print([si,sj])
#         if cnt > 50:
#             return 0
#
#
#
#
#
# import pprint
# from collections import defaultdict
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
#     # pprint.pprint(arr)
#
#     black = set()
#
#     wormhole = defaultdict(list)
#     direc = {1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
#     # 방향 1 위 2 오른쪽 3 아래 4 왼쪽
#     wall1 = {1: (1, 0, 3), 2:(0, -1, 4), 3:(0, 1, 2), 4:(-1, 0, 1)}
#     wall2 = {1: (0, 1, 2), 2:(0, -1, 4), 3:(-1, 0, 1), 4:(-1, 0, 2)}
#     wall3 = {1: (0, -1, 4), 2:(1, 0, 3), 3:(-1, 0, 1), 4:(0, 1, 2)}
#     wall4 = {1: (1, 0, 3), 2:(-1, 0, 1), 3:(0, -1, 4), 4:(0, 1, 2)}
#     wall5 = {1: (1, 0, 3), 2:(0, -1, 4), 3:(-1, 0, 1), 4:(0, 1, 2)}
#
#     for i in range(N+2):
#         for j in range(N+2):
#             if arr[i][j] == -1:
#                 black.add((i, j))
#             if arr[i][j] > 5:
#                 wormhole[arr[i][j]].append((i,j))
#
#     # print(wormhole)
#     max_v = -1
#     for i in range(N+2):
#         for j in range(N+2):
#             if arr[i][j] == 0:
#                 for s in range(1, 5):
#                     r = movingball(i, j, s, i, j)
#                     max_v = max(r, max_v)
#     print(f'#{tc} {max_v}')



# 방향전환

'''
1
4
6 5 5 5
0 5 5 5
6 5 5 5
5 5 5 5

1
4
0 0 0 3
0 0 0 0
1 0 0 4
0 0 0 0
'''
def meetblock(i, j, dir, block):
    if block == 1:
        return wall1[dir]
    if block == 2:
        return wall2[dir]
    if block == 3:
        return wall3[dir]
    if block == 4:
        return wall4[dir]
    if block == 5:
        return wall5[dir]

# 움직이기
# 종료 조건은 시작 지점과 끝 지점이 같아질 때 or blackhole 만났을 때
def movingball(ssi, ssj, nd, starti, startj):
    cnt = 0
    si, sj= ssi, ssj
    # print(si, sj, cnt)
    while True:
        si = si + direc[nd][0]
        sj = sj + direc[nd][1]

        if si == starti and sj==startj or arr[si][sj] == -1:
            return cnt
        if 1<= arr[si][sj] <=5:
            nd = meetblock(si, sj, nd, arr[si][sj])
            cnt += 1
            # print(nd)
        elif arr[si][sj] > 5:
            if (si, sj) == wormhole[arr[si][sj]][0]:
                si, sj = wormhole[arr[si][sj]][1]
            else:
                si, sj = wormhole[arr[si][sj]][0]

        # print([si,sj])
        # if cnt > 500:
        #     return 0
        # # print(si, sj, cnt)


from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[5] * (N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N+2)]
    # pprint.pprint(arr)

    black = set()

    wormhole = defaultdict(list)
    direc = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    # 방향 1 위 2 오른쪽 3 아래 4 왼쪽
    wall1 = {1: 2, 2: 4, 3: 1, 4: 3}
    wall2 = {1: 4, 2: 1, 3: 2, 4: 3}
    wall3 = {1: 3, 2: 1, 3: 4, 4: 2}
    wall4 = {1: 2, 2: 3, 3: 4, 4: 1}
    wall5 = {1: 2, 2: 1, 3: 4, 4: 3}

    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == -1:
                black.add((i, j))
            if arr[i][j] > 5:
                wormhole[arr[i][j]].append((i,j))

    # print(wormhole)
    max_v = 0
    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == 0:
                for s in range(1, 5):
                    r = movingball(i, j, s, i, j)
                    max_v = max(r, max_v)
    print(f'#{tc} {max_v}')
