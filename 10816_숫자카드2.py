# 10816_숫자카드2

from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def count_num(x):
    return bisect_right(A, x) - bisect_left(A, x)

for x in B:
    print(count_num(x), end=' ')
            