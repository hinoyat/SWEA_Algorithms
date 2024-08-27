def change(m, d):
    m -= 1
    change_d = [0, 0, 0, 0]
    change_d[m] = d
    
    
    if m == 0:
        change_d[1] = checkNS(1, change_d[0], m)
        change_d[2] = checkNS(2, change_d[1], m)
        change_d[3] = checkNS(3, change_d[2], m)
    if m == 1:
        change_d[0] = checkNS(0, change_d[1], m)
        change_d[2] = checkNS(2, change_d[1], m)
        change_d[3] = checkNS(3, change_d[2], m)
    if m == 2:
        change_d[3] = checkNS(3, change_d[2], m)
        change_d[1] = checkNS(1, change_d[2], m)
        change_d[0] = checkNS(0, change_d[1], m)
    if m == 3:
        change_d[2] = checkNS(2, change_d[3], m)
        change_d[1] = checkNS(1, change_d[2], m)
        change_d[0] = checkNS(0, change_d[1], m)

    return change_d




def checkNS(idx, dir, m):
    if dir == 0:
        return 0
    else:
        if idx == 0:
            if arr[idx][2] != arr[idx+1][6]:
                if dir == -1:
                    return 1
                elif dir == 1:
                    return -1
                else:
                    return 0
            else:
                return 0

        if idx == 1:
            if m ==2 or m==3:
                if arr[idx][2] != arr[idx+1][6]:
                    if dir == -1:
                        return 1
                    elif dir == 1:
                        return -1
                    else:
                        return 0
                else:
                    return 0
            elif m == 0:
                if arr[idx-1][2] != arr[idx][6]:
                    if dir == -1:
                        return 1
                    elif dir == 1:
                        return -1
                    else:
                        return 0
                else:
                    return 0


        if idx == 2:
            if m == 0 or m == 1:
                if arr[idx-1][2] != arr[idx][6]:
                    if dir == -1:
                        return 1
                    elif dir == 1:
                        return -1
                    else:
                        return 0
                else:
                    return 0
                
            elif m == 3:
                if arr[idx][2] != arr[idx+1][6]:
                    if dir == -1:
                        return 1
                    elif dir == 1:
                        return -1
                    else:
                        return 0
                else:
                    return 0


        if idx == 3:
            if arr[idx-1][2] != arr[idx][6]:
                if dir == -1:
                    return 1
                elif dir == 1:
                    return -1
                else:
                    return 0
            else:
                return 0


def real_change(change_d):
    global arr
    for i in range(4):
        if change_d[i] == -1:
            a = arr[i].pop(0)
            arr[i].append(a)
        elif change_d[i] == 1:
            a = arr[i].pop()
            arr[i].insert(0, a)
    




T = int(input())
for tc in range(1, T+1):
    K = int(input())
    arr = [list(map(int, input().split()))for _ in range(4)]
    
    info = []

    for t in range(K):
        m, d = map(int, input().split())
        info.append([m, d])

    for c in info:
        m, d = c
        r = change(m, d)
        real_change(r)

    point = 0

    for j in range(4):
        if arr[j][0] == 1:
            if j == 0:
                point += 1
            elif j == 1:
                point += 2
            elif j == 2:
                point += 4
            elif j == 3:
                point += 8
            
    print(f'#{tc} {point}')