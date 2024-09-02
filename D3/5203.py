
def Run(lst):
    result = 0
    idx = 1
    while idx <= 8:
        if lst[idx-1] >0 and  lst[idx+1]>0 and lst[idx] > 0:
            lst[idx-1] -= 1
            lst[idx] -= 1
            lst[idx+1] -= 1
            idx = 1
            result += 1
        else:
            idx += 1
    return result

def triplet(lst):
    result = 0
    idx = 0
    while idx < 10:
        if lst[idx] >= 3:
            lst[idx] -=3
            idx = 0
            result += 1
        idx += 1
    return result



T = int(input())
for tc in range(1, T+1):
    game = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    result = '0'
    for i in range(12):
        if i % 2 == 0:
            p1[game[i]] += 1
        else:
            p2[game[i]] += 1
        p1p = triplet(p1) + Run(p1)
        p2p = triplet(p2) + Run(p2)
        if p1p > p2p:
            result = '1'
            break
        elif p1p < p2p:
            result = '2'
            break


    print(f'#{tc} {result}')