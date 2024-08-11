T = int(input())
for tc in range(1, T+1):
    len_a, len_b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0
    if len_a < len_b:
        for s in range(len_b - len_a+1):
            sum_v = 0
            for a in range(len(A)):
                sum_v += A[a] * B[a+s]
            if max_v < sum_v:
                max_v = sum_v
    else:
        for s in range(len_a - len_b+1):
            sum_v = 0
            for b in range(len(B)):
                sum_v += B[b] * A[b+s]
            if max_v < sum_v:
                max_v = sum_v
        
    
    print(f'#{tc} {max_v}')