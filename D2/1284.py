T = int(input())
for tc in range(1, T+1):
    # W가 사용량
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + S * (W - R)
    
    if A >= B:
        print(f'#{tc} {B}')
    else:
        print(f'#{tc} {A}')