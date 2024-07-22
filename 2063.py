n = int(input())

num_list = list(map(int,input().split()))
num_list.sort()
mid_idx = len(num_list)//2
mid_num = num_list[mid_idx]
print(mid_num)