# 9012_괄호

# 괄호 문제를 스택으로 푼다.
# ( 스택에 추가한다
# ) 스택에서 하나 꺼낸다
# 모든 ) 탐색 후, 스택에 ( 가 남아있다면 올바르지 않음
# ) 스택에서 꺼내려 했는데 ( 가 없다면 올바르지 않음

def VPS(Input):
    Stack = []
    
    for i in Input:
        if i == "(":
            Stack.append("(")
        else:
            if len(Stack) == 0:
                return "NO"
            else:
                Stack.pop()

    if len(Stack) != 0:
        return "NO"
        
    return "YES"

q = int(input())
for _ in range(q):

    Input = list(input())
    print(VPS(Input))
    