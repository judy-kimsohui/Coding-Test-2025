
# LCM({15,20})=60, LCM({15})=15, LCM({20,30,35})=420
# 집합 T의 최소공배수 집합 LCMSET(T)는, T의 모든 공집합이 아닌 부분집합 S에 대해 최소공배수를 구해 모두 나열한 집합
# LCMSET({20,30,35}) = {LCM({20}), LCM({30}), LCM({35}), LCM({20,30}), LCM({30,35}), LCM({20,35}), LCM({20,30,35})} = {20, 30, 35, 60, 140, 210, 420}
# 두 집합 A와 B가 주어졌을 때, LCMSET(A) = LCMSET(B)인지를 판별
# = or !



T = int(input())
for _ in range(T):
    NA, NB = map(int, input().split())
    LCM_AL = set(map(int, input().split()))
    LCM_BL = set(map(int, input().split()))