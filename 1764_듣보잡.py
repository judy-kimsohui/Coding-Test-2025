# 1764_듣보잡

N, M = map(int, input().split())
WhatS = set()
for _ in range(N):
    WhatS.add(input())

Person = set()
for _ in range(M):
    person = input()
    if person in WhatS:
        Person.add(person)

PersonL = list(Person)
PersonL.sort()
print(len(PersonL))
for p in PersonL:
    print(p)