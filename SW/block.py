import copy
from collections import deque
from copy import deepcopy


# 배열과 터뜨릴 열을 받아와서 터뜨리기
def breaking(array1, breaking_point):
    visited = [[0] * W for _ in range(H)]

    que = deque()
    b_point = 0
    for i in range(H):
        if array1[i][breaking_point] != 0:
            b_point = [i, breaking_point]
            break
    if b_point == 0:
        return array1

    si, sj = b_point
    # 이제 어레이를 바꿔주기
    visited[si][sj] = 1
    que.append((si, sj))

    while que:
        qi, qj = que.popleft()
        point = array1[qi][qj]
        for s in range(1, point):
            for di, dj in delta:
                ni, nj = qi + di*s, qj + dj*s
                if 0<= ni < H and 0 <= nj < W and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    que.append((ni, nj))
        array1[qi][qj] = 0

    for i in range(W):
        live_block = []
        for j in range(H):
            if array1[j][i] != 0:
                live_block.append(array1[j][i])
        live_block = [0] * (H - len(live_block)) + live_block
        for j in range(H):
            array1[j][i] = live_block[j]
    return array1

def supernova(idx, array, cnt):
    global ans
    if cnt == N:
        result = 0
        for i in range(H):
            result += array[i].count(0)
        ans = max(ans, result)
        return

    # 벽돌을 깰지 안 깰지
    for i in range(W):
        # 깨면 함수 호출
        new_array = breaking(copy.deepcopy(array), i)
        supernova(i, new_array, cnt + 1)
        # 안 깨면 인덱스 + 1 하고 넘기기


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    supernova(0, copy.deepcopy(arr), 0)
    print(f'#{tc} {W * H - ans}')