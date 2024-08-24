T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    max_t = len(A)
    
    skip_t = len(B)

    check = 0
    cnt = 0
    while check < max_t:
        if A[check : check+skip_t] == B:
            cnt += 1
            check += skip_t
        else:
            check +=1

    r = max_t - (cnt*skip_t) + (cnt+1)