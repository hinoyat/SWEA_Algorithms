from collections import defaultdict

def moving(key, d):
    x = key[0]
    y = key[1]
    if d == 0:
        y += 0.5
    elif d == 1:
        y -= 0.5
    elif d == 2:
        x -= 0.5
    elif d == 3:
        x += 0.5

    return (x,y)




T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    dct = defaultdict(list)
    energy = 0
    for i in range(N):
        x, y, d, K = map(int, input().split())
        dct[(x, y)].append((d, K))
    # print(dct)
    cnt = 0
    while dct:
        newd = defaultdict(list)
        check = []
        for key in dct:
            nx, ny = moving(key, dct[key][0][0])
            if nx > 1000 or nx < -1000 or ny < -1000 or ny > 1000:
                continue
            if (nx, ny) in newd:
                if (nx, ny) not in check:
                    check.append((nx, ny))
            newd[(nx, ny)].append(*dct[key])
        for k in check:
            for e in newd[k]:
                energy += e[1]
            del newd[k]

        dct = newd
        cnt += 1
        # print(check)

    # print(dct)
    print(f'#{tc} {energy}')
