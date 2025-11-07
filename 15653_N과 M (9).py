from itertools import permutations

N, M = map(int, input().split())
List = list(map(int, input().split()))
List.sort()

Result = list(set(permutations(List, M)))
Result.sort()
for l in Result:
    print(*l)