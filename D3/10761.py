# 풀어보면 좋은 문제 상호의 배틀필드
# 풀어보면 졸은 문제 오셀로
# 신뢰
T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())
    # print(lst)
    N = int(lst.pop(0))
    # print(N, lst)
    start_t = 0
    min_t = 0xffffffff
    O = 1
    B = 1
    O_t = 0
    B_t = 0
    pre_robo = lst[0]
    for s in range(0, len(lst), 2):
        robo = lst[s]
        btn = int(lst[s+1])

        if robo == pre_robo:
            if robo == 'B':
                B_t += abs(btn - B) + 1
                B = btn
            else:
                O_t += abs(btn - O) + 1
                O = btn
                
        else:
            if robo == 'B':
                if B_t + abs(btn - B) + 1 <= O_t:
                    B_t = O_t + 1
                else:
                    B_t += abs(btn - B) + 1
                B = btn
            else:
                if O_t + abs(btn - O) + 1 <= B_t:
                    O_t = B_t + 1
                else:
                    O_t += abs(btn - O) + 1
                O = btn
        pre_robo = robo
    print(f'#{tc} {max(O_t, B_t)}')