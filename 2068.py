# 2068

t = int(input())

for i in range(t):
    num = list(map(int,input().split()))
    sorted_list = sorted(num)
    max_num = sorted_list.pop()
    print(f'#{i+1} {max_num}')