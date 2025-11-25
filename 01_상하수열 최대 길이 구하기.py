# L을 기준으로, 3~N
# A _ A 건너띈게 만족하는지 확인하고, 맞다면 DP 배열에 추가한다

T = int(input())
for t in range(T):

    N = int(input())
    AL = list(map(int, input().split()))

    # dp[i][j] : 수열을 i와 j 사이로 잘랐을 때
    # 초기값 : (0, 0)
    # 상하수열이라면 : (1, 길이) 저장
    # 상하수열이 아니라면 : (-1, 길이) 저장
    DP = [[(0, 0)] * N for _ in range(N)]

    Result = 0

    for L in range(2, N):
        for start in range(N-L):
            end = start + L

            # 길이가 3이라면, 양 끝이 같은지 확인
            if L == 2:
                if AL[start] == AL[end]:
                    DP[start][end] = (1, L+1)
                    Result = max(Result, L + 1)
            else:
                # 이전 수열이 상하수열이었는지 확인
                (flag, length) = DP[start][end-1]

                # 상하수열이었다면,
                if flag == 1:
                    # 새로운 수열 또한 상하수열이라면 최대값 갱신
                    if AL[end-2] == AL[end]:
                        DP[start][end] = (1, L+1)
                        Result = max(Result, L+1)

                    # 새로운 수열이 상하수열이 아니라면 이전값 저장
                    else:
                        DP[start][end] = (-1, length)

                # 상하수열이 아니거나 새롭게 시작하는 길이라면, 이전값 저장
                elif flag == -1 or flag == 0:
                    DP[start][end] = (-1, length)

    print("#" + str(t+1) + " " + str(Result))
