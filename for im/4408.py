# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     move = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         if s < e:
#             move.append(s-1)
#             move.append(e+1)
#         else:
#             move.append(e-1)
#             move.append(s+1)

#     lst = [0 for _ in range(401)]
#     check = sorted(move)
#     # print(move)
#     # print(check)
#     for i in range(0, len(move) - 1, 2):
#         s = move[i]
#         e = move[i+1]
#         for j in range(s, e):
#             lst[j] += 1
#     print(lst)
#     print(f'#{tc} {max(lst)}')
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    move = []
    for _ in range(N):
        s, e = map(int, input().split())
        if s < e:
            move.append(s-1)
            move.append(e+1)
        else:
            move.append(e-1)
            move.append(s+1)
    # print(move)
    lst = [0 for _ in range(201)]
    for i in range(0, len(move)-1, 2):
        s = move[i]
        e = move[i+1]
        for j in range(s//2, e//2):
            lst[j] += 1
    print(f'#{tc} {max(lst)}')
    
    