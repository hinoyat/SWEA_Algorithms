from collections import deque

def supernova(target, now, scnt):
    if target <= now:
        return now - target

    visited = set()
    que = deque()
    que.append([now, scnt])
    visited.add(now)
    while que:
        val, cnt = que.popleft()
        if val == target:
            return cnt
        for new_val in (val + 1, val - 1, val * 2, val - 10):
            if new_val not in visited and new_val >= 0 and new_val <= 1000000:
                visited.add(new_val)
                que.append((new_val, cnt + 1))

T = int(input())
for tc in range(1, T+1):
    N, target = map(int, input().split())
    ans = supernova(target, N, 0)
    print(f'#{tc} {ans}')