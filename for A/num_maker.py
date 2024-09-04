def supernova(idx, level):
    if tuple(lst) in check:
        return

    if level == N-1:
        # print(lst)
        check.add(tuple(lst))
        return

    for i in range(N-1):
        if visited[i]: continue
        lst.append(real_order[i])
        visited[i] = 1
        supernova(i + 1, level + 1)
        lst.pop()
        visited[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    order = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))
    dct = {0:'+', 1:'-', 2:'*', 3:'/'}

    real_order = []

    for i in range(len(order)):
        for j in range(order[i]):
            real_order.append(dct[i])

    # print(real_order)

    lst = []
    visited = [0] * (N-1)
    check = set()

    supernova(0, 0)
