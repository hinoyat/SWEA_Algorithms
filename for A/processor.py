T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 직선으로만 연결 가능
    # 벽에 붙은 건 연결로 친다

    # 전선 길이의 최솟값
    ans = 21e8