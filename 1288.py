# 1288 양세기
# hint 배열의 인덱스
# s='1343'
# cnt = 0
# for c in s:
#     if c =='3'
#         cont +=1

# cnt = [0] * 10
# '1295 =>'
# cnt[1] +=1
# cnt[2] +=1
# cnt[9] +=1
# cnt[5] +=1



# T = int(input())

# for i in range(T):
#     s = input()

        

    # input 받고
    # 몇 개인지 세야 함
    # 만약 10개 미만이다
    # 입력값에 X n,  n은 처음에 1 다음부터 +1씩
    # 10개되면 종료 하면서 n값 반환
    # 처음부터 set 쓰지 말고 더하고 Set쓰고 하면서 갯수 세고
    # 필요한 변수 N에 곱하는 숫자
    # 몇번째인지 세는 카운트


T=int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 10

    value = '0'
    while 0 in cnt:
        value = str(int(value)+N)
        for c in value:
            cnt[int(c)] +=1

print(f'#{tc} {value}')