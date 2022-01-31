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
def process_digits(digit, operation):
    return digit if operation == None else operation(digit)
def zero(operation=None): 
    return process_digits(0,operation)
def one(operation=None): 
    return process_digits(1,operation)
def two(operation=None): 
    return process_digits(2,operation)
def three(operation=None): 
    return process_digits(3,operation)
def four(operation=None): 
    return process_digits(4,operation) 
def five(operation=None): 
    return process_digits(5,operation)
def six(operation=None): 
    return process_digits(6,operation)
def seven(operation=None): 
    return process_digits(7,operation)
def eight(operation=None): 
    return process_digits(8,operation)
def nine(operation=None): 
    return process_digits(9,operation)

def plus(n): 
    return lambda k: k + n
def minus(n): 
    return lambda k: k - n
def times(n): 
    return lambda k: k * n
def divided_by(n): 
    return lambda k: k // n
