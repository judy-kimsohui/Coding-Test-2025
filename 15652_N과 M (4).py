from itertools import combinations_with_replacement

N, M = map(int, input().split())
List = [i for i in range(1, N+1)]

Result = list(combinations_with_replacement(List, M))
# Result.sort()

for l in Result:
    print(*l)