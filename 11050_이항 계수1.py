# 11050_이항 계수1

# 자연수 
# \(N\)과 정수 
# \(K\)가 주어졌을 때 이항 계수 
# \(\binom{N}{K}\)를 구하는 프로그램
# 이항계수 : 이항식 $(a+b)^n$을 전개했을 때 각 항의 계수

from itertools import combinations

N, K = map(int, input().split())
List = [i for i in range(N)]
print(len(list(combinations(List, K))))