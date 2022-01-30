#https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/solutions/python
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))
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
