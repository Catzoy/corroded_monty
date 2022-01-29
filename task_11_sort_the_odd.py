#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
#You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def isEven(n):
    return n % 2 == 0

def sort_array(source_array):
    evens_counter = 0
    sorted_odds = sorted([x for x in source_array if not isEven(x)])
    for i in range(len((source_array))):
        if isEven(source_array[i]):
            evens_counter += 1
            continue
        source_array[i] = sorted_odds[i - evens_counter ]       
    return source_array


