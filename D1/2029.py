# 2029
t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    quo = a // b
    rem = a % b
    print(f'#{i+1} {quo} {rem}')