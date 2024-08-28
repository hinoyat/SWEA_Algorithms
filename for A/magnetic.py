def change(m, d):
    # 인덱스로 계산할거니 -1
    m -= 1
    # 바뀌는지 안 바뀌는지 체크할 리스트
    change_d = [0, 0, 0, 0]
    # 명령 들어온 것은 바로 바꾸기
    change_d[m] = d
    
    # 바꿀 자석의 인덱스에 따라서 함수를 순서대로 호출하기
    # 호출한 결과를 위의 리스트에 넣어주기
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



# 바뀔지 안 바뀔지 판단하는 함수
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

# 여기서 배열을 진짜 바꿔줍니다.
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
            point += 2**j

            
    print(f'#{tc} {point}')