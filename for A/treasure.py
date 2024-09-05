T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    check_size = N//4
    check1 = list(input())
    check2 = check1[N//2:] + check1[:N//2]
    # print(check1)
    # print(check2)
    check_set = set()
    for i in range(0, N - check_size):
        r1 = int(''.join(check1[i:i +check_size]), 16)
        r2 = int(''.join(check2[i:i +check_size]), 16)
        check_set.add(r1)
        check_set.add(r2)
    # print(check_set)

    result = list(check_set)
    result.sort(reverse=True)
    print(f'#{tc} {result[K - 1]}')
