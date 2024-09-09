# def supernova(lst, cnt):
#     global ans
#     r = int(''.join(lst))
#     if r == ans:
#          if (cnt + 2) <= S:
#              supernova(lst, cnt + 2)
#
#     if (cnt, r) in check:
#         return
#
#     check.add((cnt, r))
#
#     if cnt == S:
#         if r > ans:
#             ans = r
#         return
#
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if i != j:
#                 if lst[i] == max_v or lst[j] == min_v or lst[i] > lst[j]:continue
#                 lst[i], lst[j] = lst[j], lst[i]
#                 supernova(lst, cnt + 1)
#                 lst[i], lst[j] = lst[j], lst[i]
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, S = map(str, input().split())
#     lst = list(N)
#     S = int(S)
#     max_v = max(lst)
#     min_v = min(lst)
#     if S > len(lst):
#         S = len(lst)
#     check = set()
#     ra = ''.join(lst)
#     ans = 0
#     supernova(lst, 0)
#     print(f'#{tc} {ans}')
#
# def lcs_dp(X, Y):
#     m = len(X)
#     n = len(Y)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if X[i - 1] == Y[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     return dp[m][n]
#
# T = int(input())
# for tc in range(1, T+1):
#     X = input()
#     Y = input()
#
#     print(lcs_dp(X, Y))
