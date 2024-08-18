# 숫자 배열 회전
from pprint import pprint
test_case = int(input())
def rotate(ar):
    ar1 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ar1[i][j] = ar[N-1-j][i]
    return ar1



for tc in range(1, test_case+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    
    arr90 = rotate(arr)
    arr180 = rotate(arr90)
    arr270 = rotate(arr180)

    for a1, a2, a3 in zip(arr90, arr180, arr270):
        print(f'#{tc} {''.join(map(str, a1))} {''.join(map(str, a2))} {''.join(map(str, a3))}')

