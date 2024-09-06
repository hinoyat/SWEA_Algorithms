# import pprint
# import copy
#
# def check(arrch):
#
#     newarr = list(zip(*arrch[:]))
#     # for i in range(len(newarr)):
#     #     newarr[i] = list(newarr[i])
#
#     for i in range(W):
#         cnt = 0
#         idx = 0
#         co = 0
#         cz = 0
#         while idx < D:
#             if newarr[i][idx] == 1:
#                 cz = 0
#                 co += 1
#             else:
#                 co = 0
#                 cz += 1
#             if co >= K or cz >= K:
#                 cnt += 1
#                 break
#             idx += 1
#
#         if cnt == 0:
#             return False
#
#     return True
#
# def change(arrc1, idx):
#     new_arr1 = arrc1[:]
#     new_arr1[idx] = [0] * W
#
#     return new_arr1
#
# def change2(arrc2, idx):
#     new_arr2 = arrc2[:]
#     new_arr2[idx] = [1] * W
#
#     return new_arr2
#
#
# def supernova(cnt, level, arr):
#     global ans
#     # print(cnt)
#
#     if cnt >= ans:
#         return
#
#     if level == D:
#         if check(arr):
#             ans = min(cnt, ans)
#         return
#     # print(cnt)
#
#     if check(arr):
#         ans = min(cnt, ans)
#         return
#     else:
#         supernova(cnt, level + 1, arr)
#
#         # check_arr = copy.deepcopy(arr)
#         # c1 = change(check_arr, level)
#         supernova(cnt + 1, level + 1, change(arr, level))
#
#         # check_arr2 = copy.deepcopy(arr)
#         # c2 = change2(check_arr2, level)
#         supernova(cnt + 1, level + 1, change2(arr, level))
#
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     # D 세로 W 가로 K 합격 기준
#     D, W, K = map(int, input().split())
#     # 특성 A = 0 특성 B = 0
#     arrs = [list(map(int, input().split())) for _ in range(D)]
#     # pprint.pprint(arr)
#
#     ans = 21e8
#     supernova(0, 0, arrs)
#     print(f'#{tc} {ans}')
#     # 배열 회전 세로 W 가로 D
#
#



#
import copy

def check(arrch):

    # newarr = list(zip(*arrch[:]))
    # for i in range(len(newarr)):
    #     newarr[i] = list(newarr[i])
    row = 0
    while row < W:
        cnt = 0
        idx = 0
        co = 0
        cz = 0
        while idx < D:
            if arrch[idx][row] == 1:
                cz = 0
                co += 1
            else:
                co = 0
                cz += 1
            if co >= K or cz >= K:
                cnt += 1
                break
            idx += 1

        if cnt == 0:
            return False
        row += 1

    return True

def change(arrc1, idx):
    new_arr1 = arrc1.copy()
    new_arr1[idx] = [0] * W

    return new_arr1

def change2(arrc2, idx):
    new_arr2 = arrc2[:]
    new_arr2[idx] = [1] * W

    return new_arr2


def supernova(cnt, level, arr):
    global ans
    # print(cnt)

    if cnt >= ans:
        return

    if level == D:
        if check(arr):
            ans = min(cnt, ans)
        return
    # print(cnt)

    if check(arr):
        ans = min(cnt, ans)
        return
    else:
        supernova(cnt, level + 1, arr)

        # check_arr = copy.deepcopy(arr)
        # c1 = change(check_arr, level)
        supernova(cnt + 1, level + 1, change(arr, level))

        # check_arr2 = copy.deepcopy(arr)
        # c2 = change2(check_arr2, level)
        supernova(cnt + 1, level + 1, change2(arr, level))




T = int(input())
for tc in range(1, T+1):
    # D 세로 W 가로 K 합격 기준
    D, W, K = map(int, input().split())
    # 특성 A = 0 특성 B = 0
    arrs = [list(map(int, input().split())) for _ in range(D)]
    # pprint.pprint(arr)

    ans = 21e8
    supernova(0, 0, arrs)
    print(f'#{tc} {ans}')
    # 배열 회전 세로 W 가로 D



