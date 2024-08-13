T = int(input().strip())
for tc in range(1, T+1):
    N = int(input())
    nperfect = list(map(str, input().split()))

    # 셔플한 카드 저장소 만들기
    perfect = ['' for _ in range(N)]
    l = len(nperfect)

    # 카드의 수가 홀수일 때 
    if l % 2 != 0:
        k = 1 # 뒤의 반절은 perfect의 홀수 인덱스로 가기 위해 탄생
        for i in range(l):
            if i <= l//2:   # 작거나 같으면으로 하면 하나가 더 들어가요
                perfect[i*2] = nperfect[i]
            else:
                perfect[k*2 - 1] = nperfect[i]  # 홀수 인덱스에 저장
                k += 1 # k 하나 늘려주기

    # 카드의 수가 짝수일 때
    else:
        k = 1
        for i in range(l):
            if i < l//2:    # 딱 반반 해야해서 미만
                perfect[i*2] = nperfect[i]
            else:
                perfect[k*2 - 1] = nperfect[i]
                k += 1

    print(f'#{tc}', end=' ')
    print(*perfect)