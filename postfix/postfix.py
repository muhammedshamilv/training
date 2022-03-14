def postfix(expression):
    stack= []
    for i in expression:
        if i.isdigit():
            stack.append(int(i))
        elif i =="+":
            op1=stack.pop()
            op2= stack.pop()
            stack.append(op1+op2)
        elif i =="-":
            op1=stack.pop()
            op2= stack.pop()
            stack.append(op1-op2)
        elif i =="/":
            op1=stack.pop()
            op2= stack.pop()
            stack.append(op1/op2)
        elif i =="*":
            op1=stack.pop()
            op2= stack.pop()
            stack.append(op1*op2)
    return stack[0]

                                                    
