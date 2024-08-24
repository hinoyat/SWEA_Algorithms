T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().strip()))
    count = [0] * 10

    for c in card:
        count[c] +=1
    
    babygin = 'false'

    result = 0

    r = 0
    while r < 10:
        if count[r] >=3:
            count[r] -=3
            r = 0 
            result +=1
        else:
            r += 1
    
    t = 1
    while t < 9:
        if count[t-1] >0 and count[t] > 0 and count[t+1]>0:
            count[t-1] -=1
            count[t] -=1
            count[t+1] -=1
            t = 0
            result +=1
        else:
            t +=1

    if result >=2:
        babygin = 'true'


    print(f'#{tc} {babygin}')