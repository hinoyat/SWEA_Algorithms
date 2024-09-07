from collections import deque
from pprint import pprint


# 안되는 경우만 작성
def canmove(qv, nv, di, dj):
    if qv == 1:
        if di == 1:
            if nv == 3 or nv == 5 or nv == 6:
                return False
            else:
                 return True
        elif di == -1:
            if nv == 3 or nv == 4 or nv == 7:
                return False
            else:
                return True
        elif dj == 1:
            if nv == 2 or nv == 4 or nv == 5:
                return False
            else:
                return True
        elif dj == -1:
            if nv == 7 or nv == 6 or nv == 2:
                return False
            else:
                return True

    elif qv == 2:
        if nv == 3:
            return False
        elif nv == 4 or nv == 7:
            if di == -1:
                return False
            else:
                return True
        elif nv == 5 or nv == 6:
            if di == 1:
                return False
            else:
                return True
        else:
            return True
    elif qv == 3:
        if nv == 2:
            return False
        elif nv == 6 or nv == 7:
            if dj == -1:
                return False
            else:
                return True
        elif nv == 4 or nv == 5:
            if dj == 1:
                return False
            else:
                return True
        else:
            return True
    elif qv == 4:
        if nv == 3 or nv == 7:
            if di == -1:
                return False
            else:
                return True
        elif nv == 2 or nv == 5:
            if dj == 1:
                return False
            else:
                return True
        elif nv == 4:
            return False
        else:
            return True
    elif qv == 5:
        if nv == 6 or nv == 3:
            if di == 1:
                return False
            else:
                return True
        elif nv == 2 or nv == 4:
            if dj == 1:
                return False
            else:
                return True
        elif nv == 5:
            return False
        else:
            return True

    elif qv == 6:
        if nv == 5 or nv == 3:
            if di == 1:
                return False
            else:
                return True
        elif nv == 7 or nv == 2:
            if dj == -1:
                return False
            else:
                return True
        elif nv == 6:
            return False
        else:
            return True

    elif qv == 7:
        if nv == 3 or nv == 4:
            if di == -1:
                return False
            else:
                return True
        elif nv == 6 or nv == 2:
            if dj == -1:
                return False
            else:
                return True
        elif nv == 7:
            return False
        else:
            return True
    return False


def supernova(si, sj):
    que = deque()
    que.append([si, sj, arr[si][sj]])
    cnt = 1
    while que:
        qi, qj, qv = que.popleft()

        for di, dj in whole[qv]:
            ni = qi + di
            nj = qj + dj
            if 0 <= ni < N and 0<= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                # if (-di, -dj) in whole[arr[ni][nj]]:
                if canmove(qv,arr[ni][nj], di, dj):
                    visited[ni][nj] = visited[qi][qj] + 1
                    if visited[ni][nj] <= L:
                        cnt += 1
                    que.append([ni, nj, arr[ni][nj]])
    return cnt
T = int(input())
for tc in range(1, T+1):
    # 세로/ 가로/ 뚜껑의 세로/ 뚜껑의 가로/ 시간
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 맨홀뚜껑이 시작 지점이다
    # 주어지는 배열의 관이 BFS로 갈 수 있는 곳이다  퍼져나간 곳의 수
    # 시작 지점이 시간 1이다 == 시작했을 때 1시간 바로 지나갔다는 소리
    # 배열의 0인 곳은 가지 못함

    # 1 상하좌우 2 상하 3 좌우 4 상, 우 5 하 우 6 하 좌 7 상좌

    whole = {1:((-1, 0), (1, 0), (0, 1), (0, -1)),
             2:((-1, 0), (1, 0)),
             3:((0, 1), (0, -1)),
             4:((-1, 0), (0, 1)),
             5:((1, 0), (0, 1)),
             6:((1, 0), (0, -1)),
             7:((-1, 0), (0, -1))
             }
    si, sj = R, C
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    ans = 0

    r = supernova(si, sj)


    print(f'#{tc} {r}')
