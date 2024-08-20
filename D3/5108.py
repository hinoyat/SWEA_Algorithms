# 숫자 추가
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())

    lst = list(map(int, input().split())) + [0]*M
    print(lst)

    # new_lst = [-1 for _ in range(N+M)]

    # for i in range(M):
    #     idx, v = map(int,input().split())
    #     new_lst[idx] = v
    
    
    

        