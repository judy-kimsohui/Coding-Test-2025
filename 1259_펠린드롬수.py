# 1259_펠린드롬수

def check(Number):
    for i in range(len(N)//2):
        if Number[i] != Number[-i-1]:
            return "no"
    return "yes"

while True:
    N = input()
    if N == "0":
        break    
    print(check(list(N)))
    
            
    
