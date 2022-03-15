def postfix(expression):
    stack= []
    operators=[]
    operand=[]
    for i in expression:
        if i.isdigit():
            operand.append(i)
        if i == '+' or i == '*' or i == '/' or i == '-':
            operators.append(i)
        if len(operand) <= len(operators):
            return "invalid expression"
    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+' or i == '*' or i == '/' or i == '-':
            op1=stack.pop()
            op2= stack.pop()
            if i =="+":
                stack.append(op1+op2)
            if i =="-":
                stack.append(op1-op2)
            if i =="/":
                stack.append(op1/op2)
            if i =="*":
                stack.append(op1*op2)
    return stack[0]                                    

