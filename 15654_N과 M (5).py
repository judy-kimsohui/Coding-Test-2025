from itertools import permutations

N, M = map(int, input().split())
List = list(map(int, input().split()))
List.sort()

Result = list(permutations(List, M))

for l in Result:
    print(*l)