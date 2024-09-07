'''

'''
# import sys
#
# sys.stdin = open("input.txt", "r")
def perm(lst):
    max_val = 0
    for i in range(len(lst)):
        sum_v = lst[i]
        sub_max_v = lst[i]**2
        for j in range(i+1, len(lst)):
            if sum_v + lst[j] <= C:
                sum_v += lst[j]
                sub_max_v += lst[j]**2
        if sub_max_v > max_val:
            max_val = sub_max_v
    return max_val




def supernova():
    info = []
    for i in range(N):
        for j in range(check_col):
            check_array = arr[i][j:j+M]
            check_array.sort(reverse=True)
            v_m = perm(check_array)
            info.append((i, j, v_m))
    return info


# 안녕안녕~~~ :)

T = int(input().strip())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())

    arr = [list(map(int, input().split()))for _ in range(N)]
    ans = 0
    check_col = N - M + 1
    # print(arr)
    info = supernova()
    info.sort(key=lambda x:x[2], reverse=True)
    # print(info)
    ans = -1
    for i in range(len(info)):
        sx, sy, sval = info[i]
        for j in range(i+1, len(info)):
            ex, ey, e_val = info[j]
            if sx == ex:
                if sy + M <= ey:
                    if sval + e_val > ans:
                        ans = sval + e_val

            else:
                if sval + e_val > ans:
                    ans = sval + e_val


    print(f'#{tc} {ans}')
