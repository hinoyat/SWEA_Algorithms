def jin(num):
    start = 1
    end = P
    cnt = 0
    while start <=end:
        mid = (start + end)//2
        if mid > num:
            end = mid
            cnt +=1
        elif mid < num:
            start = mid
            cnt +=1
        else:
            break
    return cnt



T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    ra = jin(A)
    rb = jin(B)
    print(ra, rb)
