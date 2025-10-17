# 10828_스택

Q = int(input())
Stack = []
for Query in range(Q):
    
    Query = list(input().split())
    if len(Query) == 1:

        # 스택 정수 빼고 그 수를 출력, , 스택이 비었다면 -1 출력
        if Query == ["pop"]:
            if len(Stack) == 0:
                print(-1)
            else:
                n = Stack.pop()
                print(n)

        # 스택에 들어있는 정수의 개수를 출력
        elif Query == ["size"]:
            print(len(Stack))
        
        # 스택이 비었다면 1, 아니면 0을 출력
        elif Query == ["empty"]:
            if len(Stack) == 0:
                print(1)
            else:
                print(0)

        # 스택 가장 위의 정수 출력, 스택이 비었다면 -1 출력
        elif Query == ["top"]:
            if len(Stack) == 0:
                print(-1)
            else:
                print(Stack[-1])
                    
    # push
    else:
        Stack.append(Query[1])
        
    