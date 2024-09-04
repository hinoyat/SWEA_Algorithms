# def supernova(n, cnt, target):
#     global ans
#
#     if n <= 0:
#         return
#     if cnt >= ans:
#         return
#     if n > target:
#         return
#
#     if n == target:
#         ans = max(cnt, ans)
#
#     if target > n:
#         supernova(n * 2, cnt + 1, target)
#         supernova(n + 1, cnt + 1, target)
#     else:
#         supernova(n - 1, cnt + 1, target)
#         supernova(n - 10, cnt + 1, target)
#
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, target = map(int,input().split())
#     ans = 10000
#     supernova(N, 0, target)
#
#     print(f'#{tc} {ans}')


# from collections import deque
#
#
# def supernova_bfs(n, target):
#     if n >= target:
#         return n - target
#
#     visited = set()
#     queue = deque([(n, 0)])  # (현재값, 연산 횟수)
#     visited.add(n)
#
#     while queue:
#         current, cnt = queue.popleft()
#
#         # 목표에 도달한 경우
#         if current == target:
#             return cnt
#
#         # 가능한 모든 연산
#         next_steps = [current * 2, current + 1, current - 1, current - 10]
#         for next_step in next_steps:
#             if next_step >= 0 and next_step not in visited:
#                 visited.add(next_step)
#                 queue.append((next_step, cnt + 1))
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, target = map(int, input().split())
#     result = supernova_bfs(N, target)
#     print(f'#{tc} {result}')
