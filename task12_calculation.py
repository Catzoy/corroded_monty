def zero(operation=None): 
    if operation == None:
        return 0
    return operation(0)
def one(operation=None): #your code here
    if operation == None:
        return 1
    return operation(1)
def two(operation=None): 
    if operation == None:
        return 2
    return operation(2)
def three(operation=None): #your code here
    if operation == None:
        return 3
    return operation(3)
def four(operation=None): #your code here
    if operation == None:
        return 4
    return operation(4) 
def five(operation=None): #your code here
    if operation == None:
        return 5
    return operation(5)
def six(operation=None): #your code here
    if operation == None:
        return 6
    return operation(6)
def seven(operation=None): #your code here
    if operation == None:
        return 7
    return operation(7)
def eight(operation=None): #your code here
    if operation == None:
        return 8
    return operation(8)
def nine(operation=None): #your code here
    if operation == None:
        return 9
    return operation(9)

def plus(n): #your code here
    return lambda k: k + n
def minus(n): #your code here
    return lambda k: k - n
def times(n): #your code here
    return lambda k: k * n
def divided_by(n): #your code here
    return lambda k: k // n
