# 2072

t = int(input())

for i in range(t):
    sum_odd = 0
    num = list(map(int,input().split()))
    for d in num:
        if d % 2 != 0:
            sum_odd += d
    print(f'#{i+1} {sum_odd}')