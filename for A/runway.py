def supernova(lst, max_v):
    idx = 1
    visited = [0] * N
    while idx < N:
        # 내 위치가 전의 위치보다 클 때 확인
        if lst[idx - 1] < lst[idx]:
            if lst[idx] - lst[idx-1] > 1:
                return 0
            high = lst[idx - 1]
            # 범위를 벗어나면 불가
            if idx - X < 0:
                return 0
            # 벗어나지 않았으면
            else:
                c_idx = idx - X
                c_len = 0
                while c_idx < idx:
                    if visited[c_idx]:
                        return 0
                    if lst[c_idx] == high:
                        c_len += 1
                        visited[c_idx] = 1
                    else:
                        return 0
                    c_idx += 1

        elif lst[idx - 1] > lst[idx]:
            if lst[idx-1] - lst[idx] > 1:
                return 0
            if idx + X - 1 >= N:
                return 0
            else:
                high = lst[idx]
                c_idx = idx + X - 1
                c_len = 0
                while c_idx > idx:
                    if lst[c_idx] == high:
                        visited[c_idx] = 1
                        c_len += 1
                    else:
                        return 0
                    c_idx -= 1

        idx += 1
    return 1


T = int(input())
for tc in range(1, T+1):
    N, X = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 설계 하고 들어가기
    # 지역의 최고점은 건설을 할 필요가 없음 배열 돌때마다 max값 찾기
    # 최댓값 보다 낮은 값에 대해서만
    
    # 높이 차이가 2 이상일 때 건설 False

    # 높이 차이가 날 때 X 만큼의 활주로를 건설 못하면 False
    # 돌면서 구간이 X 미만인 곳이 있다면 False

    # 건설하려는 곳에 이미 건설이 되어있으면 False

    # 한칸짜리 언덕일 때
    newarr = list(map(list, zip(*arr)))
    
    # 하나씩 보내기 행 먼저 보내고 열 보내고
    ans = 0
    for i in range(N):
        ans += supernova(arr[i], max(arr[i]))
        ans += supernova(newarr[i], max(newarr[i]))

    print(f'#{tc} {ans}')
