from itertools import combinations

N, M = map(int, input().split())
List = [i for i in range(1, N+1)]

Result = list(combinations(List, M))
# Result.sort()

for l in Result:
    print(*l)