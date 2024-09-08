T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    # K == 1 일때 거리 차이 < = 0 2일 때 <= 1 3일 때 <= 2

    ans = 0
    # 집 배열 저장하자
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append([i,j])
    home_cnt = len(home)
    # 언제까지 돌릴까? N 과 M 중 최댓값 그래야 배열의 범위를 다 커버함
    # 하지만 N 이 증가했을 때 돈을 더 벌지 못하면 가지치기 해주자
    for K in range(1, N + 2):
        # 최대 거리
        max_len = K - 1
        price = (K * K) + ((K-1)*(K-1))
        # 방범 서비스 위치 잡기
        for pi in range(N):
            for pj in range(N):
                cnt = 0
                for hi, hj in home:
                    if abs(pi - hi) + abs(pj - hj) <= max_len:
                        cnt += 1

                val = (M * cnt) - price
                if val >= 0:
                    ans = max(cnt, ans)
        if (home_cnt * M) - price < 0:
            break

    print(f'#{tc} {ans}')
