#
#
# from collections import deque
# def supernova(A_group, B_group, total_move, A_cnt, B_cnt, level):
#     global min_move
#     global ans
#
#     if level == num_people:
#         total_time = 0
#         # A 그룹 처리
#         if A_group:
#             A_group.sort()
#             idx = 0
#             cnt = 0
#             while A_group != [0] * len(A_group):
#                 if A_group[idx] > 0:
#                     A_group[idx] -= 1
#                     cnt += 1
#                     if cnt >= 3:
#                         idx = 0
#                         cnt = 0
#                         total_time += 1
#                 idx += 1
#                 if idx >= len(A_group):
#                     idx = 0
#         if B_group:
#             B_group.sort()
#             idx = 0
#             cnt = 0
#             while B_group != [0] * len(B_group):
#                 if B_group[idx] > 0:
#                     B_group[idx] -= 1
#                     cnt += 1
#                     if cnt >= 3:
#                         idx = 0
#                         cnt = 0
#                         total_time += 1
#                 idx += 1
#                 if idx >= len(B_group):
#                     idx = 0
#         print(A_group, B_group)
#         print(total_time)
#         ans = min(total_time, ans)
#
#
#
#         return
#
#     A = abs(people[level][0] - stair1[0]) + abs(people[level][1] - stair1[1])
#     supernova(A_group + [A], B_group, total_move + A, A_cnt + 1, B_cnt, level + 1)
#     B = abs(people[level][0] - stair2[0]) + abs(people[level][1] - stair2[1])
#     supernova(A_group, B_group + [B], total_move + B, A_cnt, B_cnt + 1, level + 1)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     people = []
#
#
#     stairs = []
#
#     min_move = 1000000
#
#     ans = 10000000
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:continue
#
#             if arr[i][j] == 1:
#                 people.append([i,j])
#             else:
#                 stairs.append([i,j])
#
#     num_people = len(people)
#     stair1 = [stairs[0][0], stairs[0][1]]
#     stair2 = [stairs[1][0], stairs[1][1]]
#     supernova([], [], 0, 0, 0, 0)
#     # print(num_people)
#     # print(min_move)
#     # print(people)
#     # print(stairs)
#     print(ans)





#
#
# from collections import deque
# def supernova(A_group, B_group, total_move, A_cnt, B_cnt, level):
#     global min_move
#     global ans
#
#     if level == num_people:
#         total_time = 0
#         # A 그룹 처리
#         if A_group:
#             A_group.sort()
#             idx = 0
#             cnt = 0
#             while A_group != [0] * len(A_group):
#                 if A_group[idx] > 0:
#                     A_group[idx] -= 1
#                     cnt += 1
#                     if cnt >= 3:
#                         idx = 0
#                         cnt = 0
#                         total_time += 1
#                 idx += 1
#                 if idx >= len(A_group):
#                     idx = 0
#         if B_group:
#             B_group.sort()
#             idx = 0
#             cnt = 0
#             while B_group != [0] * len(B_group):
#                 if B_group[idx] > 0:
#                     B_group[idx] -= 1
#                     cnt += 1
#                     if cnt >= 3:
#                         idx = 0
#                         cnt = 0
#                         total_time += 1
#                 idx += 1
#                 if idx >= len(B_group):
#                     idx = 0
#         print(A_group, B_group)
#         print(total_time)
#         ans = min(total_time, ans)
#
#
#
#         return
#
#     A = abs(people[level][0] - stair1[0]) + abs(people[level][1] - stair1[1])
#     supernova(A_group + [A], B_group, total_move + A, A_cnt + 1, B_cnt, level + 1)
#     B = abs(people[level][0] - stair2[0]) + abs(people[level][1] - stair2[1])
#     supernova(A_group, B_group + [B], total_move + B, A_cnt, B_cnt + 1, level + 1)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     people = []
#
#
#     stairs = []
#
#     min_move = 1000000
#
#     ans = 10000000
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 0:continue
#
#             if arr[i][j] == 1:
#                 people.append([i,j])
#             else:
#                 stairs.append([i,j])
#
#     num_people = len(people)
#     stair1 = [stairs[0][0], stairs[0][1]]
#     stair2 = [stairs[1][0], stairs[1][1]]
#     supernova([], [], 0, 0, 0, 0)
#     # print(num_people)
#     # print(min_move)
#     # print(people)
#     # print(stairs)
#     print(ans)





from collections import deque
def supernova(A_group, B_group, total_move, A_cnt, B_cnt, level):
    global min_move
    global ans

    if level == num_people:
        A_group.sort()
        B_group.sort()
        a_q = deque(A_group)
        b_q = deque(B_group)
        t = 0

        a_stair = [0] * 3
        b_stair = [0] * 3
        while True:
            for idx in range(3):
                if a_stair[idx] != 0:
                    a_stair[idx] -= 1
            for idx in range(3):
                if b_stair[idx] != 0:
                    b_stair[idx] -= 1

            for sidx in range(3):
                if a_q and a_q[0] <= t and a_stair[sidx] == 0:
                    poped = a_q.popleft()
                    if poped == t:
                        a_stair[sidx] = arr[stair1[0]][stair1[1]] + 1
                    else:
                        a_stair[sidx] = arr[stair1[0]][stair1[1]]
                if b_q and b_q[0] <= t and b_stair[sidx] == 0:
                    poped = b_q.popleft()
                    if poped == t:
                        b_stair[sidx] = arr[stair2[0]][stair2[1]] + 1
                    else:
                        b_stair[sidx] = arr[stair2[0]][stair2[1]]
            t += 1
            if not a_q and not b_q and sum(a_stair) == 0 and sum(b_stair) == 0:
                break
            if t >= ans:
                break

        ans = min(t, ans)
        return

    A = abs(people[level][0] - stair1[0]) + abs(people[level][1] - stair1[1])
    supernova(A_group + [A], B_group, total_move + A, A_cnt + 1, B_cnt, level + 1)
    B = abs(people[level][0] - stair2[0]) + abs(people[level][1] - stair2[1])
    supernova(A_group, B_group + [B], total_move + B, A_cnt, B_cnt + 1, level + 1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    people = []


    stairs = []

    min_move = 1000000

    ans = 10000000

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:continue

            if arr[i][j] == 1:
                people.append([i,j])
            else:
                stairs.append([i,j])

    num_people = len(people)
    stair1 = [stairs[0][0], stairs[0][1]]
    stair2 = [stairs[1][0], stairs[1][1]]
    supernova([], [], 0, 0, 0, 0)
    # print(num_people)
    # print(min_move)
    # print(people)
    # print(stairs)
    print(f'#{tc} {ans - 1}')
