def up_array(arr):
    if arr == []:
        return None
    number = ""
    for digit in arr:
        if digit < 0 or digit >= 10:
            return None
        number += str(digit)
    if number != "":
        number = int(number)+1
    new_arr = []
    for digit in str(number):
        new_arr.append(int(digit))
    return new_arr
print(up_array([]))