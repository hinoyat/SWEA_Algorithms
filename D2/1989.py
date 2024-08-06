# 1989 초심자의 회문 검사

test_case = int(input())
for tc in range(1, test_case+1):
    word = list(input())
    if word[:] == word[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')