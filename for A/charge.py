from pprint import pprint

def find(A, B):
    value = 0

    if not A and not B:
        return 0

    elif not A and B:
        max_v = 0
        for i in B:
            if BC_info[i] > max_v:
                max_v = BC_info[i]
        value += max_v
    elif A and not B:
        max_v = 0
        for i in A:
            if BC_info[i] > max_v:
                max_v = BC_info[i]
        value += max_v
    elif A and B:
        max_v = 0
        for i in A:
            for j in B:
                v = 0
                if i == j:
                    v += BC_info[i]
                else:
                    v += BC_info[i] + BC_info[j]
                if v > max_v:
                    max_v = v
        value += max_v
    return value

def move(i, j, d):
    ni = i + order[d][0]
    nj = j + order[d][1]
    return (ni, nj)


def solve(A, B):
    global ans

    val = 0

    ai, aj = A
    bi, bj = B

    val += find(arr[ai][aj], arr[bi][bj])

    for idx in range(M):
        a_order = A_info[idx]
        b_order = B_info[idx]
        ai, aj = move(ai, aj, a_order)
        bi, bj = move(bi, bj, b_order)
        v = find(arr[ai][aj], arr[bi][bj])
        val += v
        # print(bi, bj)
        # print(val)
    ans = max(ans, val)



T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())

    arr_array = 10

    arr = [[[] for _ in range(arr_array)] for _ in range(arr_array)]
    A_info = list(map(int, input().split()))
    B_info = list(map(int, input().split()))
    BC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


    BC_info = {}

    order = {0: (0, 0), 1:(-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}

    for bc_idx in range(N):
        bi, bj, ar, val = map(int, input().split())
        BC_info[BC[bc_idx]] = val

        bi -= 1
        bj -= 1

        for i in range(arr_array):
            for j in range(arr_array):
                if abs(i - bi) + abs(j - bj) <= ar:
                    arr[j][i].append(BC[bc_idx])


    ans = 0
    A_start = [0, 0]
    B_start = [9, 9]

    solve(A_start, B_start)

    print(f'#{tc} {ans}')
