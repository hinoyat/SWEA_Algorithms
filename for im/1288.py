T = int(input())

for tc in range(1, T+1):
    x = int(input())
    num = [0 for _ in range(10)]
    cnt = 0
    n = 1
    while 0 in num:
        cnt += 1
        now =  x * n
        for i in str(now):
            num[int(i)] += 1
        n += 1

    print(f'#{tc} {now}')