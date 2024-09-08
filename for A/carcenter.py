from collections import deque

T = int(input())
for tc in range(1, T+1):
    # 접수, 정비, 고객 수, 분실 고객 접수한 곳의 번호, 분실 고객 정비한 곳의 번호
    N, M, K, A, B = map(int, input().split())
    # 접수 시간
    desk = list(map(int,input().split()))
    # 정비 시간
    repair = list(map(int,input().split()))
    # 고객이 방문하는 시간
    customer = list(map(int,input().split()))

    ans = 0

    time = 0
    # 접수 대기/ 정비 대기
    desk_lst = [[0, 0] for _ in range(N)]
    repair_lst = [[0, 0] for _ in range(M)]

    # 접수, 정비 해당하는 큐 생성
    desk_que = deque()
    repair_que = deque()
    # 처음에 고객들이 모두 데스크 큐에 고객 번호는 1번부터 들어오고 도착 시간 순서대로 주어지니까 정렬 X
    num = 1
    for i in customer:
        desk_que.append([num, i])
        num += 1
    # print(desk_que)
    # A 왔다 B 온 사람 체크
    check = set()

    while True:
        # 비어있을 때 고객이 도착하면 데스크에 올리기 올리는
        for dn, dv in enumerate(desk_lst):
            if dv[1] > 0:
                desk_lst[dn][1] -= 1
                if desk_lst[dn][1] == 0:
                    repair_que.append(dv[0])

            if dv[1] == 0:
                if desk_que:
                    if desk_que[0][1] <= time:
                        cnum, ctime = desk_que.popleft()
                        desk_lst[dn] = [cnum, desk[dn]]
                        if dn == A - 1:
                            check.add(cnum)

        for rn, rv in enumerate(repair_lst):
            if rv[1] > 0:
                repair_lst[rn][1] -= 1
                if repair_lst[rn][1] == 0:
                    if rn == B - 1:
                        if rv[0] in check:
                            ans += rv[0]
            if rv[1] == 0:
                if repair_que:
                    cnum = repair_que.popleft()
                    repair_lst[rn] = [cnum, repair[rn]]


        if not repair_que and not desk_que and all(c[1] == 0 for c in repair_lst + desk_lst):
            break

        time += 1
    if ans == 0:
        ans = -1

    print(f'#{tc} {ans}')
