# 1933
n = int(input())
week_list = []
for i in range(1,n+1):
    if n % i == 0:
        week_list.append(i)

for s in range(len(week_list)):
    print(week_list[s],end=' ')