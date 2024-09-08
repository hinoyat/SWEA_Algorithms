T = int(input())
for tc in range(1, T+1):
    K = int(input())
    magnetic_cnt = 4
    magnetic_round = 8
    arr = [list(map(int, input().split())) for _ in range(magnetic_cnt)]