# T = int(input())
# for tc in range(1, T+1):
#     price = list(map(int, input().split()))
#     plan = list(map(int, input().split()))
#     real_ans = 21e8
#
#     # 1일로 이용했을 때 1개월로 이용했을 때 비교해서 저장하자
#     real_day_month = [0] * 14
#     for i in range(12):
#         day = plan[i] * price[0]
#         month = price[1]
#
#         if day > month:
#             real_day_month[i] = month
#         elif day < month:
#             real_day_month[i] = day
#         else:
#             real_day_month[i] = day
#
#     # 3개월이랑 1일 비교
#     real_idx = 0
#     while real_idx <= 12:
#         day_month = real_day_month[:]
#         lst3 = [0] * 14
#         idx = real_idx
#         ans = 0
#         while idx <= 12:
#             if idx <= 12:
#                 check = day_month[idx:idx+3]
#                 if sum(check) > price[2]:
#                     for i in range(idx, idx+3):
#                         day_month[i] = 0
#                         lst3[i] = 0
#                     lst3[idx] = price[2]
#             idx += 1
#         #
#         # print(day_month)
#         # print(lst3)
#         if sum(day_month) + sum(lst3) < price[3]:
#             ans = sum(day_month) + sum(lst3)
#         else:
#             ans = price[3]
#
#         if ans < real_ans:
#             real_ans = ans
#
#
#
#         real_idx += 1
#
#     if real_ans >= price[3]:
#         real_ans = price[3]
#
#     print(f'#{tc} {real_ans}')



