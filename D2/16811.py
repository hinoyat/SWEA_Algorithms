T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    di = {}
    for i in lst:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    # print(di)
    key = list(di.keys())
    key.sort()
    # print(key)
    com = []
    for i in range(1, len(key)):
        for j in range(i+1, len(key)):
            com.append([i,j])
    # print(com)

    can = -1
    min_c = []
    for i in com:
        # print(i)
        c1, c2 = i
        lst2 = [0, 0, 0]
        for i in range(0, c1):
            lst2[0] += di[key[i]]
        for j in range(c1, c2):
            lst2[1] += di[key[j]]
        for k in range(c2, len(key)):
            lst2[2] += di[key[k]]
        if 0 <lst2[0] <= N//2 and 0<lst2[1] <= N//2 and 0<lst2[2] <= N//2:
            can = 1
            min_c.append(max(lst2) - min(lst2))
        # print(min_c)
            
    if can == 1:
        print(f'#{tc} {min(min_c)}')
    else:
        print(f'#{tc} -1')