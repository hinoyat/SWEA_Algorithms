N = int(input())
word = [str(i) for i in range(1, N+1)]
for i in word:
    clap = False
    cnt = 0
    for j in i:
        if int(j) % 3 == 0 and int(j) != 0:
            cnt += 1
            clap = True

    if clap == True:
        print('-'*cnt, end=' ')
    else:
        print(i, end=' ')