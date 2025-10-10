# 10815_숫자카드
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

BnumL = []
for i, num in enumerate(B):
    BnumL.append((num, i))

FindL = [[i, 0] for _, i in BnumL]
A.sort()
BnumL.sort()

# 같으면 있는 것
# B가 A보다 작으면 없는 것
# 크면 A 넘어가기
left = 0
right = len(A)-1
mid = (left + right) // 2

for n, i in BnumL:
    right = len(A)-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == n:
            FindL[i][1] = 1
            break
        elif A[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

FindL.sort()
for i, num in FindL:
    print(num, end=" ")
            