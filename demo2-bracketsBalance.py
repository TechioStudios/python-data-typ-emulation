from stack import Stack



def bracketsBalance(str):
    BL = Stack()
    for i in str:
        if i in ['(','[','{']:
            BL.push(i)
        elif i in [')',']','}']:
            
            if BL.isEmpty():
                return False
            else:
                L = BL.pop()
                if (L == "(" and i != ")") or (L == "[" and i != "]") or (L == "{" and i != "}"):
                    return False
    return BL.isEmpty()


while True:
    print(bracketsBalance(input("Please input a string with brackets that you want to check:\n")))