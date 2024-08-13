def cal(num):
    if num < 0:
        return 0 - num
    else:
        return num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rock = list(map(int, input().split()))
    min_range = 21e8
    
    for i in rock:
        if min_range > cal(i):
            min_range = cal(i)
    
    cnt = 0
    for i in rock:
        if cal(i) == min_range:
            cnt += 1
    
    print(f'#{tc} {min_range} {cnt}')