#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
#You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

def sort_array(source_array):
    for i in range(len((source_array))):
        if (source_array[i] % 2) != 0:
            for n in range(len((source_array[i+1:]))):
                if ((source_array[n+i+1] % 2) != 0) and source_array[i] > source_array[n+i+1]:
                    source_array[i],source_array[n+i+1] = source_array[n+i+1],source_array[i]        
    return source_array

