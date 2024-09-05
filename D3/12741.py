T = int(input())
for tc in range(1, T+1):
    As, Ae, Bs, Be = map(int, input().split())
    lst1 = [0] * 100
    # lst2 = [0] * 100
    max_v = max(As, Ae, Bs, Be)
    for i in range(As, Ae):
        lst1[i] += 1
    for i in range(Bs, Be):
        lst1[i] += 1

    ans = lst1.count(2)
    print(f'#{tc} {ans}')
