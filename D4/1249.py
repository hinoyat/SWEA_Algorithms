#
# def supernova(i, j, value):
#     global min_v
#
#     if value >= min_v:
#         return
#
#     if i == N-1 and j == N-1:
#         if value < min_v:
#             min_v = value
#         return
#
#     if (i, j) in memo and memo[(i,j)] <= value:
#         return
#     memo[(i, j)] = value
#
#     for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#         ni = i + di
#         nj = j + dj
#         if ni > N - 1 or nj > N-1 or ni < 0 or nj < 0 or visited[ni][nj] !=0:continue
#         visited[ni][nj] = 1
#         supernova(ni, nj, value + arr[ni][nj])
#         visited[ni][nj] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     # print(arr)
#     min_v = 21e8
#     visited = [[0] * N for _ in range(N)]
#     value = arr[0][0]
#     visited[0][0] = 1
#     memo = {}
#     supernova(0, 0, value)
#     print(f'#{tc} {min_v}')


#
#
# import heapq
# def dijkstra():
#     # 우선순위 큐를 사용하여 최소 비용 경로를 탐색합니다.
#     pq = [(arr[0][0], 0, 0)]  # (현재 비용, x좌표, y좌표)
#     min_v = 21e8
#     distances = [[21e8] * N for _ in range(N)]
#     distances[0][0] = arr[0][0]
#
#     while pq:
#         current_value, i, j = heapq.heappop(pq)
#
#         if i == N - 1 and j == N - 1:
#             min_v = min(min_v, current_value)
#             continue
#
#         for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#             ni = i + di
#             nj = j + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 new_value = current_value + arr[ni][nj]
#                 if new_value < distances[ni][nj]:
#                     distances[ni][nj] = new_value
#                     heapq.heappush(pq, (new_value, ni, nj))
#
#     return min_v
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     result = dijkstra()
#     print(f'#{tc} {result}')


# import heapq  # heapq 모듈을 사용하여 우선순위 큐를 구현합니다.
#
#
# def dijkstra():
#     # 우선순위 큐를 초기화합니다. 초기값은 시작 지점 (비용, x, y)입니다.
#     pq = [(arr[0][0], 0, 0)]  # 시작 지점의 비용은 arr[0][0]입니다.
#
#     # 최단 경로 비용을 저장할 변수 초기화
#     min_v = 21e8  # 시작값으로 매우 큰 값 설정. 이 값은 필요에 따라 조정할 수 있습니다.
#
#     # 각 위치까지의 최소 비용을 저장하는 배열을 초기화합니다.
#     distances = [[21e8] * N for _ in range(N)]  # 모든 위치의 초기값을 무한대로 설정합니다.
#     distances[0][0] = arr[0][0]  # 시작 위치의 비용을 초기값으로 설정합니다.
#
#     # 우선순위 큐를 사용하여 최단 경로를 탐색합니다.
#     while pq:
#         # 비용이 가장 낮은 위치를 우선순위 큐에서 꺼냅니다.
#         current_value, i, j = heapq.heappop(pq)
#
#         # 현재 위치가 목표 위치인 경우, 최단 경로 비용을 갱신합니다.
#         if i == N - 1 and j == N - 1:
#             min_v = min(min_v, current_value)  # 목표 위치에 도달한 경우 최단 경로 비용을 업데이트합니다.
#             continue  # 목표 위치에 도달했으므로, 현재 노드의 인접 노드를 탐색하지 않고 다음 노드를 처리합니다.
#
#         # 현재 위치에서 상하좌우로 이동할 수 있는 모든 위치를 탐색합니다.
#         for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#             ni = i + di  # 새 위치의 x좌표
#             nj = j + dj  # 새 위치의 y좌표
#
#             # 새 위치가 격자 내에 있는지 확인합니다.
#             if 0 <= ni < N and 0 <= nj < N:
#                 new_value = current_value + arr[ni][nj]  # 새 위치까지의 경로 비용을 계산합니다.
#
#                 # 새로 계산된 비용이 기존 기록된 비용보다 작은 경우에만 업데이트합니다.
#                 if new_value < distances[ni][nj]:
#                     distances[ni][nj] = new_value  # 새 위치까지의 최소 비용을 업데이트합니다.
#
#                     # 새 위치와 새 비용을 우선순위 큐에 추가합니다.
#                     heapq.heappush(pq, (new_value, ni, nj))
#
#     # 계산된 최단 경로 비용을 반환합니다.
#     return min_v
#
#
# # 입력 처리
# T = int(input())  # 테스트 케이스의 수를 입력받습니다.
# for tc in range(1, T + 1):
#     N = int(input())  # 격자의 크기를 입력받습니다.
#     arr = [list(map(int, input())) for _ in range(N)]  # 각 행의 숫자를 입력받아 2차원 배열로 저장합니다.
#
#     # Dijkstra 알고리즘을 호출하여 최단 경로 비용을 계산합니다.
#     result = dijkstra()
#
#     # 계산된 결과를 출력합니다.
#     print(result)



import heapq

def supernova(si, sj, val):
    my_que = [(val, si, sj)]
    values = [[0xffff] * N for _ in range(N)]
    values[si][sj] = val
    min_v = 0xffff
    while my_que:
        v, qi, qj = heapq.heappop(my_que)

        if qi == N-1 and qj == N-1:
            min_v = min(min_v, v)

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0 <= ni < N and 0 <= nj < N:
                new_v = v + arr[ni][nj]
                if new_v < values[ni][nj]:
                    values[ni][nj] = new_v
                    heapq.heappush(my_que, (new_v, ni, nj))
    return min_v


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = supernova(0, 0, arr[0][0])
    print(f'#{tc} {result}')