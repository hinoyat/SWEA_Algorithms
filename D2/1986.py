test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    odd_lst = []
    even_lst = []
    for i in range(1, N+1):
        if i % 2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)

    odd = sum(odd_lst)
    even = sum(even_lst)
    result = odd - even
    print(f'#{tc} {result}')
