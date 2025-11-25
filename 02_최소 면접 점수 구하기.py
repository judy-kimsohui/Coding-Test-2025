# 면접에서 N개의 문제 중 M개의 문제를 맞혔다.
# 연속으로 문제를 맞힐 경우 점수를 더 많이 준다 (카운터)
# 카운터 초기값은 0이다

# 문제를 맞힐 경우 1점을 획득한 경우 카운트 += 1
# 카운터가 K에 도달하면 0으로 초기화, 총 점이 2배가 된다.
# 문제 틀리면, 카운터가 초기화된다.
# M개의 문제를 맞힐 수 있는 경우 중 최소 총점을 구하라

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())

    # 틀릴 수 있는 문제 수 (카운터 초기화 전 후반부쪽에 끼워넣어야함)
    C = N - M

    # 초반부에 2배씩 뛰어야 하는 문제 수 S = 다 맞혀야함
    S = N - K * C

    if S >= 0:
        # 후반부 부터 카운터 초기화 고려해 계산한 점수Last
        Last = (K - 1) * C

        # K 단위로 2배씩 몇 번 뛰어야하는지, 나머지 점수는 몇 점인지
        B = S // K
        L = S % K

        Score = 0
        for _ in range(B):
            Score += K
            Score *= 2

        Score += L + Last
        print("#" + str(t+1) + " " + str(Score))

    else:
        # K로 나눌 수 있는 최대 수 H 구하기
        H = N // K

        # 후반부 부터 카운터 초기화 고려해 계산한 점수Last
        Last = (K - 1) * H

        print("#" + str(t + 1) + " " + str(Last))