#https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
#Given an array of integers.

#Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

#If the input array is empty or null, return an empty array

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    counter = 0
    sum = 0
    for i in arr:
        if i > 0:
            counter += 1
        elif i < 0:
            sum += i
    return [counter,sum]

