def move(point, info, N):
    direct = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}

    ai, aj = direct[info[1]]
    
    ni = point[0] + ai
    nj = point[1] + aj
    nn = info[0]
    nd = info[1]
    if ni == 0 and nd == 1:
        nd = 2
        nn //= 2
    elif ni == N-1 and nd == 2:
        nd = 1
        nn //= 2
    elif nj == 0 and nd == 3:
        nd = 4
        nn //= 2
    elif nj == N-1 and nd == 4:
        nd = 3
        nn //= 2
    # print(ni, nj, nn, nd)
    return [ni, nj, nn, nd]

def sum_m(info):

    max_dir = 0
    max_val = 0
    sum_v = 0
    # print(info)
    for i in range(0, len(info), 2):
        m = info[i]
        d = info[i+1]
        if m > max_val:
            max_val = m
            max_dir = d

    for j in range(0, len(info), 2):
        m = info[j]
        sum_v += m
    
    return [sum_v, max_dir]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    misang = {}
    for i in range(K):
        mi, mj, n, d = map(int, input().split())
        misang[(mi, mj)] = [n, d]

    for _ in range(M):
        newmisang = {}
        for j in list(misang.keys()): 
            ni, nj, nn, nd = move(j, misang[j], N)
            if nn > 0:
                if (ni, nj) in newmisang.keys():
                    newmisang[(ni, nj)].append(nn)
                    newmisang[(ni, nj)].append(nd)

                else:
                    newmisang[(ni, nj)] = [nn, nd]
        # print(newmisang)
        
        for m in list(newmisang.keys()):
            if len(newmisang[m]) > 2:
                r = sum_m(newmisang[m])
                newmisang[m] = r

        misang = newmisang

    result = 0
    for i in list(misang.keys()):
        result += misang[i][0]

    print(f'#{tc} {result}')
