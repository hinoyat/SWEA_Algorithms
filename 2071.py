# 2072

t = int(input())

for i in range(t):
    sum_num = 0
    num = list(map(int,input().split()))
    for d in num:
        sum_num += d
    
    avg = round(sum_num/len(num))
    print(f'#{i+1} {avg}')