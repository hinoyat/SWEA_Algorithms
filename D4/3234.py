
def fac(num):
    if num > 1:
        return num * fac(num-1)
    else:
        return 1



def supernova(cnt, left, right, max_val):
    global ans
    if right > left:
        return

    if cnt == N:
        ans += 1
        return

    if left > max_val + right:
        ans += 2**(N-cnt) * fac(N-cnt)
        return


    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            supernova(cnt + 1, left + num[i], right, max_val - num[i])
            supernova(cnt + 1, left, right + num[i], max_val - num[i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    ans = 0
    visited = [0] * N
    max_v = sum(num)
    supernova(0, 0, 0, max_v)
    print(f'#{tc} {ans}')