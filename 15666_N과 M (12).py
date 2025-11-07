from itertools import combinations_with_replacement

N, M = map(int, input().split())
List = list(map(int, input().split()))
List.sort()

Result = list(set(combinations_with_replacement(List, M)))
Result.sort()
for l in Result:
    print(*l)