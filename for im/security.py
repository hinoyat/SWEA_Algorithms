from pprint import pprint
import math
test = int(input())
for tc in range(1, test+1):
    N, M = map(int, input().split())
    # range 돌릴 k 범위 최대
    arr = [list(map(int, input().split())) for _ in range(N)]
    # pprint(arr)
    home = 0
    max_v = 0
    K = math.ceil(N/2)
    for k in range(1, N+2):
        distance = k
        max_cnt = 0
        for i in range(N):
            for j in range(N):
                cnt = 0
                for hi in range(N):
                    for hj in range(N):
                        if arr[hi][hj] == 1:
                            if abs(i - hi) +  abs(j - hj) < k:
                                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
        # print(k)
        # print(max_cnt)
        k_p = (k*k+(k-1)*(k-1))
        p = max_cnt * M
        # print(k_p)
        # print(p)
        result = p - k_p
        if result >= 0 and max_cnt > home:
            max_v = result
            home = max_cnt
    print(f'#{tc} {home}')