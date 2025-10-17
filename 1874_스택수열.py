# 1874_스택수열

# 수열을 push, pop 했을 때 해당 순서를 만들 수 있는가?

N = int(input())
ResultL = []
for _ in range(N):
    ResultL.append(int(input()))

L = len(ResultL)
Stack = []

# 수열 만들기가 가능한가?
possible = True
AnswerL = []

# 올라가는 번호는, 스택에 차례대로 넣을 번호
cnt = 1

for num in ResultL:

    if cnt <= num:
        Stack += [i for i in range(cnt, num+1)]
        AnswerL += ["+" for _ in range(cnt, num+1)]
        cnt = num+1
    
    # 스택 마지막 수가 결과와 같다면 pop
    if Stack[-1] == num:
        n = Stack.pop()
        AnswerL.append("-")
        continue
    
    possible = False
        
if possible:
    for i in AnswerL:
        print(i)
else:
    print("NO")
