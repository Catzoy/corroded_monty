def next_bigger(n):
    digits_array = [digit for digit in str(n)]
    max_num = int("".join(sorted(digits_array, reverse=True)))
    min_num = sorted(digits_array)
    output = n
    while output <= max_num:
        output += 1
        if sorted(list(str(output))) == min_num:
            return output
    return -1
print(next_bigger(890))
